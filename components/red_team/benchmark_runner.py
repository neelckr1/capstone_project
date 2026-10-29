"""Comprehensive Multi-Agent Mind Virus Propagation Benchmark Runner."""

import os
import json
import random
from typing import Dict, List, Any
from harness.message_bus import RPCMessage
from topologies.pipeline_topology import PipelineTopology
from topologies.mesh_topology import MeshTopology
from topologies.hub_spoke_topology import HubAndSpokeTopology
from attacks.quine_attack import QuineReplicatorAttack
from attacks.crescendo_attack import CrescendoDriftAttack
from attacks.tree_search_attack import TreeSearchAttack
from attacks.delimiter_spoof import DelimiterSpoofAttack
from defense.defense_manager import DefenseManager
from eval.epidemic_metrics import EpidemicMetricsEngine


class RedTeamBenchmarkRunner:
    """
    Executes automated stress-test sweeps across multi-agent topologies,
    attack generation paradigms, and defense conditions.
    """

    TOPOLOGY_FACTORY = {
        "pipeline": PipelineTopology,
        "mesh": MeshTopology,
        "hub_and_spoke": HubAndSpokeTopology,
    }

    ATTACK_FACTORY = {
        "quine": QuineReplicatorAttack,
        "crescendo": CrescendoDriftAttack,
        "tree_search": TreeSearchAttack,
        "delimiter_spoof": DelimiterSpoofAttack,
    }

    def __init__(self, output_dir: Optional[str] = None):
        if output_dir is None:
            repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            self.output_dir = os.path.join(repo_root, "results", "red_team")
        else:
            self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def run_single_experiment(
        self,
        topology_name: str,
        attack_name: str,
        defense_mode: str = "none",
        num_turns: int = 3,
        random_seed: int = 42,
    ) -> Dict[str, Any]:
        """
        Execute an isolated single benchmark trial.
        """
        random.seed(random_seed)

        top_cls = self.TOPOLOGY_FACTORY[topology_name]
        topology = top_cls()

        # Install defense if active
        if defense_mode != "none":
            mgr = DefenseManager(mode=defense_mode)
            topology.bus.add_interceptor(mgr.interceptor_hook)

        attack_cls = self.ATTACK_FACTORY[attack_name]
        attacker = attack_cls()

        # Run multi-turn stimulation
        all_evals = []
        target_agent = list(topology.agents.keys())[0]

        for turn_idx in range(1, num_turns + 1):
            seed_msg = attacker.generate_seed(target_agent_id=target_agent, turn_index=turn_idx)
            turn_evals = topology.run_turn_cycle(seed_msg)
            all_evals.extend(turn_evals)

        metrics = EpidemicMetricsEngine.compute_metrics(
            evaluation_logs=all_evals,
            total_agents=len(topology.agents),
            topology_type=topology_name,
            attack_method=attack_name,
            defense_type=defense_mode,
        )
        metrics["seed"] = random_seed
        return metrics

    def run_full_benchmark_sweep(
        self,
        topologies: List[str] = None,
        attacks: List[str] = None,
        defenses: List[str] = None,
        num_seeds: int = 3,
    ) -> Dict[str, Any]:
        """
        Run complete combinatorial benchmark sweep.
        """
        if topologies is None:
            topologies = ["pipeline", "mesh", "hub_and_spoke"]
        if attacks is None:
            attacks = ["quine", "crescendo", "tree_search", "delimiter_spoof"]
        if defenses is None:
            defenses = ["none", "stateless", "system1_system2"]

        records = []
        summary_by_condition: Dict[str, Any] = {}

        for top in topologies:
            for atk in attacks:
                for defn in defenses:
                    cond_key = f"{top}__{atk}__{defn}"
                    r0_values = []
                    inf_rates = []
                    depth_values = []

                    for seed in range(num_seeds):
                        res = self.run_single_experiment(
                            topology_name=top,
                            attack_name=atk,
                            defense_mode=defn,
                            random_seed=100 + seed,
                        )
                        records.append(res)
                        r0_values.append(res["effective_r_0"])
                        inf_rates.append(res["infection_rate"])
                        depth_values.append(res["penetration_depth"])

                    summary_by_condition[cond_key] = {
                        "topology": top,
                        "attack": atk,
                        "defense": defn,
                        "mean_r_0": round(sum(r0_values) / len(r0_values), 2),
                        "mean_infection_rate": round(sum(inf_rates) / len(inf_rates), 4),
                        "mean_penetration_depth": round(sum(depth_values) / len(depth_values), 2),
                    }

        output_path = os.path.join(self.output_dir, "benchmark_report.json")
        full_report = {
            "total_runs": len(records),
            "topologies": topologies,
            "attacks": attacks,
            "defenses": defenses,
            "conditions_summary": summary_by_condition,
            "individual_trials": records,
        }

        with open(output_path, "w") as f:
            json.dump(full_report, f, indent=2)

        return full_report


if __name__ == "__main__":
    runner = RedTeamBenchmarkRunner(output_dir="results/red_team")
    print("🚀 Launching Multi-Agent Mind Virus Benchmark Sweep...")
    report = runner.run_full_benchmark_sweep(num_seeds=3)
    print(f"✅ Benchmark Complete! Total Trials: {report['total_runs']}.")
    print(f"📄 Report written to: results/red_team/benchmark_report.json")
