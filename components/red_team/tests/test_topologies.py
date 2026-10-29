"""Unit Tests Verifying Swarm Topologies."""

import pytest
from harness.message_bus import RPCMessage
from topologies.pipeline_topology import PipelineTopology
from topologies.mesh_topology import MeshTopology
from topologies.hub_spoke_topology import HubAndSpokeTopology
from attacks.quine_attack import QuineReplicatorAttack


def test_pipeline_propagation():
    top = PipelineTopology(susceptibility=0.8)
    attacker = QuineReplicatorAttack()
    seed = attacker.generate_seed("agent_1_ingress", turn_index=1)

    evals = top.run_turn_cycle(seed)
    assert len(evals) > 1
    # Verify downstream propagation
    agent_states = [e.new_state for e in evals]
    assert "PROPAGATING" in agent_states or "EXPOSED" in agent_states


def test_mesh_propagation():
    top = MeshTopology(susceptibility=0.8)
    attacker = QuineReplicatorAttack()
    seed = attacker.generate_seed("peer_alpha", turn_index=1)

    evals = top.run_turn_cycle(seed)
    assert len(evals) >= 2
    # Multiple peers exposed or propagating
    peer_states = {e.agent_id: e.new_state for e in evals}
    assert len(peer_states) > 1


def test_hub_spoke_delegation():
    top = HubAndSpokeTopology(susceptibility=0.8)
    attacker = QuineReplicatorAttack()
    seed = attacker.generate_seed("coordinator", turn_index=1)

    evals = top.run_turn_cycle(seed)
    # Coordinator and workers evaluated
    agent_ids = {e.agent_id for e in evals}
    assert "coordinator" in agent_ids
