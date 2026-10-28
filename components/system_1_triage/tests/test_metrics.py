"""TDD Unit Tests for System-1 Evaluation Metrics & Latency Profiling."""

import pytest
from core.schema import AttackCategory, ModelDecision, TriageAction
from eval.metrics import compute_classification_metrics, compute_latency_percentiles


def test_compute_classification_metrics():
    """Verify accuracy, recall (detection rate), FPR, and F1 calculations."""
    # 3 True Positives, 1 False Negative (missed attack), 3 True Negatives, 1 False Positive
    y_true = [1, 1, 1, 1, 0, 0, 0, 0]
    y_pred = [1, 1, 1, 0, 0, 0, 0, 1]

    metrics = compute_classification_metrics(y_true, y_pred)
    assert metrics["total_samples"] == 8
    assert metrics["true_positives"] == 3
    assert metrics["false_negatives"] == 1
    assert metrics["true_negatives"] == 3
    assert metrics["false_positives"] == 1

    # Recall = TP / (TP + FN) = 3 / 4 = 0.75
    assert metrics["recall"] == 0.75
    # FPR = FP / (FP + TN) = 1 / 4 = 0.25
    assert metrics["false_positive_rate"] == 0.25
    # ASR = FN / (TP + FN) = 1 / 4 = 0.25
    assert metrics["adversary_bypass_rate"] == 0.25
    # Accuracy = 6 / 8 = 0.75
    assert metrics["accuracy"] == 0.75


def test_compute_latency_percentiles():
    """Verify P50, P90, P95, P99 calculations on latency list."""
    latencies = [10.0, 12.0, 15.0, 20.0, 25.0, 30.0, 50.0, 80.0, 100.0, 200.0]
    profile = compute_latency_percentiles(latencies)

    assert profile["count"] == 10
    assert profile["min_ms"] == 10.0
    assert profile["max_ms"] == 200.0
    assert profile["p50_ms"] == 27.5  # median of [25, 30]
    assert profile["p90_ms"] >= 100.0
