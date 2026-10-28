# Multi-Turn Prompt Injection & Advanced Adversarial Attacks: Research Findings

## 1. Executive Summary

As Large Language Models (LLMs) have evolved with stronger safety alignment (RLHF, DPO, input/output guardrails), simple single-turn adversarial prompts (e.g., direct jailbreak strings, Base64 encodings) have largely been neutralized. 

Consequently, adversarial research has pivoted toward **multi-turn attacks**, **long-context exploitation**, and **indirect agent hijacking**. These approaches bypass static safety filters by:
- Distributing intent across benign-looking conversational turns (**semantic drift**).
- Exploiting in-context learning dynamics across large context windows.
- Leveraging the model's tendency to trust its own prior generation history.

---

## 2. Core Attack Methodologies & Empirical Results

### 1. The Crescendo Attack (Conversational Semantic Drift)
* **Citation:** Mark Russinovich, Ahmed Salem, Ronen Eldan (Microsoft Research, 2024) — *USENIX Security / arXiv:2404.01833*
* **Method Used:**
  * **Adaptive Dialogue:** Starts with completely innocuous, benign queries loosely touching a historical or theoretical topic.
  * **Incremental Escalation:** Progressively nudges the model across conversational turns using the model’s *own* past responses as context.
  * **Backtracking:** If the model refuses at turn $N$, the algorithm reverts to turn $N-1$, rephrases the prompt along a milder angle, and re-escalates.
* **Empirical Results:**
  * Achieved **60%–85%+ Attack Success Rate (ASR)** across closed and open foundation models (including GPT-4, Gemini Pro, and Claude-v2).
  * Automated successfully via the *Crescendomation* tool without triggering standard perimeter safety classifiers.

---

### 2. Many-Shot Jailbreaking (MSJ — In-Context Learning Saturation)
* **Citation:** Cem Anil, Esin Durmus, Mrinank Sharma, et al. (Anthropic, 2024) — *Anthropic Technical Report*
* **Method Used:**
  * **Context Saturation:** Exploits ultra-long context windows ($128\text{k}+$ tokens) by prefixing a prompt with tens to hundreds of synthetic, faux dialogue turns showing an AI assistant answering sensitive queries.
  * **In-Context Learning (ICL) Override:** Uses the accumulated in-context demonstrations to overpower post-hoc safety fine-tuning.
* **Empirical Results:**
  * Demonstrated a clear **power-law scaling**: ASR increases monotonically as the number of dialogue shots grows (scaling from near 0% at 0 shots to over 70%–90% at 128–256 shots on Claude 2.0, GPT-4, and Gemini 1.5 Pro).

---

### 3. Tree of Attacks with Pruning (TAP) & PAIR (Automated Black-Box Refinement)
* **Citations:** 
  * TAP: Anay Mehrotra et al. (2023) — *arXiv:2312.02119*
  * PAIR: Patrick Chao et al. (2023) — *arXiv:2310.08419*
* **Method Used:**
  * **PAIR:** Uses an Attacker LLM in a feedback loop with a Target LLM to iteratively refine prompts based on whether the target accepted or refused.
  * **TAP:** Structures exploration as a **decision tree with pruning**. An evaluator LLM prunes off-topic or hard-refusal branches, focusing queries solely on high-probability paths.
* **Empirical Results:**
  * TAP achieved **over 80% ASR** on aligned models using only **10–30 queries**, outperforming brute-force and gradient-based approaches (such as GCG) with a fraction of the query budget.

---

### 4. InjecAgent: Indirect Prompt Injection in Agentic Workflows
* **Citation:** Qiusi Zeng et al. (UIUC, ACL 2024 Findings) — *arXiv:2403.02691*
* **Method Used:**
  * **Tool-Return Poisoning:** Targets autonomous ReAct-style LLM agents. Malicious payload instructions are embedded inside third-party data retrieved by tools (e.g., search results, web pages, or customer support tickets).
  * **Multi-Turn Action Chaining:** The agent executes the injected command across subsequent steps, chaining actions to read internal files, trigger API endpoints, or exfiltrate sensitive data.
* **Empirical Results:**
  * Tested on 30 LLMs across 1,054 scenarios: **GPT-4 was vulnerable 24% of the time** out of the box, escalating to **near 50% vulnerability** when enhanced with adversarial prompt wrappers.

---

### 5. Multilingual & Cross-Modal Hybrid Extensions
* **Citations:**
  * Multilingual: Yong Deng et al. (ICLR 2024) — *arXiv:2310.06474*
  * Multimodal: Eugene Bagdasaryan et al. (2023) — *arXiv:2307.10490*
* **Method Used:**
  * **Multilingual Drift:** Steering multi-turn conversations through low-resource languages (e.g., Zulu, Bengali, Hmong) where safety alignment data is scarce.
  * **Visual Prompt Injection (VPI):** Embedding typographic instructions or adversarial noise into images within multi-turn multimodal conversations.
* **Empirical Results:**
  * Multilingual pivoting routinely boosts jailbreak success by **30%–50%** over English baselines.
  * Visual injections completely bypass text-only input sanitizers because image tokens map directly into the multimodal latent space.

---

## 3. Summary Comparison Table

| Technique | Core Mechanism | Threat Vector | Typical Query Overhead | Reported ASR | Key Reference |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Crescendo** | Turn-by-turn semantic drift & refusal backtracking | Direct Multi-Turn | 5 – 15 turns | 60% – 85%+ | Russinovich et al. (2024) |
| **Many-Shot (MSJ)** | In-context demonstration saturation (ICL) | Long-Context Prompt | 1 turn (100+ dialogue shots) | 70% – 90%+ | Anil et al. (Anthropic, 2024) |
| **TAP / PAIR** | Attacker LLM + Tree search with evaluator pruning | Automated Multi-Turn | 10 – 30 queries | 80%+ | Mehrotra et al. (2023) |
| **InjecAgent** | Indirect payload execution via tool-calling loops | Indirect Agent Loop | 2 – 5 execution steps | 24% – 50% | Zeng et al. (ACL 2024) |
| **Cross-Lingual** | Transitioning dialogue into low-resource languages | Direct Multi-Turn | 1 – 3 turns | +30%–50% over English | Deng et al. (ICLR 2024) |

---

## 4. Why Multi-Turn Bypasses Defenses & What Works Against It

### Why Stateless Defenses Fail
1. **Benign Local Context:** At any single turn $t_k$, the user prompt (e.g., *"Can you elaborate on step 2 of that history?"*) contains zero adversarial tokens or toxic phrases.
2. **Context Inertia:** The LLM attends heavily to its own prior outputs, lowering its refusal activation threshold as conversation length increases.

### Effective Mitigations
* **Trajectory-Aware Guardrails:** Inspecting the full rolling conversation history ($\bigcup_{i=1}^k T_i$) rather than isolated turn-by-turn inputs.
* **Dual-Core Architecture (Privilege Separation):** Separating untrusted external data channels from system control instructions in agent execution pipelines.
* **Deliberative & Fragmented Alignment:** Pre-evaluating intermediate hidden states or checking partial output segments during generation before rendering tokens to the user.
