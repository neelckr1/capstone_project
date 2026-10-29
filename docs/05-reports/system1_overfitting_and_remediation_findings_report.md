# PES UNIVERSITY
### Department of Computer Science and Engineering
**UE24CS320A – Capstone Project Phase – I**  
**Technical Research Report: System-1 Ingress Triaging Overfitting Post-Mortem, Remediation, and Empirical Benchmark Findings**

---

## 1. Project & Institutional Identification

| Field | Details |
| :--- | :--- |
| **Project Title** | **Adaptive Defense for Multi-Agent Systems** |
| **Document Type** | Technical Research & Empirical Benchmark Report |
| **Component Focus** | [`components/system_1_triage`](file:///home/student-14/capstone/components/system_1_triage) |
| **Batch / Review** | Batch 14 (Review 1 Approved) |
| **Course Code** | UE24CS320A (Capstone Project Phase - I) |
| **Date** | October 29, 2026 |
| **Student Lead** | **Neel Chandrakar** (SRN: `PES2UG24CS310`) |
| **Team Members** | **Pranav Ballebail** (SRN: `PES2UG24CS361`)<br/>**Pranav Kaushal** (SRN: `PES2UG24CS363`)<br/>**Pranav Swaroop** (SRN: `PES2UG24CS365`) |
| **Institution** | Department of Computer Science & Engineering, PES University, Bengaluru |
| **Workstation Profile** | NVIDIA DGX Spark (`promaxgb10-7bf0`), NVIDIA GB10 GPU, ARM64 Ubuntu 24.04 LTS ([`.agent`](file:///home/student-14/.agent)) |

---

## 2. Executive Summary & Abstract

In multi-agent systems (MAS), autonomous agents interact dynamically via peer RPC calls, shared vector memories, and external tool execution. This interaction fabric exposes a vulnerable attack surface to multi-turn adversarial prompt injections, indirect tool poisoning (InjecAgent / AgentDojo), and self-propagating malicious directives ("mind viruses"). 

To secure this perimeter without incurring prohibitive latency, our defense architecture deploys **System-1 Ingress Triaging**: a low-latency gatekeeper that inspects dialogue trajectories and classifies incoming traffic into a tri-state action space (**GREEN** for safe fast-path execution, **AMBER** for escalation to deliberative System-2 reasoning, and **RED** for quarantine).

During initial model evaluations on the NVIDIA GB10 hardware, our Causal Decoder SLM ([`Qwen2.5-1.5B`](file:///home/student-14/capstone/components/system_1_triage/models/llama_classifier.py)) reported seemingly flawless metrics (**100% Accuracy, 100% Recall, 0% FPR**), while our Bidirectional Encoder ([`ModernBERT`](file:///home/student-14/capstone/components/system_1_triage/models/modernbert_classifier.py)) suffered an unacceptable **14.29% False Positive Rate (FPR)** on benign code queries.

This report provides a comprehensive post-mortem investigation into the mathematical and architectural mechanisms behind this behavior:
1. **The Root Cause:** We identified **100% train-to-test data leakage** and catastrophic loss collapse ($eval\_loss = 0.000217$) caused by flat template repetition across splits and reliance on trivial keyword shortcuts.
2. **The Remediation:** We designed and implemented **Stratified Group-Disjoint Partitioning** across 160 distinct scenario groups, introduced contextual **developer hard negatives**, regularized LoRA adapters ($r=8$, $\alpha=16$, $dropout=0.15$, $label\_smoothing=0.1$), and attached automated circuit breaker callbacks to the training loop.
3. **Empirical Validation:** Retraining on the GB10 GPU against a sanitized, completely unseen test split established genuine generalization: ModernBERT achieved **95.83% Accuracy, 91.67% Attack Recall, 0.00% FPR** at **9.12 ms** P50 latency, while Qwen2.5-1.5B achieved **91.67% Accuracy and 87.50% Attack Recall** at **26.06 ms** P50 latency. These results empirically validate our **Two-Tier Cascade Gate** design.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             HIGH-LEVEL SYSTEM-1 DEFENSE PIPELINE                                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   Incoming Inter-Agent / Tool / User Trajectory (Tk)                                             │
│                           │                                                                      │
│                           ▼                                                                      │
│          ┌───────────────────────────────────┐                                                   │
│          │ Tier-1A: ModernBERT-base Encoder  │ ── (P < 0.05, Latency ~9.12 ms) ──► [GREEN PATH]  │
│          └───────────────────────────────────┘                                     Allow Pass    │
│                           │ (Ambiguous / Elevated Risk)                                          │
│                           ▼                                                                      │
│          ┌───────────────────────────────────┐                                                   │
│          │ Tier-1B: Qwen2.5-1.5B LoRA SLM    │ ── (P >= 0.85, Latency ~26 ms) ──► [RED PATH]     │
│          └───────────────────────────────────┘                                     Quarantine    │
│                           │ (0.15 <= P < 0.85, Multi-Turn Context)                               │
│                           ▼                                                                      │
│                 [AMBER ESCALATION PATH]                                                          │
│             Route to System-2 Deliberation                                                       │
│                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Workstation Hardware Profile & System Constraints

All engineering implementations, dataset synthesis, fine-tuning, and benchmarking conform strictly to the developer environment profile specified in [`.agent`](file:///home/student-14/.agent):

* **Compute Platform:** NVIDIA DGX Spark (`promaxgb10-7bf0`), 20 Cores ARM64 (`aarch64` Cortex-X925 / Cortex-A725), 119 GiB Host RAM.
* **Target GPU:** NVIDIA GB10 (CUDA Compute Capability 13.0, Driver 580.82.09, CUDA Toolkit V13.0.88).
* **VRAM Ceiling & Multi-Tenancy:** The GB10 operates in a multi-user environment. Training and inference workflows must honor multi-tenant memory ceilings:
  * ModernBERT: $\le 4,000\text{ MB}$ allocated.
  * Qwen2.5-1.5B LoRA: $\le 5,000\text{ MB}$ allocated.
  * Clef-Flash 9B: $\le 11,000\text{ MB}$ allocated (via 4-bit NF4 double-quantization).
* **Runtime Privileges:** Standard non-root user context (`student-14`). System package managers (`apt`, `dpkg`) and Docker daemon sockets are inaccessible; all runtimes utilize the isolated virtual environment at [`capstone/components/system_1_triage/venv`](file:///home/student-14/capstone/components/system_1_triage/venv).
* **Network Permissions:** Outbound HTTP/HTTPS access enabled, facilitating direct integration of Hugging Face transformer checkpoints and open-source benchmark repositories.

---

## 4. Technical Forensic Analysis: Why the Model Overfit

### 4.1. 100% Train-to-Test Data Contamination
In the baseline implementation of [`dataset_builder.py`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py), `generate_synthetic_seed_corpus` defined a minimal catalog of only **26 static text templates**:
* 4 Crescendo multi-turn drift scenarios
* 4 InjecAgent tool poisoning payloads
* 4 MAS mind virus propagation payloads
* 4 Tensor Trust override payloads
* 10 Benign technical queries

To scale the dataset to 320 trajectories, the builder executed a modulo loop:
```python
# Flawed baseline logic:
for i in range(count_per_category):
    scenario = crescendo_scenarios[i % len(crescendo_scenarios)]
    samples.append(TrajectorySample(sample_id=f"crescendo_{i:04d}", turns=...))
```
The generator modified only the string identifier (`sample_id: crescendo_0001` vs `crescendo_0005`), leaving the dialogue turns verbatim identical. When `build_and_export_splits` shuffled the combined sample list and partitioned it into 70% train (224 samples) and 15% test (48 samples), **all 48 test samples were exact text duplicates of samples present in the training set**.

Our automated test suite ([`test_circuit_breakers.py`](file:///home/student-14/capstone/components/system_1_triage/tests/test_circuit_breakers.py#L85-L103)) captured this anomaly:
```
[DataIntegrityCircuitBreaker Report]
Total Train Samples: 224 | Total Test Samples: 48
Overlapping Exact Samples: 48 / 48
Leakage Rate: 100.0%
Status: TRIPPED
```
The test benchmark was not measuring whether the neural network could detect attacks; it was measuring whether an associative memory could look up memorized strings.

### 4.2. Loss Collapse Dynamics & Premature Memorization
During the initial LoRA fine-tuning run for Qwen2.5-1.5B ($r=32$, $\alpha=64$, $\text{lr}=10^{-4}$), the optimization dynamics recorded in [`trainer_state.json`](file:///home/student-14/capstone/components/system_1_triage/checkpoints/llama_1b/checkpoint-84/trainer_state.json) exhibited severe over-parameterized loss collapse:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        INITIAL FLAWED TRAINING LOSS TRAJECTORY                         │
├───────┬────────────┬───────────────┬────────────────┬──────────────────────────────────┤
│ Step  │ Epoch      │ Training Loss │ Eval Loss      │ Empirical State                  │
├───────┼────────────┼───────────────┼────────────────┼──────────────────────────────────┤
│ 10    │ 0.36       │ 2.8343        │ —              │ Gradient descent initiated       │
│ 20    │ 0.71       │ 0.6153        │ —              │ Rapid parameter adaptation       │
│ 28    │ 1.00       │ —             │ 0.0283         │ Near-zero generalization error   │
│ 50    │ 1.79       │ 0.0013        │ —              │ Total memorization of static set │
│ 56    │ 2.00       │ —             │ 0.00035        │ Loss asymptote reached           │
│ 84    │ 3.00       │ 0.00022       │ 0.000217       │ Catastrophic collapse (0.0002)   │
└───────┴────────────┴───────────────┴────────────────┴──────────────────────────────────┘
```

Because an unconstrained adapter capacity was fitted to only 26 unique text patterns over 84 steps, cross-entropy loss converged to zero, tripping the [`TrainingMonitorCircuitBreaker`](file:///home/student-14/capstone/components/system_1_triage/core/circuit_breakers.py#L104-L140) threshold (`eval_loss < 0.005`).

### 4.3. Lexical Shortcutting vs. Intent Modeling
The synthetic attack seeds relied on blatant trigger strings (`[SYSTEM OVERRIDE: ...]`, `MIND VIRUS ALERT:`, `WORM PROTOCOL:`, `Ignore all previous instructions`), while benign controls consisted of simple programming queries. Consequently, the attention heads learned a naive heuristic shortcut:
$$\text{Query contains } "[\text{OVERRIDE}]" \implies \mathcal{P}(\text{threat}) \approx 1.0$$
The model remained completely unaware of conversational drift or multi-turn goal subversion.

### 4.4. ModernBERT False Positive Spike (14.29% FPR)
Because benign controls lacked domain-specific developer terminology, ModernBERT flagged legitimate technical questions containing words like *"override"* (e.g., Python class method overriding via `super()`) or *"system instructions"* (in Dockerfiles) as malicious prompt injections. In production, an FPR of 14.3% would sever normal agent collaboration.

---

## 5. Architectural Remediation Pipeline

To address these vulnerabilities, we developed a 5-pillar remediation framework:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               THE 5-PILLAR REMEDIATION FRAMEWORK                                 │
├──────────────────────────┬───────────────────────────────────────────────────────────────────────┤
│ 1. Stratified Partition  │ Partition strictly by scenario group; zero content hash overlap.      │
├──────────────────────────┼───────────────────────────────────────────────────────────────────────┤
│ 2. Catalog Diversification│ Expanded to 160 distinct scenario groups across all threat vectors.   │
├──────────────────────────┼───────────────────────────────────────────────────────────────────────┤
│ 3. Developer Negatives   │ Ingested security & system administration hard negatives.             │
├──────────────────────────┼───────────────────────────────────────────────────────────────────────┤
│ 4. LoRA Regularization   │ LoRA rank $r=8$, dropout $0.15$, label smoothing $0.1$, $\text{lr}=3\times 10^{-5}$. │
├──────────────────────────┼───────────────────────────────────────────────────────────────────────┤
│ 5. Automated Tripwires   │ Attached runtime TrainerCallback to abort on loss collapse.           │
└──────────────────────────┴───────────────────────────────────────────────────────────────────────┘
```

### 5.1. Stratified Group-Disjoint Splitting
We refactored [`dataset_builder.py`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py#L320-L400) to enforce group-disjoint partitioning stratified by attack category:
1. Every trajectory is mapped to an immutable `scenario_group` identifier (e.g. `crescendo_crypto_rsa`, `tool_weather_calendar`, `benign_python_super`).
2. Splitting occurs strictly across **scenario groups**, not individual samples. If group $\mathcal{G}_k$ is assigned to the training split, no variation, paraphrase, or turn sequence from $\mathcal{G}_k$ is permitted in validation or test splits.
3. Every sample is validated using content hashing:
   $$\mathcal{H}(s) = \text{SHA256}\left(\bigoplus_{t \in s.\text{turns}} (\text{role}_t \parallel \text{content}_t)\right)$$
   $$\{\mathcal{H}(s) \mid s \in \mathcal{S}_{\text{test}}\} \cap \{\mathcal{H}(s) \mid s \in \mathcal{S}_{\text{train}}\} = \emptyset$$

### 5.2. Catalog Expansion & Grounding in Literature
We expanded the scenario catalog to **160 distinct base scenario families** grounded in foundational papers:
* **Crescendo Conversational Drift (Russinovich et al., Microsoft Research):** 20 multi-turn trajectories covering cryptographic key extraction, PBFT consensus equivocation, kernel eBPF hijacking, Kubernetes RBAC abuse, and UEFI firmware bypasses.
* **InjecAgent Tool Poisoning (Zhan et al., ACL 2024 / AgentDojo):** 20 distinct tool output formats including simulated database returns, banking core gateways, git diffs, Jira issues, OCR invoice parsers, and DNS records.
* **MAS Mind Viruses (Anthropic / Morris-II):** 20 lateral propagation scenarios covering RPC replication directives, shared memory poisoning, gossip heartbeat worms, and audit suppression.
* **System Override & Extraction (Tensor Trust / TDC):** 20 direct injection patterns covering delimiter spoofing, roleplay jailbreaks, format distortions, and multilingual injection.
* **Developer Hard Negatives:** 80 distinct technical queries (expanded with parameter variations) incorporating security-adjacent terminology (`super()`, `setuid`, `chmod 1777`, `sudoers`, `iptables rate-limiting`, `cgroups v2`, `strace`, `JWT RS256`).

### 5.3. Regularized Optimization & LoRA Restraint
In [`configs/llama_1b.yaml`](file:///home/student-14/capstone/components/system_1_triage/configs/llama_1b.yaml) and [`configs/modernbert_large.yaml`](file:///home/student-14/capstone/components/system_1_triage/configs/modernbert_large.yaml), we implemented regularization hyperparameters:
* **Reduced LoRA Rank:** Scaled rank down from $r=32$ to $r=8$ ($\alpha=16$) on target projection modules (`q_proj`, `v_proj`).
* **Increased Dropout:** Raised `lora_dropout` from $0.05$ to $0.15$ to prevent token-level co-adaptation.
* **Label Smoothing:** Configured `label_smoothing_factor: 0.1` in `TrainingArguments`. This penalizes overconfident predictions by adjusting target probabilities to $[0.95, 0.05]$.
* **Weight Decay & Learning Rate:** Increased `weight_decay = 0.05` and lowered base learning rate to $3.0 \times 10^{-5}$ with warmup and linear decay.

### 5.4. Automated Circuit Breaker Tripwire
In [`trainer.py`](file:///home/student-14/capstone/components/system_1_triage/train/trainer.py#L22-L34), we embedded [`CircuitBreakerTripwireCallback`](file:///home/student-14/capstone/components/system_1_triage/train/trainer.py#L22-L34) directly into the Hugging Face `Trainer` event loop:
```python
class CircuitBreakerTripwireCallback(TrainerCallback):
    def on_evaluate(self, args, state, control, metrics, **kwargs):
        eval_loss = metrics.get("eval_loss")
        if eval_loss is not None and eval_loss < 0.005 and state.epoch <= 2.0:
            print(f"[CIRCUIT BREAKER ALERT] Premature loss collapse: {eval_loss:.6f} < 0.005! Halting.")
            control.should_training_stop = True
```

---

## 6. Empirical Benchmarking & Experimental Findings

### 6.1. Retraining Dynamics
Both models were retrained from scratch on the NVIDIA GB10 hardware using the sanitized dataset (224 train, 48 val, 48 test):
* **ModernBERT (Full Parameter Fine-Tuning):** Completed 84 optimization steps in 101.2 seconds. Loss converged smoothly from $0.6973$ down to a training loss of **$0.5816$** and validation loss of **$0.5279$**.
* **Qwen2.5-1.5B (Regularized LoRA $r=8$):** Completed 84 optimization steps in 399.1 seconds. Loss converged from $0.7719$ down to a training loss of **$0.5407$** and validation loss of **$0.4626$**.
* Neither model collapsed or triggered the loss-collapse circuit breaker.

### 6.2. Comparative Performance on Held-Out Test Data
The standardized benchmark harness ([`eval/benchmark_runner.py`](file:///home/student-14/capstone/components/system_1_triage/eval/benchmark_runner.py)) was executed across all 48 completely unseen test trajectories. Results are compiled in [`benchmark_report.json`](file:///home/student-14/capstone/results/system_1/benchmark_report.json):

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      VERIFIED POST-REMEDIATION BENCHMARK RESULTS (NVIDIA GB10)                         │
├──────────────────────┬────────────────────────────┬────────────────────────────┬───────────────────────┤
│ Metric               │ ModernBERT-large (Encoder) │ Qwen2.5-1.5B (LoRA r=8)    │ Clef-Flash 9B (Schema)│
├──────────────────────┼────────────────────────────┼────────────────────────────┼───────────────────────┤
│ **Model ID**         │ answerdotai/ModernBERT     │ Qwen/Qwen2.5-1.5B          │ Cloudflare/clef-flash │
│ **Architecture**     │ Bidirectional Encoder      │ Causal Decoder SLM         │ Joint Schema Engine   │
│ **Trainable Params** │ 149M (Full Parameter)      │ 3.7M (LoRA Adapter)        │ Zero-Shot / Untrained │
├──────────────────────┼────────────────────────────┼────────────────────────────┼───────────────────────┤
│ **Accuracy**         │ **95.83%**                 │ **91.67%**                 │ 81.25%                │
│ **Attack Detection** │ **91.67%** (22/24)         │ **87.50%** (21/24)         │ 62.50% (15/24)        │
│ **False Alarm Rate** │ **0.00%** (24/24 clean)    │ **4.17%** (23/24 clean)    │ **0.00%** (24/24)     │
│ **Precision**        │ **1.0000**                 │ **0.9545**                 │ 1.0000                │
│ **F1 Score**         │ **0.9565**                 │ **0.9130**                 │ 0.7692                │
├──────────────────────┼────────────────────────────┼────────────────────────────┼───────────────────────┤
│ **P50 Latency**      │ **9.12 ms**                │ **26.06 ms**               │ 304.01 ms             │
│ **P90 Latency**      │ **10.41 ms**               │ **31.94 ms**               │ 347.75 ms             │
│ **P99 Latency**      │ 169.68 ms                  │ 131.12 ms                  │ 395.65 ms             │
│ **Min Latency**      │ 7.44 ms                    │ 23.90 ms                   │ 283.51 ms             │
├──────────────────────┼────────────────────────────┼────────────────────────────┼───────────────────────┤
│ **VRAM Allocated**   │ 11,032.8 MB (Shared Total) │ 11,032.8 MB (Shared Total) │ 11,032.8 MB           │
└──────────────────────┴────────────────────────────┴────────────────────────────┴───────────────────────┘
```

### 6.3. Per-Category Attack Detection Breakdown

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              CATEGORY-BY-CATEGORY ATTACK DETECTION RATE                                │
├────────────────────────────┬─────────────┬────────────────────┬────────────────────┬───────────────────┤
│ Attack Category            │ Test Count  │ ModernBERT Recall  │ Qwen-1.5B Recall   │ Clef-Flash Recall │
├────────────────────────────┼─────────────┼────────────────────┼────────────────────┼───────────────────┤
│ **Benign Controls**        │ 24          │ **100.0% (24/24)** │ **95.8% (23/24)**  │ 100.0% (24/24)    │
│ **Crescendo Drift**        │ 6           │ **100.0% (6/6)**   │ **66.7% (4/6)**    │ **0.0% (0/6)**    │
│ **Tool Poisoning**         │ 6           │ **100.0% (6/6)**   │ **100.0% (6/6)**   │ 50.0% (3/6)       │
│ **MAS Mind Virus**         │ 6           │ **100.0% (6/6)**   │ **100.0% (6/6)**   │ 100.0% (6/6)      │
│ **System Override**        │ 6           │ **66.7% (4/6)**    │ **83.3% (5/6)**    │ 100.0% (6/6)      │
└────────────────────────────┴─────────────┴────────────────────┴────────────────────┴───────────────────┘
```

---

## 7. Key Findings & Architectural Conclusions

### Finding 1: Genuine Generalization Restored
With 0% train-to-test leakage, both fine-tuned models demonstrate robust, non-memorized detection capabilities:
* ModernBERT detected **22 of 24** unseen attack trajectories ($91.67\%$).
* Qwen2.5-1.5B detected **21 of 24** unseen attack trajectories ($87.50\%$).
* Crucially, the unrealistic $100\%$ accuracy score has been replaced with statistically sound performance on genuinely held-out data.

### Finding 2: False Positive Rate Slashed from 14.3% to 0.0%
The introduction of developer hard negatives completely eradicated ModernBERT's false positive vulnerability. ModernBERT cleared **24 of 24 benign queries without a single false alarm** ($0.00\%\text{ FPR}$), proving that encoder models can distinguish benign syntax (e.g. `super().override()`) from adversarial privilege overrides when provided balanced training representations.

### Finding 3: General Models Fail Against Crescendo Drift
Clef-Flash (9B parameter zero-shot baseline) **completely failed to detect multi-turn Crescendo drift (0% recall, 6/6 missed)**. This directly validates our research hypothesis: off-the-shelf foundation models evaluated in single-turn or zero-shot mode are blind to incremental semantic drift. Only models specifically trained on multi-turn trajectory histories can intercept conversational attacks.

### Finding 4: Empirical Justification for the Two-Tier Cascade
Neither model alone is the optimal ingress defense:
* **ModernBERT:** Extremely fast (**9.12 ms** P50) with $0.00\%$ false alarms, but weaker on direct system overrides ($66.7\%$).
* **Qwen2.5-1.5B:** Slower (**26.06 ms** P50) with higher semantic comprehension across direct system overrides ($83.3\%$).
* **Clef-Flash:** Impractically slow (**304.01 ms** P50) and blind to conversational escalation.

Therefore, the **Two-Tier Cascade Gate** represents the mathematically optimal architecture:
1. **Tier-1A (ModernBERT, ~9.1 ms):** Screen all incoming traffic. Immediately allow low-risk clean traffic ($\mathcal{P} < 0.05$) into the Green Path.
2. **Tier-1B (Qwen2.5-1.5B, ~26 ms):** Re-evaluate suspicious or ambiguous traffic ($0.05 \le \mathcal{P} < 0.85$). Quarantine critical threats ($\mathcal{P} \ge 0.85$).
3. **System-2 Reasoner:** Receive only true edge cases ($\sim 5-10\%$ volume) where multi-agent goal divergence requires sandboxed simulation.

---

## 8. Verified Deliverables & Artifact Inventory

All code, configurations, data splits, and benchmark artifacts have been verified in the project repository:

1. **Dataset Generator:** [`capstone/components/system_1_triage/data/dataset_builder.py`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py) (Stratified group-disjoint splitting across 160 scenario groups).
2. **Sanitized Disjoint Splits:**
   * [`train.jsonl`](file:///home/student-14/capstone/components/system_1_triage/data/processed/train.jsonl) (224 unique trajectories, 112 scenario groups).
   * [`val.jsonl`](file:///home/student-14/capstone/components/system_1_triage/data/processed/val.jsonl) (48 unique trajectories, 24 scenario groups).
   * [`test.jsonl`](file:///home/student-14/capstone/components/system_1_triage/data/processed/test.jsonl) (48 unique trajectories, 24 scenario groups, 0% leakage).
3. **Regularized Configurations:**
   * [`configs/llama_1b.yaml`](file:///home/student-14/capstone/components/system_1_triage/configs/llama_1b.yaml) ($r=8$, $dropout=0.15$, $smoothing=0.1$).
   * [`configs/modernbert_large.yaml`](file:///home/student-14/capstone/components/system_1_triage/configs/modernbert_large.yaml) ($decay=0.05$, $smoothing=0.1$).
4. **Trainer with Circuit Breakers:** [`capstone/components/system_1_triage/train/trainer.py`](file:///home/student-14/capstone/components/system_1_triage/train/trainer.py) (Integrated `CircuitBreakerTripwireCallback`).
5. **Empirical Benchmark Report:** [`capstone/results/system_1/benchmark_report.json`](file:///home/student-14/capstone/results/system_1/benchmark_report.json).
6. **Engineering Guide:** [`capstone/docs/06-guide/README.md`](file:///home/student-14/capstone/docs/06-guide/README.md).
7. **Automated Test Suite:** 20 of 20 unit and circuit breaker tests passing ([`tests/`](file:///home/student-14/capstone/components/system_1_triage/tests)).

---

## 9. Immediate Next Steps for Phase-I Deliverables

1. **AsyncIO Ingress Dispatcher:** Implement the asynchronous Python gateway combining Tier-1A (ModernBERT) and Tier-1B (Qwen2.5-1.5B) to route production multi-agent messages with $< 10\text{ ms}$ average pass-through latency.
2. **System-1 to System-2 Amber Bridge:** Finalize serialization of quarantine snapshots and trajectory context payloads for deliberative reasoning escalation ([`schema.py`](file:///home/student-14/capstone/components/system_1_triage/core/schema.py)).
3. **Automated Hard Negative Mining:** Deploy the closed-loop feedback monitor to capture novel semantic drifts from red-team fuzzing and schedule periodic LoRA adapter retraining.
