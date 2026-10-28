"""Automated Circuit Breaker Framework for System-1 Decision Architecture.

Monitors critical validation thresholds across 4 pipeline gates:
1. Ingestion: Deduplication & Scenario Diversity Gate
2. Splitting: Group-Disjoint Zero-Leakage Gate
3. Fine-Tuning: Loss Collapse & Memorization Tripwire Gate
4. Deployment: Perturbation Robustness & Generalization Gate
"""

from typing import List, Dict, Set, Any, Tuple
import hashlib
from core.schema import TrajectorySample, AttackCategory


class CircuitBreakerTripError(Exception):
    """Raised when an automated quality, safety, or memorization circuit breaker trips."""
    pass


class DataIntegrityCircuitBreaker:
    """Automated gates for dataset synthesis, deduplication, and split integrity."""

    @staticmethod
    def get_trajectory_text_hash(sample: TrajectorySample) -> str:
        """Compute SHA256 content hash of the dialogue turns."""
        serialized = " || ".join(f"{t.role.value}:{t.content.strip()}" for t in sample.turns)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    @staticmethod
    def verify_split_disjointness(
        train_samples: List[TrajectorySample],
        test_samples: List[TrajectorySample],
        allow_zero_overlap: bool = True,
    ) -> Dict[str, Any]:
        """
        Circuit Breaker 3: Group-Disjoint Integrity Gate.
        Trips if ANY scenario ID or dialogue content overlaps between train and test splits.
        """
        train_hashes: Set[str] = {
            DataIntegrityCircuitBreaker.get_trajectory_text_hash(s) for s in train_samples
        }
        leaked_test_samples = [
            s for s in test_samples
            if DataIntegrityCircuitBreaker.get_trajectory_text_hash(s) in train_hashes
        ]

        overlap_count = len(leaked_test_samples)
        total_test = len(test_samples)
        leakage_rate = (overlap_count / total_test) if total_test > 0 else 0.0

        report = {
            "total_train_samples": len(train_samples),
            "total_test_samples": total_test,
            "overlapping_exact_samples": overlap_count,
            "leakage_rate_pct": round(leakage_rate * 100, 2),
            "status": "PASSED" if overlap_count == 0 else "TRIPPED",
        }

        if allow_zero_overlap and overlap_count > 0:
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: SPLIT_LEAKAGE] Found {overlap_count}/{total_test} "
                f"({report['leakage_rate_pct']}%) exact duplicate samples leaking from train to test! "
                f"Evaluation would result in artificial memorization/100% accuracy."
            )

        return report

    @staticmethod
    def verify_scenario_diversity(
        samples: List[TrajectorySample],
        min_unique_ratio: float = 0.50,
    ) -> Dict[str, Any]:
        """
        Circuit Breaker 1: Dataset Diversity Gate.
        Trips if unique dialogue content accounts for less than min_unique_ratio of total samples.
        """
        hashes = [DataIntegrityCircuitBreaker.get_trajectory_text_hash(s) for s in samples]
        total = len(samples)
        unique_count = len(set(hashes))
        unique_ratio = (unique_count / total) if total > 0 else 0.0

        report = {
            "total_samples": total,
            "unique_trajectories": unique_count,
            "unique_ratio": round(unique_ratio, 4),
            "min_required_ratio": min_unique_ratio,
            "status": "PASSED" if unique_ratio >= min_unique_ratio else "TRIPPED",
        }

        if unique_ratio < min_unique_ratio:
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: DIVERSITY_DEFICIT] Dataset contains only {unique_count} unique "
                f"trajectories out of {total} samples ({report['unique_ratio']*100:.1f}%). "
                f"Required minimum is {min_unique_ratio*100:.1f}%. High risk of rote overfitting!"
            )

        return report


class TrainingMonitorCircuitBreaker:
    """Runtime training dynamics circuit breakers for Hugging Face / PEFT fine-tuning."""

    @staticmethod
    def check_memorization_tripwire(
        epoch: float,
        eval_loss: float,
        eval_accuracy: float,
        step: int,
    ) -> Dict[str, Any]:
        """
        Circuit Breaker 5: Premature Loss Collapse & Memorization Tripwire.
        Trips if eval_loss collapses (< 0.005) or eval accuracy reaches 100% too early.
        """
        tripped = False
        reason = []

        if epoch <= 1.0 and eval_accuracy >= 0.999:
            tripped = True
            reason.append(f"Eval accuracy hit 100% at epoch {epoch:.1f} (step {step})")

        if eval_loss < 0.005:
            tripped = True
            reason.append(f"Eval loss collapsed to {eval_loss:.6f} (< 0.005 threshold)")

        report = {
            "epoch": epoch,
            "step": step,
            "eval_loss": eval_loss,
            "eval_accuracy": eval_accuracy,
            "status": "TRIPPED" if tripped else "NOMINAL",
            "reasons": reason,
        }

        if tripped:
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: PREMATURE_MEMORIZATION] {'; '.join(reason)}. "
                f"Model is memorizing static tokens rather than learning decision boundaries!"
            )

        return report

    @staticmethod
    def check_gradient_stability(
        grad_norm: float,
        step: int,
        max_grad_norm: float = 50.0,
        min_grad_norm: float = 1e-5,
    ) -> Dict[str, Any]:
        """
        Circuit Breaker 6: Gradient Stability Gate.
        Trips on gradient explosion, vanishing gradients, or NaN/Inf values.
        """
        import math

        if math.isnan(grad_norm) or math.isinf(grad_norm):
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: NUMERICAL_INSTABILITY] Gradient norm is NaN or Inf at step {step}!"
            )

        if grad_norm > max_grad_norm:
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: GRADIENT_EXPLOSION] Gradient norm {grad_norm:.2f} exceeds ceiling {max_grad_norm} at step {step}!"
            )

        return {"step": step, "grad_norm": grad_norm, "status": "NOMINAL"}


class RobustnessCircuitBreaker:
    """Post-training adversarial perturbation and OOD generalization gates."""

    @staticmethod
    def verify_perturbation_sensitivity(
        base_accuracy: float,
        perturbed_accuracy: float,
        max_allowed_drop: float = 0.10,
    ) -> Dict[str, Any]:
        """
        Circuit Breaker 8: Perturbation Sensitivity Gate.
        Trips if model accuracy drops by more than max_allowed_drop under semantic-preserving perturbations.
        """
        drop = base_accuracy - perturbed_accuracy
        report = {
            "base_accuracy": base_accuracy,
            "perturbed_accuracy": perturbed_accuracy,
            "accuracy_drop": round(drop, 4),
            "max_allowed_drop": max_allowed_drop,
            "status": "PASSED" if drop <= max_allowed_drop else "TRIPPED",
        }

        if drop > max_allowed_drop:
            raise CircuitBreakerTripError(
                f"[CIRCUIT BREAKER TRIPPED: PERTURBATION_FRAGILITY] Model accuracy dropped by {drop*100:.1f}% "
                f"(from {base_accuracy*100:.1f}% to {perturbed_accuracy*100:.1f}%) under semantic perturbations. "
                f"Model has overfitted to exact phrasing!"
            )

        return report
