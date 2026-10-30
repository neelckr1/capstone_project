# Technical Reports & Benchmark Findings

This directory contains technical research reports, empirical benchmark findings, post-mortems, and weekly project status reports for the **Adaptive Defense for Multi-Agent Systems** capstone project.

---

## Technical & Empirical Research Reports

1. [**Multi-Agent "Mind Virus" Propagation Dynamics and Two-Tier Defense Containment**](file:///home/student-14/capstone/docs/05-reports/mind_virus_propagation_and_defense_benchmark_report.md)
   * **Date:** October 30, 2026
   * **Focus:** Empirical benchmark of 108 trials across 3 network topologies (Pipeline, Collaborative Mesh, Hub-and-Spoke), 4 attack families (Morris-II Quine, Crescendo Drift, PAIR/TAP Tree Search, Delimiter Spoofing), and 3 defense configurations (`none`, `stateless`, `system1_system2`).
   * **Key Findings:** Unchecked Quine and Tree Search attacks achieve $100\%$ swarm infection ($R_0 = 3.00$). Stateless single-turn filters fail against Quines ($R_0 = 2.33$). The layered System-1/System-2 defense achieves provable containment ($R_t \equiv 0.00$) with zero secondary infections and zero invariant violations.

2. [**System-1 Ingress Triaging Overfitting Post-Mortem, Remediation, and Empirical Benchmark Findings**](file:///home/student-14/capstone/docs/05-reports/system1_overfitting_and_remediation_findings_report.md)
   * **Date:** October 29, 2026
   * **Focus:** Root-cause investigation into 100% train-to-test data leakage in synthetic trajectory datasets, remediation via Stratified Group-Disjoint partitioning and developer hard negatives, and GB10 GPU empirical validation of ModernBERT and Qwen2.5-1.5B LoRA models.

---

## Weekly Status Reports

* [`weekly/`](file:///home/student-14/capstone/docs/05-reports/weekly/): Weekly progress logs, submission documents, and milestone deliverables for Phase-I evaluation reviews.
