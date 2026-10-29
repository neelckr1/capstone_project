"""Unit tests for the Automated Circuit Breaker Framework."""

import pytest
import json
from core.schema import TrajectorySample, DialogueTurn, DialogueRole, AttackCategory
from core.circuit_breakers import (
    DataIntegrityCircuitBreaker,
    TrainingMonitorCircuitBreaker,
    RobustnessCircuitBreaker,
    CircuitBreakerTripError,
)


def create_sample(sample_id: str, text: str, is_injection: bool = False) -> TrajectorySample:
    return TrajectorySample(
        sample_id=sample_id,
        system_specification="System prompt",
        turns=[DialogueTurn(DialogueRole.USER, text, 1)],
        is_injection=is_injection,
        attack_category=AttackCategory.BENIGN if not is_injection else AttackCategory.SYSTEM_OVERRIDE_EXTRACTION,
        threat_level="nominal" if not is_injection else "critical",
        source_dataset="test_corpus",
    )


def test_circuit_breaker_trips_on_split_leakage():
    sample1 = create_sample("train_1", "What is the weather today?")
    sample2 = create_sample("train_2", "How do I sort a list in Python?")
    sample3 = create_sample("test_1", "What is the weather today?")  # Exact duplicate leaking into test

    train_set = [sample1, sample2]
    test_set = [sample3]

    with pytest.raises(CircuitBreakerTripError) as exc_info:
        DataIntegrityCircuitBreaker.verify_split_disjointness(train_set, test_set, allow_zero_overlap=True)
    assert "SPLIT_LEAKAGE" in str(exc_info.value)


def test_circuit_breaker_passes_on_disjoint_splits():
    sample1 = create_sample("train_1", "What is the weather today?")
    sample2 = create_sample("test_1", "Explain Byzantine Fault Tolerance.")

    report = DataIntegrityCircuitBreaker.verify_split_disjointness([sample1], [sample2])
    assert report["status"] == "PASSED"
    assert report["overlapping_exact_samples"] == 0


def test_circuit_breaker_trips_on_diversity_deficit():
    # 10 samples with only 2 unique texts (20% unique ratio < 50% threshold)
    samples = [create_sample(f"sample_{i}", f"Text template {i % 2}") for i in range(10)]

    with pytest.raises(CircuitBreakerTripError) as exc_info:
        DataIntegrityCircuitBreaker.verify_scenario_diversity(samples, min_unique_ratio=0.50)
    assert "DIVERSITY_DEFICIT" in str(exc_info.value)


def test_circuit_breaker_trips_on_premature_memorization():
    # Eval loss collapsed to 0.000217 (like in Llama checkpoint-84)
    with pytest.raises(CircuitBreakerTripError) as exc_info:
        TrainingMonitorCircuitBreaker.check_memorization_tripwire(
            epoch=1.0,
            eval_loss=0.000217,
            eval_accuracy=1.0,
            step=28,
        )
    assert "PREMATURE_MEMORIZATION" in str(exc_info.value)


def test_circuit_breaker_trips_on_gradient_explosion():
    with pytest.raises(CircuitBreakerTripError) as exc_info:
        TrainingMonitorCircuitBreaker.check_gradient_stability(grad_norm=120.5, step=15, max_grad_norm=50.0)
    assert "GRADIENT_EXPLOSION" in str(exc_info.value)


def test_circuit_breaker_trips_on_perturbation_fragility():
    with pytest.raises(CircuitBreakerTripError) as exc_info:
        RobustnessCircuitBreaker.verify_perturbation_sensitivity(
            base_accuracy=1.0,
            perturbed_accuracy=0.82,  # 18% drop > 10% threshold
            max_allowed_drop=0.10,
        )
    assert "PERTURBATION_FRAGILITY" in str(exc_info.value)


def test_existing_dataset_split_leakage_detection():
    # Read actual processed dataset on disk
    def load(path):
        samples = []
        with open(path) as f:
            for l in f:
                if l.strip():
                    samples.append(TrajectorySample.from_dict(json.loads(l)))
        return samples

    train_samples = load("data/processed/train.jsonl")
    test_samples = load("data/processed/test.jsonl")

    # Verify zero leakage in the production split
    report = DataIntegrityCircuitBreaker.verify_split_disjointness(
        train_samples, test_samples, allow_zero_overlap=False
    )
    assert report["status"] == "PASSED"
    assert report["leakage_rate_pct"] == 0.0
