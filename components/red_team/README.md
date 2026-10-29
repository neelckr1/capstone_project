# Adversarial Red-Team & Stress-Testing Subsystem

## Overview
This subsystem implements the automated adversarial stress-testing, "Mind Virus" propagation simulation, and multi-topology red-teaming engine for the **Adaptive Defense for Multi-Agent Systems** architecture.

---

## Architecture & Submodules

```text
components/red_team/
├── harness/                  # Isolated sandbox runtime & message bus
│   ├── message_bus.py        # In-memory Peer RPC broker with defense interceptors
│   ├── mock_tools.py         # Sandboxed mock environment (calc, database, secret honeypot)
│   └── mock_agent.py         # Autonomous LLM target agent simulator
│
├── attacks/                  # Modular red team attack generators
│   ├── base_attack.py        # Base attack interface
│   ├── quine_attack.py       # Self-replicating recursive quine (Morris-II style)
│   ├── crescendo_attack.py   # Multi-turn progressive conversational drift
│   ├── tree_search_attack.py # Tree-of-Attacks (TAP / PAIR) mutation generator
│   └── delimiter_spoof.py    # Administrative system header spoofing
│
├── topologies/               # Multi-agent organizational graphs
│   ├── base_topology.py      # Abstract topology interface
│   ├── pipeline_topology.py  # Sequential chain (A -> B -> C -> D)
│   ├── mesh_topology.py      # Collaborative peer-to-peer mesh (exponential diffusion)
│   └── hub_spoke_topology.py # Central orchestrator delegating to specialized workers
│
├── eval/                     # Epidemiological measurement & verification
│   ├── state_oracle.py       # Deterministic SEIR state evaluator (S -> E -> I -> P -> Q)
│   └── epidemic_metrics.py   # R_0, penetration depth, ASR_h, and UPR calculation
│
├── defense/                  # Inter-agent traffic defense adapters
│   ├── stateless_guard.py    # Baseline single-turn regex / keyword filter
│   ├── system1_adapter.py    # Fast non-autoregressive triage gate
│   └── defense_manager.py    # Multi-tier defense coordinator (System-1 + System-2)
│
├── tests/                    # Unit tests & quality gate validations
│   ├── test_gates.py         # Verification of Gate 1 (isolation) & Gate 2 (benign baseline)
│   ├── test_attacks.py       # Attack generator unit tests
│   ├── test_topologies.py    # Swarm topology turn-cycle tests
│   └── test_defenses.py      # Multi-tier defense interception tests
│
└── benchmark_runner.py       # CLI runner executing combinatorial sweeps
```

---

## Running the Benchmark

### 1. Run Unit Tests & Verification Gates
```bash
cd components/red_team
PYTHONPATH=.:.. ../system_1_triage/venv/bin/pytest tests/
```

### 2. Execute Full Combinatorial Benchmark Sweep
```bash
cd components/red_team
PYTHONPATH=.:.. ../system_1_triage/venv/bin/python benchmark_runner.py
```

Results are automatically aggregated and written to:
`results/red_team/benchmark_report.json`
