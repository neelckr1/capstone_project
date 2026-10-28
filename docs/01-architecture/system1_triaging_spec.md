# System-1 Architecture & Threat Modeling Specification

## 1. Executive Summary

This document specifies the engineering architecture for the **System-1 Ingress Triaging Layer** within the *Adaptive Defense for Multi-Agent Systems* capstone project. 

The primary purpose of System-1 is to act as a high-speed, non-autoregressive gatekeeper positioned at the perimeter of an autonomous multi-agent swarm. It intercepts all incoming user requests, inter-agent peer messages, and tool output payloads to detect advanced prompt injections before they can trigger malicious tool execution or propagate lateral "mind viruses."

---

## 2. Threat Modeling & Paper Grounding

Traditional LLM safety guardrails (such as Llama Guard) treat each user prompt as an isolated, single-turn event. This model fails completely against state-of-the-art multi-turn and agentic attacks:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          ADVANCED THREAT VECTORS TARGETED                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Conversational Semantic Drift (Crescendo Attack)                                    │
│    Reference: Russinovich, Salem, Eldan (Microsoft Research, USENIX Security 2024)    │
│    Mechanism: Attacks start benignly, escalate across turns, and backtrack on refusal. │
│    Defense Invariant: Ingest rolling multi-turn trajectories to detect intent drift.   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Indirect Tool-Return Poisoning (InjecAgent & AgentDojo)                             │
│    Reference: Zhan et al. (ACL 2024) / Debenedetti et al. (NeurIPS 2024)               │
│    Mechanism: Malicious instructions embedded in retrieved web pages, SQL, or emails. │
│    Defense Invariant: Privilege-separated token framing ([TOOL_RETURN_k]).             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Self-Replicating Mind Viruses & Prompt Infection                                   │
│    Reference: Papadopoulos et al. (Anthropic 2024) / Lee & Tiwari (arXiv:2410.07283)  │
│    Mechanism: Coerces an agent to replicate directives into outgoing peer RPC calls.  │
│    Defense Invariant: Categorical head detecting lateral infection directives (R0).    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 4. System Override & Prompt Extraction                                                 │
│    Reference: Tensor Trust (NeurIPS TDC 2023) / HackAPrompt (EMNLP 2023)               │
│    Mechanism: Delimiter spoofing (<|im_start|>) and system prompt extraction queries.  │
│    Defense Invariant: Direct binary classifier detecting prompt exfiltration signals.  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Mathematical Formulation of the Tri-State Triaging Gate

Given an inter-agent interaction trajectory $\mathcal{T}_k$:
$$\mathcal{T}_k = \left( \mathcal{S}_{\text{spec}}, (u_1, a_1), (u_2, a_2), \dots, (u_k, a_k), \mathcal{O}_{\text{tool}} \right)$$

The System-1 model computes a single forward pass:
$$\mathbf{z} = f_{\theta}(\mathcal{T}_k) \in \mathbb{R}^C$$
$$\mathcal{P}(\text{threat} \mid \mathcal{T}_k) = \sigma(\mathbf{z}_{\text{binary}})$$

The decision gate routes traffic across three distinct operational paths:

```
                       P(threat | Trajectory)
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
      P < 0.15          0.15 <= P < 0.85          P >= 0.85
    [ GREEN PATH ]       [ AMBER PATH ]         [ RED PATH ]
          │                     │                     │
          ▼                     ▼                     ▼
     Allow Fast             Escalate to           Drop Message
     MAS Execution          System-2 LLM          & Quarantine
     (~10-25ms)             Reasoner              Agent Node
```

* **GREEN PATH ($\mathcal{P} < 0.15$):** Low-risk or nominal interaction. The message passes through directly to the destination agent without invoking heavy foundation models, preserving sub-25ms swarm responsiveness.
* **AMBER PATH ($0.15 \le \mathcal{P} < 0.85$):** Ambiguous or semantic drift detected. Communication is temporarily paused and routed to the **System-2 Deliberative Reasoner** for multi-step trajectory auditing and goal-invariant verification.
* **RED PATH ($\mathcal{P} \ge 0.85$):** High-confidence adversarial injection or viral replication directive. The payload is dropped immediately, the sending agent is quarantined in an isolated sandbox, and an alert is dispatched to human supervisors.

---

## 4. Hardware Sizing & Multi-Tenant Feasibility on NVIDIA GB10

The underlying hardware is an **NVIDIA GB10 (Grace Blackwell Architecture, CUDA 13.0, 119.6 GiB Unified Memory, ARM64 Cortex-X925)**.

* **Unified Memory Dynamic:** CPU and GPU share the same 120 GB physical memory pool over NVLink/C2C interconnect.
  * ModernBERT-large (395M): Full fine-tuning uses **~3.5 GB VRAM**.
  * Llama-3.2-1B / Qwen-1.5B (1.54B): LoRA Rank 16 uses **~4.5 GB VRAM**.
  * Clef-Flash (9B): 4-bit NF4 QLoRA uses **~10.5 GB VRAM**.

---

## 5. Empirical Benchmark Results on NVIDIA GB10 (The Pareto Frontier)

Evaluation executed across 48 held-out multi-turn test trajectories (`eval/benchmark_runner.py`):

| Model Archetype | Parameter Count | Tuning Method | Accuracy | Recall (Attacks) | FPR (Benigns) | P50 Latency (GB10) | Active VRAM |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`ModernBERT-base`** | 149M | BF16 (FFT) | **93.75%** | **100.00%** | **14.29%** | **7.65 ms** | ~350 MB |
| **`Qwen2.5-1.5B`** | 1.54B | BF16 (LoRA r=16) | **100.00%** | **100.00%** | **0.00%** | **25.00 ms** | ~3.8 GB |
| **`Clef-Flash`** | ~9.0B | 4-bit NF4 Schema | **87.50%** | **77.78%** | **0.00%** | **299.34 ms** | ~6.5 GB |

### Crucial Research Finding:
* **`Qwen2.5-1.5B` LoRA** achieves a perfect **100.00% Accuracy and 0.00% FPR** at **25.00 ms** median latency, cleanly separating normal developer queries from adversarial injections.
* **`ModernBERT`** provides an ultra-fast **7.65 ms** frontline screening latency with **100.00% Attack Recall**, making it an ideal Tier-1A pre-filter in a two-tier cascade gate.
* **`Clef-Flash`** catches system overrides, tool poisoning, and mind viruses with 0.00% false alarms, but misses subtle conversational Crescendo drift unless explicitly trained on multi-turn dialogue histories.
