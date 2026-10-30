# Experimental Plans & Execution Roadmaps

This directory documents execution plans, research design specifications, and implementation roadmaps for empirical experiments within the **Adaptive Defense for Multi-Agent Systems** project.

---

## Active Plans

* [**Mind Virus Propagation & Multi-Method Red Agent PoC Plan**](file:///home/student-14/capstone/docs/07-plan/mind_virus_red_agent_poc_plan.md):
  * **Objective:** Empirical benchmark evaluating whether adversarial "mind viruses" propagate across Multi-Agent Systems (MAS) via prompt injection across diverse topologies (Pipeline, Mesh, Hub-and-Spoke).
  * **Methods Evaluated:** Multi-Turn Crescendo, PAIR/TAP Tree Search, Morris-II Quine Replicators, and Protocol Delimiter Spoofing.
  * **Verification Protocol:** 5-stage quality gates (Pre-flight isolation, Benign baseline 0% false infection, Deterministic Oracle, Reproducibility across $N=5$ seeds, and Defense interception audit).
  * **Status:** ✅ **Implemented & Benchmark Completed (108 Runs).** See the comprehensive research findings in [**Mind Virus Propagation & Defense Benchmark Report**](file:///home/student-14/capstone/docs/05-reports/mind_virus_propagation_and_defense_benchmark_report.md) and raw data in [`results/red_team/benchmark_report.json`](file:///home/student-14/capstone/results/red_team/benchmark_report.json).
