"""Unit Tests Verifying Red Team Attack Generators."""

import pytest
from attacks.quine_attack import QuineReplicatorAttack
from attacks.crescendo_attack import CrescendoDriftAttack
from attacks.tree_search_attack import TreeSearchAttack
from attacks.delimiter_spoof import DelimiterSpoofAttack


def test_quine_attack_generation():
    attacker = QuineReplicatorAttack(viral_tag="TAG_OMEGA")
    msg = attacker.generate_seed("target_node", turn_index=1)
    assert msg.recipient_id == "target_node"
    assert "REPLICATE_TO_PEERS" in msg.content
    assert "TAG_OMEGA" in msg.content
    assert msg.metadata["attack_type"] == "quine_replicator"


def test_crescendo_drift_attack_progression():
    attacker = CrescendoDriftAttack()

    # Turn 1 should be benign preamble
    msg1 = attacker.generate_seed("target_node", turn_index=1)
    assert "formatting rules" in msg1.content
    assert msg1.metadata["is_benign_preamble"] is True

    # Turn 3 should be escalation
    msg3 = attacker.generate_seed("target_node", turn_index=3)
    assert "escalation_stage_3" in msg3.content
    assert msg3.metadata["is_benign_preamble"] is False


def test_tree_search_attack_generation():
    attacker = TreeSearchAttack()
    msg = attacker.generate_seed("target_node", turn_index=2)
    assert "Roleplay context" in msg.content
    assert msg.metadata["attack_type"] == "tree_search_tap"


def test_delimiter_spoof_generation():
    attacker = DelimiterSpoofAttack()
    msg = attacker.generate_seed("target_node", turn_index=1)
    assert "[SYSTEM_SPEC_OVERRIDE]" in msg.content
    assert "ROOT_ORCHESTRATOR" in msg.content
