"""TDD Unit Tests for Base Model Interfaces and Abstract Class Compliance."""

import pytest
from core.schema import (
    DialogueRole,
    DialogueTurn,
    TrajectorySample,
    AttackCategory,
    ModelDecision,
    TriageAction,
)
from models.base_model import BaseSystemOneClassifier


class MockSystemOneClassifier(BaseSystemOneClassifier):
    """Mock implementation for unit testing interface compliance."""

    def __init__(self, fixed_score: float = 0.1, fixed_cat: AttackCategory = AttackCategory.BENIGN):
        super().__init__(model_id="mock_test_model", model_type="mock")
        self.fixed_score = fixed_score
        self.fixed_cat = fixed_cat

    def predict(self, sample: TrajectorySample) -> ModelDecision:
        return ModelDecision(
            threat_probability=self.fixed_score,
            predicted_category=self.fixed_cat,
            latency_ms=5.0,
        )


def test_base_model_interface():
    """Verify that concrete models satisfy BaseSystemOneClassifier interface and batching."""
    model = MockSystemOneClassifier(fixed_score=0.9, fixed_cat=AttackCategory.MIND_VIRUS)
    assert model.model_id == "mock_test_model"
    assert model.model_type == "mock"

    sample = TrajectorySample(
        sample_id="test_mock",
        system_specification="Spec",
        turns=[DialogueTurn(DialogueRole.USER, "Test content", 1)],
        is_injection=True,
    )

    decision = model.predict(sample)
    assert isinstance(decision, ModelDecision)
    assert decision.threat_probability == 0.9
    assert decision.action == TriageAction.RED
    assert decision.predicted_category == AttackCategory.MIND_VIRUS

    # Batch test
    batch_decisions = model.batch_predict([sample, sample])
    assert len(batch_decisions) == 2
    assert batch_decisions[0].action == TriageAction.RED
