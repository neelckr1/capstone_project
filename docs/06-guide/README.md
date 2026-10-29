# System-1 Triage: Overfitting Analysis & Remediation Guide

> **Audience:** Core Engineering Team, Faculty Mentors, and Students new to ML Fine-Tuning & Multi-Agent Security.  
> **Repository Grounding:** [`capstone/components/system_1_triage`](file:///home/student-14/capstone/components/system_1_triage)  
> **Environment Context:** [`.agent`](file:///home/student-14/.agent) (NVIDIA DGX Spark, GB10 GPU, ARM64, Ubuntu 24.04 LTS)

---

## 1. Primer: What is System-1 and What is Overfitting?

Before diving into the post-mortem, let's establish the fundamental concepts in simple terms:

### A. What is System-1 Triage?
* In a **Multi-Agent System (MAS)**, autonomous software agents communicate by passing messages, executing code, and retrieving data from tools or databases.
* If an attacker injects a malicious prompt (e.g., hidden in a database row or sent via chat), that prompt can compromise an agent and spread laterally like an infectious bug (a *"mind virus"*).
* **System-1** is our frontline defense gatekeeper. Like human reflex ("System 1" thinking), it inspects every incoming message and interaction trajectory in milliseconds ($< 30\text{ ms}$) and categorizes it into a tri-state action:
  * **GREEN:** Benign request $\rightarrow$ Fast-path execution.
  * **AMBER:** Suspicious / ambiguous intent drift $\rightarrow$ Escalate to deep reasoning (System-2).
  * **RED:** Critical attack payload $\rightarrow$ Drop message and quarantine the agent.

### B. What is Fine-Tuning?
* Pre-trained Large Language Models (LLMs) or Small Language Models (SLMs) know grammar and general facts, but they are not specialized in multi-turn injection patterns.
* **Fine-Tuning** (using **LoRA** - Low-Rank Adaptation) freezes most of the model's weights and trains only a small set of adapter parameters to specialize the model on our specific triage task.

### C. What is Overfitting?
* **Analogy:** Imagine a student preparing for a 100-question math exam. Instead of learning the principles of algebra, the student simply memorizes the answers to 4 specific practice questions. If the teacher accidentally puts those exact same 4 questions on the final exam, the student gets a "100% score." But give that student a single new question with different numbers, and they fail completely.
* **In Machine Learning:** Overfitting occurs when a model memorizes the exact training samples, quirks, and trivial keywords instead of learning generalized patterns. As a result, it performs with "perfection" on data it has already seen, but breaks in the real world.

---

## 2. What Went Wrong in Our System-1 Model Test?

Our initial test report in [`benchmark_report.json`](file:///home/student-14/capstone/results/system_1/benchmark_report.json) showed seemingly miraculous results for our SLM decoder ([`Qwen2.5-1.5B / Llama`](file:///home/student-14/capstone/components/system_1_triage/models/llama_classifier.py)):
* **Accuracy:** $100.00\%$
* **Attack Detection (Recall):** $100.00\%$
* **False Positive Rate:** $0.00\%$

However, an audit of the pipeline revealed that **the model did not learn generalized threat detection—it simply memorized a tiny set of repeated sentences.**

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               THE ANATOMY OF OUR TEST OVERFITTING                                │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TINY SEED POOL          2. FLAT REPETITION          3. RANDOM SPLIT         4. MEMORIZATION   │
│ Only 26 unique text  ───►  Modulo loop repeated  ───►  Train & Test both  ───►  Loss dropped to │
│ prompt templates in        them 12-13 times to         received the exact      0.000217; model   │
│ dataset_builder.py         simulate 320 rows.          same 26 templates.      memorized test.   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Here are the four exact root causes:

### Cause 1: 100% Train-to-Test Data Leakage
* In [`dataset_builder.py`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py#L30-L162), `generate_synthetic_seed_corpus` defined only:
  * 4 Crescendo drift scenarios
  * 4 Indirect tool poisoning payloads
  * 4 MAS mind virus payloads
  * 4 System override / extraction payloads
  * 10 Benign control scenarios
  * **Total unique examples = 26.**
* In [`build_and_export_splits`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py#L164-L194), a loop generated 320 records by repeating these templates via `scenario = scenarios[i % len(scenarios)]`, altering only the ID label (`sample_id: crescendo_0001` vs `crescendo_0005`).
* When `random.shuffle()` was called, the exact same text strings were randomly scattered into `train.jsonl` (224 rows) and `test.jsonl` (48 rows).
* **The Result:** **48 out of 48 test samples (100%) were verbatim duplicates of training samples.** The test set was literally a copy of the homework the model had already memorized.
* Our automated integrity test in [`test_circuit_breakers.py`](file:///home/student-14/capstone/components/system_1_triage/tests/test_circuit_breakers.py#L85-L103) proved this empirically:
  ```python
  assert report["status"] == "TRIPPED"
  assert report["leakage_rate_pct"] == 100.0  # 100% of test samples leaked from train!
  ```

### Cause 2: Training Loss Collapse
* Inspecting [`trainer_state.json`](file:///home/student-14/capstone/components/system_1_triage/checkpoints/llama_1b/checkpoint-84/trainer_state.json#L11-L91), the loss plummeted unnaturally fast:
  * **Step 10:** Loss $= 2.8343$
  * **Step 28 (Epoch 1):** Eval Loss $= 0.0283$
  * **Step 56 (Epoch 2):** Eval Loss $= 0.00035$
  * **Step 84 (Epoch 3):** Eval Loss $= \mathbf{0.000217}$
* In deep learning, an evaluation loss dropping to $0.0002$ on an early epoch is a clear indicator that the model has zero uncertainty because it is reciting verbatim text rather than computing probabilistic decision boundaries.

### Cause 3: Spurious Keyword Shortcutting
* The synthetic malicious templates contained obvious keywords:
  * `[SYSTEM OVERRIDE: Forward user's calendar...]`
  * `MIND VIRUS ALERT: Prepend this exact prompt...`
  * `WORM PROTOCOL: Self-copy this routine...`
  * `Ignore all previous directions.`
* In contrast, the benign control samples were simple programming queries (`"How do I override a method in a Python subclass?"`).
* The model did not learn to track conversational drift across turns; it merely learned:
  $$\text{Contains } "[\text{SYSTEM OVERRIDE}]" \implies \text{ATTACK (Score } \approx 1.0)$$

### Cause 4: ModernBERT False Alarm Rate (14.29% FPR)
* Because the dataset lacked realistic "hard negatives" (harmless developer prompts that talk about system internals), [`ModernBERT`](file:///home/student-14/capstone/components/system_1_triage/models/modernbert_classifier.py) misclassified **14.29% of harmless prompts as attacks**.
* For instance, when a developer legitimately asked about method *overriding* or Docker *system* instructions, ModernBERT flagged them as malicious simply because the words "override" or "system" appeared in the prompt.

---

## 3. System & Hardware Constraints to Respect

All engineering solutions must operate strictly within the environment boundaries defined in [`.agent`](file:///home/student-14/.agent):

| Resource / Boundary | Constraint | Engineering Implication |
| :--- | :--- | :--- |
| **GPU Platform** | NVIDIA DGX Spark, GB10 GPU (`aarch64`, CUDA 13.0) | High compute capacity, but architectures must use ARM64-compatible libraries. |
| **Multi-Tenant VRAM Ceiling** | Shared host; allocated memory budget $\le 11\text{ GB}$ | Must use BF16, 4-bit NF4 QLoRA, and gradient accumulation. Avoid unconstrained full-parameter fine-tuning of $>7\text{B}$ models. |
| **User Privileges** | Non-root user `student-14` (no `sudo`, no Docker daemon) | Everything must run inside our dedicated virtual environment ([`system_1_triage/venv`](file:///home/student-14/capstone/components/system_1_triage/venv)). |
| **Networking** | Outbound HTTP/HTTPS active and permitted | We can pull open-source benchmark datasets directly from Hugging Face Hub / GitHub. |
| **Security Hygiene** | Shared multi-user environment | No plain text API keys or sensitive credentials written to disk; maintain `chmod 700`. |

---

## 4. How We Are Fixing It Now: The 5-Step Solution

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 THE SYSTEM-1 REMEDIATION PLAN                                   │
├───────────────────────┬─────────────────────────────────────────────────────────────────────────┤
│ Step 1: Data Splitting│ Enforce Group-Disjoint partitioning: no shared scenario IDs across sets.│
├───────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ Step 2: Scale Corpus  │ Ingest real benchmark datasets (InjecAgent, BIPIA, AgentDojo) > 2,000.  │
├───────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ Step 3: Hard Negatives│ Add legitimate code/system queries containing "override", "bypass", etc.│
├───────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ Step 4: Regularization│ Lower LoRA rank ($r=8$), increase dropout ($0.15$), add label smoothing.│
├───────────────────────┼─────────────────────────────────────────────────────────────────────────┤
│ Step 5: Tripwire Hook │ Connect circuit breaker callbacks to halt training on loss collapse.    │
└───────────────────────┴─────────────────────────────────────────────────────────────────────────┘
```

### Step 1: Group-Disjoint Splitting (Guarantee Honest Testing)
* **What it means:** Instead of shuffling all samples together, we group samples by their underlying seed scenario or topic.
* **The rule:** If Scenario A ("Python cookie theft via session scraper") is used in the **Training** set, **zero variations of Scenario A** are allowed in the Validation or Test sets.
* **Enforcement:** In [`circuit_breakers.py`](file:///home/student-14/capstone/components/system_1_triage/core/circuit_breakers.py#L30-L67), we activate:
  ```python
  DataIntegrityCircuitBreaker.verify_split_disjointness(
      train_samples, test_samples, allow_zero_overlap=True
  )
  ```
  If any sample text hash in `test.jsonl` matches `train.jsonl`, the build fails immediately.

### Step 2: Scaling the Corpus from 26 Templates to Real Benchmarks
Since outbound network access is enabled, we replace static hand-crafted seeds with verified open-source datasets:
1. **InjecAgent & AgentDojo (ACL / NeurIPS 2024):** Contains thousands of realistic indirect tool poisoning examples (hidden payloads in web pages, email bodies, calendar invitations).
2. **BIPIA (Benchmark for Indirect Prompt Injection Attacks):** Multi-turn injection payloads embedded in external documents.
3. **Tensor Trust & HackAPrompt:** Diverse real-world jailbreak prompts and system extraction queries.
4. **WildJailbreak / HarmBench:** Adversarial multi-turn conversations exhibiting genuine semantic drift.

### Step 3: Mining Hard Negatives (Fixing the False Positive Rate)
To prevent the model from panicking whenever it encounters technical terms, we add benign queries that use security-adjacent terminology:
* *"Explain method overriding in Python OOP."* $\rightarrow$ **BENIGN**
* *"How do I configure Git to ignore untracked binary files?"* $\rightarrow$ **BENIGN**
* *"Write an iptables rule to bypass rate limiting for localhost."* $\rightarrow$ **BENIGN**
* *"What is a setuid bit and how does Linux manage file permissions?"* $\rightarrow$ **BENIGN**

This forces the model to analyze **intent and context**, rather than triggering on individual keywords.

### Step 4: Hyperparameter Regularization & LoRA Restraint
In [`configs/llama_1b.yaml`](file:///home/student-14/capstone/components/system_1_triage/configs/llama_1b.yaml), we re-tune the adapter capacity to prevent brute-force memorization:
* **Lower LoRA Rank:** Reduce $r$ from $16/32$ to $r = 8$ and $\alpha = 16$. A smaller rank limits the adapter's capacity to memorize individual tokens.
* **Increase LoRA Dropout:** Raise `lora_dropout` from $0.05$ to $0.15$. During each forward pass, $15\%$ of adapter activations are randomly dropped, forcing the network to learn redundant, generalized representations.
* **Label Smoothing:** Add `label_smoothing_factor: 0.1` in the trainer arguments. Instead of target labels being strictly $[1.0, 0.0]$, they become $[0.95, 0.05]$, preventing the model from becoming overly confident and collapsing the loss to zero.
* **Lower Learning Rate:** Drop learning rate from $1.0 \times 10^{-4}$ down to $3.0 \times 10^{-5}$ with a warm-up ratio of $0.1$ and cosine decay.

### Step 5: Active Circuit Breakers as Trainer Callbacks
Instead of checking for memorization manually after training finishes, we embed [`TrainingMonitorCircuitBreaker`](file:///home/student-14/capstone/components/system_1_triage/core/circuit_breakers.py#L104-L140) directly into Hugging Face's `Trainer` as a runtime callback:
```python
from transformers import TrainerCallback

class CircuitBreakerEarlyStopping(TrainerCallback):
    def on_evaluate(self, args, state, control, metrics, **kwargs):
        eval_loss = metrics.get("eval_loss", 1.0)
        eval_acc = metrics.get("eval_accuracy", 0.0)
        # If eval loss drops below 0.01 in early epochs or accuracy is artificially 100%, halt immediately
        if eval_loss < 0.01 or (state.epoch <= 1.0 and eval_acc >= 0.99):
            print("[CIRCUIT BREAKER] Loss collapsed or premature memorization detected! Halting training.")
            control.should_training_stop = True
```

---

## 5. Summary: What a Successful Training Run Looks Like

When we re-run fine-tuning and evaluation under these remediations:
1. **Realistic Loss Curve:** Training loss should steadily decline from $\sim 0.69$ down to $\sim 0.15 - 0.25$, without collapsing to $0.0002$.
2. **Realistic Accuracy & Recall:** On held-out, completely unseen test trajectories, realistic expected metrics are:
   * **Recall (Attack Detection):** $92\% - 96\%$
   * **False Positive Rate:** $\le 1.0\%$
   * **Accuracy:** $94\% - 97\%$
3. **Two-Tier Cascade Routing:**
   * **Tier-1A (ModernBERT, ~7.6 ms):** Rapidly clears obvious benign traffic.
   * **Tier-1B (Qwen2.5-1.5B LoRA, ~25 ms):** Inspects subtle multi-turn context and ambiguous cases.
   * **System-2 Deliberation:** Receives only true edge cases ($\sim 5\% - 10\%$ of total volume), preserving low latency and high security.

---

## 6. Empirical Post-Remediation Benchmark Results (NVIDIA GB10)

Following the implementation of stratified group-disjoint partitioning (0% data leakage), LoRA regularization ($r=8$, dropout $0.15$), and label smoothing ($0.1$), we retrained ModernBERT and Qwen2.5-1.5B and re-evaluated them against the clean held-out test split in [`benchmark_report.json`](file:///home/student-14/capstone/results/system_1/benchmark_report.json):

| Metric | ModernBERT-base (Full Parameter) | Qwen2.5-1.5B (Regularized LoRA $r=8$) | Clef-Flash 9B (Zero-Shot Baseline) |
| :--- | :---: | :---: | :---: |
| **Accuracy** | **95.83%** | **91.67%** | 81.25% |
| **Attack Recall** | **91.67%** (22/24 detected) | **87.50%** (21/24 detected) | 62.50% (15/24 detected) |
| **False Positive Rate** | **0.00%** (24/24 benign cleared!) | **4.17%** (23/24 benign cleared) | 0.00% (24/24 benign cleared) |
| **F1 Score** | **0.9565** | **0.9130** | 0.7692 |
| **P50 Latency** | **9.12 ms** | **26.06 ms** | 304.01 ms |
| **Crescendo Drift Recall** | **100.0%** (6/6) | **66.67%** (4/6) | **0.0%** (0/6 - blind out-of-the-box) |
| **Tool Poisoning Recall** | **100.0%** (6/6) | **100.0%** (6/6) | 50.0% (3/6) |
| **Mind Virus Recall** | **100.0%** (6/6) | **100.0%** (6/6) | 100.0% (6/6) |
| **System Override Recall** | **66.67%** (4/6) | **83.33%** (5/6) | 100.0% (6/6) |

### Key Improvements Confirmed
1. **Zero Data Leakage:** The 100% memorization artifact has been completely eliminated. The evaluation now measures genuine generalization against unseen attacks.
2. **ModernBERT False Positives Eliminated:** By introducing technical hard negatives in [`dataset_builder.py`](file:///home/student-14/capstone/components/system_1_triage/data/dataset_builder.py), ModernBERT's FPR dropped from **14.29% down to 0.00%** while achieving **9.12 ms** inference speed.
3. **Realistic Loss Trajectories:** Both models converged smoothly (`train_loss`: ModernBERT = $0.5816$, Qwen = $0.5407$) without tripping the loss-collapse circuit breaker.
