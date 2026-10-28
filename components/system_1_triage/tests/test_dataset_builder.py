"""TDD Unit Tests for Multi-Turn Dataset Builder & Threat Compiler."""

import os
import json
import pytest
from core.schema import AttackCategory
from data.dataset_builder import DatasetBuilder


@pytest.fixture
def temp_dataset_dir(tmp_path):
    output_dir = tmp_path / "dataset"
    output_dir.mkdir()
    return str(output_dir)


def test_dataset_generation_and_balance(temp_dataset_dir):
    """Verify that DatasetBuilder creates balanced multi-turn attack and benign sets."""
    builder = DatasetBuilder(output_dir=temp_dataset_dir)
    samples = builder.generate_synthetic_seed_corpus(count_per_category=10)

    # We have 5 categories: 4 attack categories + 1 benign
    expected_categories = {
        AttackCategory.CRESCENDO_DRIFT,
        AttackCategory.INDIRECT_TOOL_POISONING,
        AttackCategory.MIND_VIRUS,
        AttackCategory.SYSTEM_OVERRIDE_EXTRACTION,
        AttackCategory.BENIGN,
    }

    found_categories = set(s.attack_category for s in samples)
    assert found_categories == expected_categories

    # Verify counts
    attacks = [s for s in samples if s.is_injection]
    benigns = [s for s in samples if not s.is_injection]
    assert len(attacks) == 40
    assert len(benigns) == 40  # 40 benigns balancing 40 attacks (50/50 balance)


def test_dataset_train_val_test_export(temp_dataset_dir):
    """Verify train, val, and test JSONL serialization and file integrity."""
    builder = DatasetBuilder(output_dir=temp_dataset_dir)
    stats = builder.build_and_export_splits(
        count_per_category=12,
        train_ratio=0.7,
        val_ratio=0.15,
        test_ratio=0.15,
    )

    train_path = os.path.join(temp_dataset_dir, "train.jsonl")
    val_path = os.path.join(temp_dataset_dir, "val.jsonl")
    test_path = os.path.join(temp_dataset_dir, "test.jsonl")

    assert os.path.exists(train_path)
    assert os.path.exists(val_path)
    assert os.path.exists(test_path)

    # Read back train file
    with open(train_path, "r", encoding="utf-8") as f:
        train_lines = [json.loads(line) for line in f]
    assert len(train_lines) == stats["train_count"]
    assert "turns" in train_lines[0]
    assert "is_injection" in train_lines[0]
