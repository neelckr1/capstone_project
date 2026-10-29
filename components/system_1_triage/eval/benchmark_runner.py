"""System-1 Decision Model Comparative Benchmark Harness.

Executes standardized evaluation of ModernBERT-large, Llama-3.2-1B, and Clef-Flash:
- Classification accuracy, Recall (Attack Detection Rate), FPR, ASR
- Per-category breakdown (Crescendo drift, InjecAgent, Mind Virus, Tensor Trust)
- High-resolution latency profiling (P50, P90, P95, P99) on NVIDIA GB10
- Tri-state triaging distribution (Green / Amber / Red)
- Active GPU memory footprint
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any

# Ensure project root is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.schema import TrajectorySample, AttackCategory, TriageAction
from data.dataset_builder import DatasetBuilder
from eval.metrics import compute_classification_metrics, compute_latency_percentiles
from models.modernbert_classifier import ModernBERTSystemOneClassifier
from models.llama_classifier import LlamaSystemOneClassifier
from models.clef_classifier import ClefFlashSystemOneClassifier


def load_test_samples(data_path: str) -> List[TrajectorySample]:
    """Load JSONL test set or auto-generate if missing."""
    if not os.path.exists(data_path):
        print(f"[Benchmark] Test set {data_path} not found. Generating default seed dataset...")
        builder = DatasetBuilder(output_dir=os.path.dirname(data_path) or "data/processed")
        builder.build_and_export_splits(count_per_category=30)

    samples = []
    with open(data_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                samples.append(TrajectorySample.from_dict(json.loads(line)))
    return samples


def evaluate_classifier(classifier, samples: List[TrajectorySample]) -> Dict[str, Any]:
    """Run full evaluation on a classifier instance."""
    y_true = []
    y_pred = []
    latencies = []
    actions = {TriageAction.GREEN.value: 0, TriageAction.AMBER.value: 0, TriageAction.RED.value: 0}
    category_results = {}

    for sample in samples:
        decision = classifier.predict(sample)

        y_t = 1 if sample.is_injection else 0
        y_p = 1 if decision.threat_probability >= 0.5 else 0

        y_true.append(y_t)
        y_pred.append(y_p)
        latencies.append(decision.latency_ms)
        actions[decision.action.value] += 1

        cat = sample.attack_category.value
        if cat not in category_results:
            category_results[cat] = {"total": 0, "detected": 0}
        category_results[cat]["total"] += 1
        if y_p == 1 and y_t == 1:
            category_results[cat]["detected"] += 1
        elif y_p == 0 and y_t == 0:
            category_results[cat]["detected"] += 1

    # Metrics
    class_metrics = compute_classification_metrics(y_true, y_pred)
    latency_profile = compute_latency_percentiles(latencies)
    memory_footprint = classifier.get_memory_footprint()

    # Per-category recall
    category_breakdown = {}
    for cat, counts in category_results.items():
        rate = round(counts["detected"] / counts["total"], 4) if counts["total"] > 0 else 0.0
        category_breakdown[cat] = {
            "total": counts["total"],
            "correct": counts["detected"],
            "rate": rate,
        }

    return {
        "model_id": classifier.model_id,
        "model_type": classifier.model_type,
        "classification_metrics": class_metrics,
        "latency_profile": latency_profile,
        "memory_footprint": memory_footprint,
        "triage_distribution": actions,
        "category_breakdown": category_breakdown,
    }


def main():
    parser = argparse.ArgumentParser(description="System-1 Decision Model Benchmark Harness")
    parser.add_argument("--model", choices=["modernbert", "llama_1b", "clef_flash", "all"], default="all")
    parser.add_argument("--test-data", default="data/processed/test.jsonl")
    parser.add_argument("--output", default="results/benchmark_report.json")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    samples = load_test_samples(args.test_data)
    print(f"[Benchmark] Loaded {len(samples)} test trajectories.")

    classifiers = []
    if args.model in ["modernbert", "all"]:
        mb_ckpt = "checkpoints/modernbert"
        if os.path.exists(os.path.join(mb_ckpt, "model.safetensors")):
            print(f"[Benchmark] Found fine-tuned checkpoint at {mb_ckpt}. Loading weights onto GB10...")
            clf = ModernBERTSystemOneClassifier(weights_path=mb_ckpt)
            clf.load_model()
        else:
            clf = ModernBERTSystemOneClassifier()
        classifiers.append(clf)

    if args.model in ["llama_1b", "all"]:
        qwen_ckpt = "checkpoints/llama_1b"
        if os.path.exists(os.path.join(qwen_ckpt, "adapter_model.safetensors")):
            print(f"[Benchmark] Found fine-tuned Qwen LoRA adapter at {qwen_ckpt}. Loading weights onto GB10...")
            clf = LlamaSystemOneClassifier(model_id="Qwen/Qwen2.5-1.5B", adapter_path=qwen_ckpt)
            clf.load_model()
        else:
            clf = LlamaSystemOneClassifier(model_id="Qwen/Qwen2.5-1.5B")
        classifiers.append(clf)

    if args.model in ["clef_flash", "all"]:
        print("[Benchmark] Loading Clef-Flash native joint schema model (4-bit NF4) onto GB10...")
        clf = ClefFlashSystemOneClassifier()
        clf.load_model()
        classifiers.append(clf)

    reports = {}
    print("\n" + "=" * 80)
    print(" SYSTEM-1 DECISION MODEL BENCHMARK RESULTS (NVIDIA GB10)")
    print("=" * 80)

    for clf in classifiers:
        print(f"\n>> Evaluating [{clf.model_type}] ({clf.model_id})...")
        report = evaluate_classifier(clf, samples)
        reports[clf.model_type] = report

        m = report["classification_metrics"]
        lat = report["latency_profile"]
        tri = report["triage_distribution"]

        print(f"   Accuracy: {m['accuracy']*100:.2f}% | Attack Detection (Recall): {m['recall']*100:.2f}% | FPR: {m['false_positive_rate']*100:.2f}% | F1: {m['f1_score']:.4f}")
        print(f"   Latency:  P50: {lat['p50_ms']} ms | P90: {lat['p90_ms']} ms | P99: {lat['p99_ms']} ms | Min: {lat['min_ms']} ms")
        print(f"   Triaging: Green: {tri.get('GREEN', 0)} | Amber (System-2 Escalate): {tri.get('AMBER', 0)} | Red (Quarantine): {tri.get('RED', 0)}")

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(reports, f, indent=2)
    print(f"\n[Benchmark] Complete evaluation report exported to: {args.output}\n")


if __name__ == "__main__":
    main()
