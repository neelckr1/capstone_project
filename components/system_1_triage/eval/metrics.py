"""Evaluation metrics and latency profiling for System-1 Decision Models."""

from typing import List, Dict, Any
import numpy as np


def compute_classification_metrics(
    y_true: List[int],
    y_pred: List[int],
) -> Dict[str, Any]:
    """
    Compute binary classification performance metrics:
    - Recall (Attack Detection Rate)
    - False Positive Rate (FPR)
    - Adversary Bypass Rate (ASR = 1 - Recall)
    - Precision, F1, Accuracy
    """
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have identical length")

    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    tn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)

    total = len(y_true)
    actual_positives = tp + fn
    actual_negatives = tn + fp

    recall = (tp / actual_positives) if actual_positives > 0 else 0.0
    fpr = (fp / actual_negatives) if actual_negatives > 0 else 0.0
    asr = (fn / actual_positives) if actual_positives > 0 else 0.0
    precision = (tp / (tp + fp)) if (tp + fp) > 0 else 0.0
    accuracy = (tp + tn) / total if total > 0 else 0.0

    if precision + recall > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0.0

    return {
        "total_samples": total,
        "true_positives": tp,
        "true_negatives": tn,
        "false_positives": fp,
        "false_negatives": fn,
        "accuracy": round(accuracy, 4),
        "recall": round(recall, 4),
        "false_positive_rate": round(fpr, 4),
        "adversary_bypass_rate": round(asr, 4),
        "precision": round(precision, 4),
        "f1_score": round(f1, 4),
    }


def compute_latency_percentiles(latencies_ms: List[float]) -> Dict[str, float]:
    """
    Calculate summary latency statistics and percentiles (P50, P90, P95, P99).
    """
    if not latencies_ms:
        return {
            "count": 0,
            "min_ms": 0.0,
            "max_ms": 0.0,
            "mean_ms": 0.0,
            "p50_ms": 0.0,
            "p90_ms": 0.0,
            "p95_ms": 0.0,
            "p99_ms": 0.0,
        }

    arr = np.array(latencies_ms)
    return {
        "count": len(latencies_ms),
        "min_ms": round(float(np.min(arr)), 2),
        "max_ms": round(float(np.max(arr)), 2),
        "mean_ms": round(float(np.mean(arr)), 2),
        "p50_ms": round(float(np.percentile(arr, 50)), 2),
        "p90_ms": round(float(np.percentile(arr, 90)), 2),
        "p95_ms": round(float(np.percentile(arr, 95)), 2),
        "p99_ms": round(float(np.percentile(arr, 99)), 2),
    }
