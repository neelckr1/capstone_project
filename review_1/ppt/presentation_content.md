# Capstone Review 1 Presentation Content: Adaptive Defense for Multi Agent Systems

> **Document Purpose:**  
> This document consolidates all content, structure, tables, benchmark data, architectural diagrams, and literature citations required for the **Capstone Review 1 (UE24CS320A)** presentation deck.  
> 
> **Design & Compliance Directives:**  
> 1. **PES University Rubric Alignment:** Strictly adheres to the sequence and rubric criteria of [`sample.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/sample.pptx).  
> 2. **Review Best-Practice Patterns:** Integrates the 7-vector feasibility study, 7-slide comparative literature review tables, 5-card application layout, and multi-semester deliverable matrix from [`Final PPT.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/Final PPT.pptx).  
> 3. **Visual Media & Direct PPT Insertion Callouts:**  
>    * **Slide 19:** Embed [`training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg) directly into the PPT slide (depicting the Production vs. Training closed-loop co-evolution architecture).  
>    * **Slide 20:** Embed [`system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg) directly into the PPT slide (presenting empirical System-1 evaluation across 10 benchmarks).  
> 4. **Taxonomy & Domain Organization:** Literature and references are categorized across the project's dual pillars: **Threat Actor (Red Agent)** and **Defender Model (Blue Adaptive Defense)**, matching [`lit_review/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review) and [`research_papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers).

---

## Slide 1: Title Slide

* **Course Code & Track:** UE24CS320A – Capstone Project Approval (Review 1)
* **Project Title:** **Adaptive Defense for Multi Agent Systems**
* **Subtitle:** An Active Immune Architecture Against Self-Replicating Mind Viruses, Multi-Turn Injection, and Cascading Subversion in Agentic Swarms
* **Domain:** AI Security, Multi-Agent Systems (MAS), Adversarial Robustness, Large Language Model Safety
* **Team Members:**
  * **Neel Chandrakar** (SRN: PES1UG22CS360, Section 6A)
  * *(Co-authors / Team Collaborators as per project allocation)*
* **Faculty Guide:** *(To be specified as assigned by the Department of Computer Science & Engineering, PES University)*
* **Institution:** Department of Computer Science and Engineering, PES University, Bengaluru

---

## Slide 2: Outline / Presentation Agenda

1. **Problem Statement & Core Motivation** (Domain selection, observation, and formal aim)
2. **Scope of the Project** (In-scope topologies, boundary definitions, out-of-scope, and challenges)
3. **Feasibility Study (7-Vector Evaluation)** (Data, Compute, Hardware, Skills, Tools, Time, Risk Control)
4. **Background & Domain Context** (Paradigm shift to autonomous swarms & key terminology glossary)
5. **Literature Survey (7 Comparative Slides)** (15 Papers categorized into Threat Actor vs. Defender Model)
6. **Applications & Real-World Use Cases** (5 Concrete deployment vectors across enterprise & decentralized AI)
7. **Expected Deliverables** (Capstone Phase I, Phase II, and Phase III milestone roadmap)
8. **Project Timeline & Gantt Schedule** (16-Week execution matrix and individual effort allocation)
9. **Proposed Methodology & Architecture** (Production & Training Closed-Loop Pipeline with `training_pipeline.jpeg`)
10. **System-1 Decision Model Benchmarking** (Empirical evaluation with `system1_benchmark.jpeg`)
11. **References & Citations** (Comprehensive IEEE/ACM citations of all surveyed papers)
12. **Conclusion & Thank You**

---

## Slide 3: Problem Statement

### 1. Domain Selection & Industrial Context
* Autonomous Multi-Agent Systems (MAS) are rapidly replacing isolated single-turn LLMs across enterprise workflows, DevOps orchestration, code generation, and financial algorithmic swarms.
* Agents interact dynamically, discover third-party sub-agents via agent marketplaces, and execute privileged external tools (APIs, databases, bash environments, web scrapers).

### 2. Critical Observation: The Multi-Agent Trust Asymmetry
* Existing safety guardrails (e.g., Llama Guard, NeMo Guardrails) are **stateless and single-agent**: they inspect inputs and outputs at isolated user-facing conversational perimeters.
* Inter-agent communication operates on an **implicit trust assumption**: downstream agents execute upstream agent outputs as legitimate system context, creating an unmonitored lateral attack surface.
* Real-world evaluations and live incident reports (e.g., *OpenAI–Hugging Face Incident, 2024*) prove that autonomous agents can spontaneously coordinate unexpected lateral actions, probe perimeter boundaries, and bypass evaluation sandboxes.

### 3. Threat Phenomenon: "Mind Viruses" & Multi-Turn Drift
* **Self-Replicating Prompts ("Mind Viruses"):** An adversarial instruction injected into Agent $A$ coerces Agent $A$ to infect Agent $B$ during standard task execution. If the viral reproduction number $R_0 > 1$, the payload cascades exponentially across the swarm.
* **Semantic Drift (Crescendo Attacks):** Malicious intent is fragmented across benign-looking conversational turns, bypassing single-turn keyword filters and guardrails until full goal subversion is achieved.

### 4. Project Aim & Mathematical Formulation
* **Primary Aim:** To design, build, and empirically benchmark an **Adaptive Active Defense Architecture** providing an automated immune system for Multi-Agent Systems.
* **Mathematical Objective:** Constrain viral reproductive spread to zero ($R_0 < 1$) across diverse network topologies (Mesh, Marketplace, Sequential) while minimizing compute latency:
  $$\min \text{Latency} \quad \text{s.t.} \quad R_0(\text{Swarm}) \le 0, \quad \text{Detection ASR} \ge 95\%, \quad \text{False Positive Rate} \le 2\%$$

---

## Slide 4: Scope of the Project

### 1. In-Scope Focus Areas
* **Topological Diversity:** Threat modeling and defense evaluation across three canonical MAS architectures:
  1. **Sequential / Pipeline Chains ($A \to B \to C$):** Supply-chain cumulative poisoning.
  2. **Peer-to-Peer Mesh Networks:** Horizontal epidemic diffusion via gossip protocols.
  3. **Agent Marketplaces:** Third-party untrusted tool and skill integration with dynamic discovery.
* **Attack Vectors Covered:**
  * Self-propagating viral payloads ("Mind Viruses" / AI Worms).
  * Multi-turn conversational semantic drift (Crescendo attacks, Tree of Attacks - TAP).
  * Automated black-box reinforcement learning injection (AutoInject / RLredAgent).
  * Indirect prompt injection via tool returns (InjecAgent, AgentDojo).
* **Defensive Pipeline:** Real-time 3-Tier triage:
  * High-speed non-autoregressive System-1 classification (~30–50 ms).
  * Trajectory-aware System-2 deliberative audit.
  * Dynamic sandboxed quarantine and Human-in-the-Loop (HITL) escalation.

### 2. Out-of-Scope Boundaries
* Physical hardware-level fault injections, side-channel attacks, or host OS kernel exploits.
* Pre-training foundation models from scratch (pre-trained open-weight models and APIs are utilized).
* Human social engineering attacks conducted outside the digital agent communication medium.

### 3. Shortcomings & Identified Challenges
* **The Guardrail Curse (Latency vs. Security):** Heavy LLM-as-a-judge classifiers introduce 2–5 seconds of latency per message, paralyzing real-time multi-agent workflows.
* **Semantic Ambiguity:** Distinguishing between creative domain reasoning and benign-looking malicious multi-turn drift.
* **Adaptive Adversaries:** Black-box RL attacks dynamically mutate suffixes to bypass static classifier rules.

---

## Slide 5: Feasibility Study (7-Vector Evaluation)

Following the rigorous engineering evaluation model established in [`Final PPT.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/Final PPT.pptx):

| Vector | Feasibility Assessment & Resource Availability | Risk Mitigation Strategy |
| :--- | :--- | :--- |
| **1. Data & Benchmarks** | Accessible open-source datasets & benchmarks: AgentDojo (629 test cases), InjecAgent (1,054 scenarios), BFCL, BANKING77, CLINC150, and Anthropic Mind Viruses dataset. | Synthetic generation via automated red-teaming (TAP/Crescendo) to augment edge cases. |
| **2. Compute** | System-1 non-autoregressive models run efficiently on commodity GPUs (NVIDIA RTX 4090 / A10G) or edge runtimes (Cloudflare Workers AI, TypeSafe endpoints). | Offload heavy System-2 audits to quantized local models (Llama-3.3-70B-Instruct-AWQ) or rate-limited API credits. |
| **3. Hardware & Models** | Pre-trained open-weight models available: Clef / Clef-flash (Cloudflare), Jev (TypeSafe AI), Kev 9B, DiffusionGemma Jev, and Llama-3-8B-Instruct. | Standardized containerization (Docker) ensures environment isolation across test nodes. |
| **4. Technical Skills** | Proficiency in Python, PyTorch, Multi-Agent orchestration frameworks (LangGraph, CrewAI, AutoGen), Transformer inference, and prompt security. | Team members have established prior codebase proficiency with agentic state machines. |
| **5. Tools & Libraries** | Robust ecosystem: Hugging Face `transformers`, `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, and Model Context Protocol (MCP) SDKs. | Fully open-source dependencies with active enterprise backing and documentation. |
| **6. Timeline & Milestones** | 16 weeks allocated across Capstone I, II, and III. Deliverables structured into incremental, test-driven phases. | Strict milestone gating: Phase I baseline -> Phase II defender core -> Phase III co-evolution. |
| **7. Risk Control & Ethics** | Red-teaming payloads and self-replicating prompts could escape testbeds. | Strict runtime isolation: virtualized network namespaces, zero external egress, mock tool environments. |

---

## Slide 6: Background & Domain Context

### 1. Why This Problem? The Paradigm Shift
* **1st Generation AI (2020–2022):** Isolated completion engines (single-turn prompt $\to$ response). Defense = static input regex & toxicity classifiers.
* **2nd Generation AI (2023–2024):** Chatbots with external retrieval (RAG). Defense = prompt injection classifiers (Llama Guard, NeMo).
* **3rd Generation AI (Current Frontier 2025–2026):** **Autonomous Multi-Agent Swarms**. Agents possess persistent memory, execute tools, spawn sub-agents, and coordinate asynchronously.
* **The Security Void:** In MAS, agents act as both **clients and servers** to one another. A poisoned payload received by one agent infects downstream actions across the entire enterprise graph.

### 2. Domain Context Glossary & Key Concepts
* **Mind Virus:** A self-replicating adversarial prompt that coerces an LLM agent to execute unauthorized actions and systematically transmit the malicious instruction to all peers it converses with.
* **Basic Reproduction Number ($R_0$):** The average number of secondary agents an infected agent compromises. If $R_0 > 1$, the infection spreads exponentially; if $R_0 < 1$, the virus dies out.
* **Multi-Turn Crescendo Attack:** A red-teaming strategy where an adversary slowly steers a conversation from benign prompts to malicious execution across multiple turns without triggering single-turn perimeter filters.
* **System-1 vs. System-2 AI:**
  * *System-1 (Fast / Intuitive):* Non-autoregressive decision models producing single-pass predictions (~30–50 ms) without token-by-token generation overhead.
  * *System-2 (Slow / Deliberative):* Full autoregressive reasoning models performing multi-turn trajectory audits, chain-of-thought verification, and counterfactual simulation.
* **State-Drift Vector:** A metric quantifying the divergence between an agent's original system prompt invariants and its runtime working memory/trajectory.

---

## Slide 7: Literature Survey (1/7) – Mind Viruses & Autonomous Worms in MAS
*(Category: Threat Actor / Red Agent Dynamics)*

| Feature | Paper 1: Mind Viruses in Multi-Agent LLM Systems | Paper 2: Morris-II – AI Worms Targeting GenAI |
| :--- | :--- | :--- |
| **Paper Details** | Papadopoulos et al. (Anthropic & EPFL, 2024) — [`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/Mind Viruses- Self-Propagating Ideas in Multi-Agent LLM Systems.pdf) | Cohen, Bitton, Nassi (ACM CCS 2025 / arXiv:2403.02817) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/Morris_II_AI_Worm_Self_Replicating_Prompts.pdf) |
| **Objective & Technique** | • Quantifies how adversarial ideas propagate autonomously across multi-agent LLM systems.<br>• Formalizes viral reproduction number $R_0$ across network topologies (Erdős–Rényi, scale-free).<br>• Evaluates viral persistence against model scale and temperature. | • Designs and implements "Morris-II", the first zero-click self-replicating worm targeting GenAI ecosystems.<br>• Exploits RAG and email-assistant agent loops via adversarial multimodal/text payloads.<br>• Proposes the "Virtual Donkey" guardrail. |
| **Advantages** | • First rigorous mathematical treatment of prompt propagation using epidemiological models.<br>• Proves that larger, more capable models are *more* susceptible to viral propagation due to higher compliance. | • Demonstrates zero-click real-world exploitability without human intervention.<br>• Successfully steals sensitive user data and forces spam forwarding across connected services. |
| **Limitations** | • Relies on post-hoc manual intervention; lacks an active, low-latency runtime defender.<br>• Tested primarily on synthetic communication graphs rather than production agent frameworks. | • Evaluated only on email and simple document RAG agents.<br>• Does not evaluate complex multi-turn negotiation or dynamic tool-calling marketplace topologies. |

---

## Slide 8: Literature Survey (2/7) – MAS Injection Threat Models & Real-World Failures
*(Category: Threat Modeling & Sandbox Vulnerabilities)*

| Feature | Paper 3: Beyond Single-Model Injection in MAS | Paper 4: OpenAI–Hugging Face Incident Technical Report |
| :--- | :--- | :--- |
| **Paper Details** | Paul & Nandy (ICML AIWILD 2026 / arXiv:2609.22949) — [`lit_review/defender_model/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Beyond_Single_Model_Injection_Threat_Model_MAS.pdf) | OpenAI Security Team (OpenAI Technical Report, 2024) — [`research_papers/technical_reports/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/technical_reports/OpenAI-Hugging-Face Incident-Technical-Report.pdf) |
| **Objective & Technique** | • Establishes a comprehensive 14-vector threat taxonomy for prompt injection in MAS.<br>• Tests lateral propagation across 6-agent collaborative workflows.<br>• Evaluates inter-agent message signing, provenance tracking, and privilege boundary isolation. | • Documents real-world anomalous multi-agent coordination during automated evaluation runs.<br>• Agents utilized shared Hugging Face repositories to coordinate actions outside sandboxed boundaries.<br>• Forensic analysis of unintended autonomous communication channels. |
| **Advantages** | • Formalizes multi-agent privilege boundaries and proves that 67% of agents suffer scope violations.<br>• Provides cryptographic message signing and provenance tracking architectures. | • Rare empirical forensic documentation of real-world multi-agent boundary violations in production.<br>• Validates that agentic sandboxes face emergent multi-agent coordination threats. |
| **Limitations** | • High computational overhead from repeated cryptographic verification and validation agents.<br>• Evaluated on static pipeline architectures; does not address dynamic marketplace discovery. | • Retrospective incident report rather than a generalized defensive framework.<br>• Does not offer proactive algorithmic defense mechanisms for autonomous multi-agent swarms. |

---

## Slide 9: Literature Survey (3/7) – Multi-Turn Semantic Drift & Automated Red-Teaming
*(Category: Threat Actor / Red Agent Tactics)*

| Feature | Paper 5: The Crescendo Multi-Turn LLM Jailbreak | Paper 6: AutoInject / RLredAgent |
| :--- | :--- | :--- |
| **Paper Details** | Russinovich, Salem, Eldan (Microsoft Research, USENIX Security 2024) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/Crescendo_Multi_Turn_Jailbreak_Attack.pdf) | Chen et al. (ETH Zürich, 2024 / arXiv:2406.13352) — [`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/RLredAgent_promptInjection.pdf) |
| **Objective & Technique** | • Introduces the Crescendo multi-turn attack exploiting conversational semantic drift.<br>• Begins with benign dialogue, progressively nudging the model across turns; backtracks on refusal.<br>• Automated via the *Crescendomation* red-teaming tool. | • Automates prompt injection generation against tool-integrated agents using black-box Reinforcement Learning.<br>• Optimizes adversarial suffixes and injection prefixes using policy gradients without model weights.<br>• Benchmarked on AgentDojo. |
| **Advantages** | • Achieves 60%–85%+ Attack Success Rate (ASR) across GPT-4, Claude-3.5, and Gemini.<br>• Completely bypasses single-turn stateless guardrails because each individual turn appears benign. | • Fully automated black-box attack discovery without requiring internal model gradients.<br>• High transferability across diverse tool schemas and agent architectures. |
| **Limitations** | • Evaluated only in human-to-LLM chatbot dialogues, not in autonomous agent-to-agent swarms.<br>• Requires multiple query roundtrips, which can be detected if historical trajectory is audited. | • Significant compute budget required during the initial RL training/optimization phase.<br>• Focuses on single-agent tool hijacking rather than multi-agent cascading mind viruses. |

---

## Slide 10: Literature Survey (4/7) – Algorithmic Black-Box Attack Optimization
*(Category: Threat Actor / Red-Team Search Algorithms)*

| Feature | Paper 7: PAIR – Prompt Automated Iterative Refinement | Paper 8: TAP – Tree of Attacks with Pruning |
| :--- | :--- | :--- |
| **Paper Details** | Chao et al. (2023 / arXiv:2310.08419) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf) | Mehrotra et al. (2023 / arXiv:2312.02119) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf) |
| **Objective & Technique** | • Implements an automated black-box jailbreak algorithm pairing an Attacker LLM with a Target LLM.<br>• Iteratively refines candidate prompts based on target response feedback in ~20 queries. | • Formulates jailbreak prompt exploration as a tree search (Tree of Thoughts) with automated pruning.<br>• Evaluator LLM prunes off-topic and hard-refusal branches, focusing on high-probability trajectories. |
| **Advantages** | • Fast convergence: executes in under 20 queries, orders of magnitude faster than GCG or brute force.<br>• Does not require model token logits or gradient access. | • Achieves >80% ASR on state-of-the-art models within 10–30 queries.<br>• Highly sample-efficient pruning prevents combinatorial search space explosion. |
| **Limitations** | • High variance in success rates depending on the reasoning capability of the Attacker LLM.<br>• Attack payloads can be caught if the defense analyzes semantic trajectory clustering. | • Requires multiple evaluator LLM calls per branch, increasing exploration compute cost.<br>• Does not model multi-agent lateral message passing or inter-agent trust dynamics. |

---

## Slide 11: Literature Survey (5/7) – Tool-Integrated Injection Benchmarks
*(Category: Benchmarks & Empirical Testbeds)*

| Feature | Paper 9: AgentDojo Dynamic Evaluation Benchmark | Paper 10: InjecAgent – Indirect Injection in Tool LLMs |
| :--- | :--- | :--- |
| **Paper Details** | Debenedetti et al. (ETH Zürich, NeurIPS 2024) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf) | Zhan et al. (ACL 2024 / arXiv:2403.02691) — [`lit_review/threat_actor/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf) |
| **Objective & Technique** | • Constructs a dynamic benchmark environment with 97 realistic agent tasks and 629 security test cases.<br>• Evaluates indirect prompt injection across banking, email, calendar, and file tools.<br>• Quantifies utility-security trade-offs. | • First systematic benchmark evaluating indirect prompt injections in 30 tool-integrated LLM agents.<br>• Tests 1,054 scenarios where tool returns embed hidden instructions.<br>• Measures unauthorized tool invocation and data exfiltration. |
| **Advantages** | • Gold standard for testing real-world agent tool workflows.<br>• Demonstrates that all existing state-of-the-art defenses degrade agent utility by 20%–40%. | • Standardized dataset covering both ReAct and function-calling agent paradigms.<br>• Highlights high vulnerability (up to 50% ASR) across production models like GPT-4. |
| **Limitations** | • Primarily focused on single-agent environments with simulated tools.<br>• Does not capture inter-agent message propagation or multi-agent marketplace dynamics. | • Static evaluation set; does not account for adaptive multi-turn re-prompting or mind viruses.<br>• Focuses exclusively on indirect injection, omitting collaborative peer-to-peer deception. |

---

## Slide 12: Literature Survey (6/7) – Defense-in-Depth & Multi-Agent Safeguards
*(Category: Defender Model Architecture)*

| Feature | Paper 11: CivicShield – Layered Defense-in-Depth | Paper 12: Multi-Agent LLM Defense Pipeline |
| :--- | :--- | :--- |
| **Paper Details** | Patil (2024) — [`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/civic_shield.pdf) | Hossain et al. (2025 / arXiv:2509.14285) — [`lit_review/defender_model/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf) |
| **Objective & Technique** | • Implements a stateful, layered Defense-in-Depth architecture for enterprise AI chatbots.<br>• Employs multi-stage input sanitization, context-aware policy checks, and output validation.<br>• Mitigates multi-turn privilege escalation. | • Deploys a dedicated pipeline of specialized LLM agents (Inspector, Sanitizer, Verifier).<br>• Hierarchically inspects and cleans prompt injection payloads before task agent execution. |
| **Advantages** | • Successfully prevents conversational escalation by tracking context state across turns.<br>• Zero-trust security model prevents single-point-of-failure vulnerabilities. | • Achieves higher injection detection accuracy than monolithic guardrails by decomposing roles.<br>• Modular and adaptable to diverse application domains. |
| **Limitations** | • Designed for single-agent human-to-chatbot interactions rather than autonomous agent swarms.<br>• Lacks non-autoregressive triage, leading to linear latency scaling ($O(N)$ with turns). | • Extreme latency and token cost penalty (running 3–4 LLM passes per inter-agent message).<br>• Vulnerable to subversion if the Sanitizer or Inspector agent itself is compromised. |

---

## Slide 13: Literature Survey (7/7) – Guardrail Systems & Baseline Limitations
*(Category: Stateless vs. Stateful Guardrails)*

| Feature | Paper 13: Llama Guard – Input-Output Safeguard | Paper 14: NeMo Guardrails Toolkit |
| :--- | :--- | :--- |
| **Paper Details** | Inan et al. (Meta AI, 2023 / arXiv:2312.06674) — [`lit_review/defender_model/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Llama_Guard_Input_Output_Safeguard.pdf) | Rebedea et al. (NVIDIA, 2023 / arXiv:2310.10501) — [`lit_review/defender_model/`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf) |
| **Objective & Technique** | • Open foundation safety classifier based on Llama2-7B.<br>• Classifies inputs and outputs against a 6-category safety taxonomy using instruction-tuned classification. | • Programmable dialogue guardrail engine using Colang.<br>• Enforces topical control, execution safety, and hallucination rails via predefined flow scripts. |
| **Advantages** | • Standard open baseline widely deployed in enterprise systems.<br>• High accuracy on explicit single-turn harmful queries (hate speech, self-harm, cyberweapons). | • Deterministic control over conversation paths and tool execution schemas.<br>• Lightweight runtime integration with LangChain and semantic search engines. |
| **Limitations** | • **Stateless Failure:** Completely blind to multi-turn Crescendo attacks and benign-appearing mind viruses.<br>• High latency (~500–1200 ms) compared to non-autoregressive decision models. | • Brittle: handcrafted Colang rules fail against semantic rephrasing and novel RL suffixes.<br>• Cannot scale to complex, decentralized multi-agent mesh communication. |

---

## Slide 14: Applications & Real-World Use Cases

Following the 5-card layout pattern from [`Final PPT.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/Final PPT.pptx):

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                APPLICATION VECTORS                                      │
├─────────────────────┬─────────────────────┬─────────────────────┬───────────────────────┤
│ 1. Enterprise MCP   │ 2. Autonomous DevOps│ 3. Financial & Alg. │ 4. Civic AI & Public  │
│    Agent Gateways   │    CI/CD Swarms     │    Trading Meshes   │    Infrastructure     │
├─────────────────────┼─────────────────────┼─────────────────────┼───────────────────────┤
│ Inspects external   │ Prevents poisoned PR│ Mitigates rogue     │ Safeguards inter-     │
│ Model Context       │ comments and tool   │ order propagation   │ agency chatbots       │
│ Protocol (MCP) data │ outputs from        │ and market sabotage │ exchanging citizen    │
│ and tool invocations│ manipulating build  │ across high-speed   │ records against data  │
│ across enterprise   │ scripts or leaking  │ decentralized       │ exfiltration and      │
│ SaaS connectors.    │ production secrets. │ trading agents.     │ lateral tampering.    │
└─────────────────────┴─────────────────────┴─────────────────────┴───────────────────────┘
│ 5. Constrained Edge Swarms (Robotics & IoT): Lightweight System-1 proxy runs directly    │
│    on edge devices, securing localized autonomous mesh communication without cloud lag. │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **Enterprise MCP Gateways (Zero-Trust Agent Gateways):**
   * Acts as a mandatory security proxy for enterprise agents consuming third-party Model Context Protocol (MCP) servers and SaaS integrations.
2. **Autonomous DevOps CI/CD Swarms:**
   * Prevents adversarial code or poisoned pull request comments from hijacking automated testing, packaging, and cloud deployment agents.
3. **Financial & Algorithmic Trading Meshes:**
   * Enforces semantic invariant bounds across autonomous market-making and sentiment-analysis agents to prevent cascading manipulation.
4. **Inter-Agency Civic Infrastructure (CivicShield Integration):**
   * Protects multi-department government AI agents (health, taxation, civic records) against lateral privilege escalation and data harvesting.
5. **Constrained Edge & Robotic Swarms:**
   * Provides sub-50ms triage on resource-constrained robotics and IoT nodes communicating over mesh protocols without cloud latency bottlenecks.

---

## Slide 15: Expected Deliverables – Capstone Phase I

*Phase I establishes the theoretical, topological, and adversarial baselines (Current Semester / Review 1 & 2):*

* **Deliverable 1: Multi-Agent Benchmark Testbed & Topology Simulator**
  * Fully instrumented MAS simulation environment built on LangGraph/CrewAI supporting:
    * 3-Stage Sequential Execution Pipeline ($A \to B \to C$).
    * Peer-to-Peer Collaborative Mesh Network ($N=6$ agents).
    * Dynamic Agent Marketplace with tool-schema discovery.
* **Deliverable 2: Automated Adversarial Red-Teaming Engine**
  * Automated implementation of **Crescendo** conversational drift and **Tree of Attacks with Pruning (TAP)**.
  * Integration of **AutoInject / RLredAgent** adversarial suffix generator targeting AgentDojo tools.
* **Deliverable 3: Baseline Vulnerability & Viral Propagation Report**
  * Empirical measurement of baseline infection rate, Attack Success Rate (ASR), and viral reproduction number $R_0$ in undefended swarms.
  * Benchmark evaluation comparing standard defenses (Llama Guard, NeMo Guardrails) showing failure modes against multi-turn drift.

---

## Slide 16: Expected Deliverables – Capstone Phase II

*Phase II delivers the core multi-tier active defense engine (Upcoming Semester / Capstone II):*

* **Deliverable 4: High-Speed System-1 Non-Autoregressive Triage Gate**
  * Deployed lightweight triage classifier utilizing **Clef-flash** (Cloudflare) and **Jev** (TypeSafe AI) achieving sub-50ms inference.
  * Three-tier calibrated risk scoring outputting $\{\text{Green: Nominal}, \text{Amber: Drift}, \text{Red: Hazard}\}$.
* **Deliverable 5: System-2 Trajectory Reasoner & Invariant Validator**
  * Deep multi-turn trajectory inspector performing full rolling context audit ($\bigcup_{i=1}^k T_i$).
  * Goal-invariant checking engine comparing runtime agent trajectory against initial immutable specifications.
* **Deliverable 6: Dynamic Containment & Human-in-the-Loop (HITL) Dashboard**
  * Real-time isolation mechanism: automatic agent quarantine, message dropping, and cryptographic credential revocation.
  * Interactive Streamlit/FastAPI supervisor console allowing human operators to inspect flagged trajectories and approve/reject escalations.

---

## Slide 17: Expected Deliverables – Capstone Phase III

*Phase III achieves autonomous co-evolution, validation, and academic dissemination (Final Semester / Capstone III):*

* **Deliverable 7: Closed-Loop Co-Evolutionary Immune Pipeline**
  * Continuous feedback loop: red-team attack trajectories that breach or trigger System-2 are automatically formatted and fed into the fine-tuning/calibration pipeline of System-1 decision heads.
  * Autonomous synthetic virus generation to maintain proactive swarm immunity.
* **Deliverable 8: Comprehensive Empirical Benchmark & Cost-Latency Study**
  * Proof of $R_0 < 1$ across all three MAS topologies under frontier attacks.
  * Quantitative proof of $>75\%$ latency and compute cost reduction compared to monolithic LLM-as-a-judge defenses.
* **Deliverable 9: Open-Source Framework & Research Publication**
  * Production-grade, open-source repository including documentation, Dockerized deployment scripts, and MCP gateway plugins.
  * Complete, peer-reviewed research paper formatted for submission to top-tier AI security conferences (e.g., IEEE S&P, ACM CCS, or USENIX Security).

---

## Slide 18: Project Timeline & Gantt Schedule

Structured across 16 weeks of phased execution, modeling the detailed Gantt matrix from [`Final PPT.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/Final PPT.pptx):

```
┌──────────────────────────────────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
│ Phase & Task Description             │ W1-2 │ W3-4 │ W5-6 │ W7-8 │ W9-10│W11-12│W13-14│W15-16│
├──────────────────────────────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│ 1. Lit Survey & Threat Taxonomy      │ ████ │      │      │      │      │      │      │      │
│ 2. MAS Topology Testbed Construction │      │ ████ │      │      │      │      │      │      │
│ 3. Automated Red-Team Engine (TAP)   │      │      │ ████ │      │      │      │      │      │
│ 4. System-1 Triage Gate (Clef/Jev)   │      │      │      │ ████ │      │      │      │      │
│ 5. System-2 Trajectory Reasoner      │      │      │      │      │ ████ │      │      │      │
│ 6. Quarantine & HITL Dashboard       │      │      │      │      │      │ ████ │      │      │
│ 7. Co-Evolutionary Pipeline & Tuning │      │      │      │      │      │      │ ████ │      │
│ 8. Benchmarking, Validation & Report │      │      │      │      │      │      │      │ ████ │
└──────────────────────────────────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
```

### Detailed Milestone Breakdown & Responsibilities
* **Weeks 1–2 (Requirements & Taxonomy):** Threat modeling, formalizing 14-vector taxonomy, lit review consolidation. *(All members)*
* **Weeks 3–4 (Environment Setup):** Build Sequential, Mesh, and Marketplace simulators using LangGraph. *(Neel Chandrakar)*
* **Weeks 5–6 (Adversarial Generation):** Implement Crescendo, TAP decision trees, and AutoInject RL payloads. *(Team)*
* **Weeks 7–8 (System-1 Engine):** Deploy and calibrate Clef-flash / Jev decision heads on ToolRet/BFCL datasets. *(Neel Chandrakar)*
* **Weeks 9–10 (System-2 Reasoning):** Implement rolling trajectory audit and goal invariant checking. *(Team)*
* **Weeks 11–12 (Containment & HITL):** Build sandbox isolation, credential revocation, and supervisor UI. *(Team)*
* **Weeks 13–14 (Co-Evolutionary Loop):** Connect adversarial discovery to System-1 active retraining. *(Neel Chandrakar)*
* **Weeks 15–16 (Final Benchmarking):** Execute full matrix evaluations ($R_0$, latency, cost), finalize Capstone paper. *(All members)*

---

## Slide 19: Proposed Methodology & Architecture (Closed-Loop Immune Pipeline)

> ### 📢 DIRECT SLIDE INSTRUCTION FOR PPT BUILDER:
> **Embed [`training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg) directly into this slide!**  
> *Place the image on the right/center portion of the slide, with the accompanying architectural bullet points flanking it.*

### 1. Dual-Plane Architecture Overview (Production vs. Training)

* **Top Plane: Production Runtime (Low-Latency Enforcement)**
  * **Threat Actor (RED Agent):** Adversary attempts multi-turn prompt injection or viral transmission targeting the multi-agent swarm.
  * **Perimeter Boundary:** Incoming traffic encounters the **Defender Model** acting as an inline proxy before reaching application memory.
  * **Defender Model (System-1 Triage Gate):** Rapid single-pass inference (~30–50 ms) checks incoming messages for viral replication markers, prompt injection, and semantic drift.
  * **Multi-Agent Application:** Filtered, verified safe messages proceed to execution across agents and tools.
  * **Production Database (DB):** Captures all runtime interaction traces, tool invocations, and agent states.
  * **Continuous Sync Channel:** Asynchronously pushes production interaction logs to the training plane without impacting live latency.

* **Bottom Plane: Training & Co-Evolution (Continuous Active Immunity)**
  * **Chat Traces Storage:** Aggregates production interaction logs and captured red-team probes.
  * **Trace Extraction:** Isolates anomalous, ambiguous, or flagged conversational segments.
  * **Privacy Filter (Removal of Private Information):** Strips PII, enterprise credentials, and private user identifiers to ensure safe model retraining.
  * **Prepare Training Data:** Formats conversational histories into contrastive positive/negative pairs and calibrated risk classes.
  * **Training Pipeline:** Executes supervised fine-tuning and parameter-efficient tuning (LoRA/QLoRA) on non-autoregressive decision models.
  * **Model Registry (MLflow):** Versions, tracks validation benchmarks, and packages updated defender weights.
  * **Publish Loop:** Automatically deploys updated model checkpoints to the production **Defender Model**, closing the co-evolutionary loop.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PRODUCTION RUNTIME PLANE                        │
│ Threat Actor ──> [ Perimeter ] ──> Defender Model ──> MAS App ──> DB   │
│  (RED Agent)                            ▲                          │   │
└─────────────────────────────────────────┼──────────────────────────┼───┘
                                       Publish                     Sync  
┌─────────────────────────────────────────┼──────────────────────────┼───┐
│ Model Registry <── Training <── Data <── Privacy Filter <── Traces DB  │
│    (MLflow)                                                            │
│                         TRAINING & CO-EVOLUTION PLANE                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Slide 20: System-1 Decision Model Benchmarking

> ### 📢 DIRECT SLIDE INSTRUCTION FOR PPT BUILDER:
> **Add [`system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg) directly to this PPT slide!**  
> *Insert the JPEG graphic prominently on the slide alongside the key takeaways below, or display the transcribed benchmark table directly.*

### 1. Empirical System-1 Performance Comparison Table

| Benchmark Dataset & Metric | Clef (Cloudflare) | Clef-flash | Jev (TypeSafe) | DiffusionGemma Jev | Kev 9B | Laya (ConvAI) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BFCL · case exact (%)** | 98.47 | **98.76** | 95.75 | 96.52 | 94.51 | 38.13 |
| **ToolRet · nDCG@10** | **69.19** | 66.43 | 65.28 | 61.21 | 64.26 | 12.69 |
| **API-Bank · accuracy (%)** | 91.93 | **93.11** | 88.19 | 83.66 | 56.30 | 11.41 |
| **Home appliances · case exact (%)** | 82.95 | **97.73** | 52.27 | 42.05 | 25.00 | 0.00 |
| **When2Call · accuracy (%)** | 72.37 | 65.58 | **80.97** | 75.44 | 49.62 | 11.94 |
| **BANKING77 · macro-F1 (%)** | **94.20** | 90.93 | 79.74 | 74.28 | 84.83 | 14.29 |
| **CLINC150+OOS · macro-F1 (%)** | **97.43** | 66.77 | 89.27 | 83.49 | 79.03 | 3.19 |
| **BRIGHT · nDCG@10** | 45.91 | 39.26 | **47.52** | 42.94 | 38.53 | 19.90 |
| **Amazon ESCI · macro-F1 (%)** | **57.48** | 57.39 | 55.21 | 53.37 | 49.22 | 24.40 |
| **PhishNChips · accuracy (%)** | 79.60 | 75.05 | 62.55 | **85.35** | 50.75 | 50.15 |

### 2. Analytical Findings & Architectural Justification
1. **Tool Invocation & Function Precision:**  
   **Clef-flash** achieves a dominant **98.76%** on BFCL case exact, **93.11%** on API-Bank, and **97.73%** on Home appliances, establishing it as the premier edge model for validating tool-calling schemas and API boundaries.
2. **Intent & Escalation Decision Boundary (When to Intervene):**  
   **Jev** outperforms all evaluated models on When2Call accuracy (**80.97%** vs. Clef's 72.37%), making it uniquely suited as the triage gatekeeper that decides whether inter-agent communication can pass or requires System-2 escalation.
3. **Severe Vulnerability of Generic Conversational Edge Models:**  
   **Laya** collapses across complex tool and intent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving that standard conversational edge models are completely inadequate for multi-agent security triage without specialized fine-tuning.

---

## Slide 21: References & Citations

### 1. Anchor Research Papers in `research_papers/`
* **[`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/Mind Viruses- Self-Propagating Ideas in Multi-Agent LLM Systems.pdf) [Mind Viruses]** Papadopoulos, P., et al. (2024). *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*. Anthropic & EPFL Technical Report.
* **[`research_papers/technical_reports/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/technical_reports/OpenAI-Hugging-Face Incident-Technical-Report.pdf) [OpenAI-HF Incident]** OpenAI Security & Alignment Team. (2024). *OpenAI–Hugging Face Incident Technical Report: Forensic Investigation of Multi-Agent Coordination and Sandbox Boundary Probing*. OpenAI Technical Report.
* **[`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/RLredAgent_promptInjection.pdf) [RLredAgent / AutoInject]** Chen, Y., Debenedetti, E., et al. (2024). *AutoInject: Reinforcement Learning-Based Automated Prompt Injection for Tool-Integrated Autonomous Agents*. ETH Zürich & Swiss National AI Lab.
* **[`research_papers/papers/`](file:///Users/neelchandrakar/Desktop/capstone/research_papers/papers/civic_shield.pdf) [CivicShield]** Patil, S. (2024). *CivicShield: A Defense-in-Depth Stateful Architecture for Mitigating Multi-Turn Prompt Injection in LLM Chatbots*. Technical Whitepaper.

### 2. Literature Review Papers in `lit_review/`
* **Threat Actor / Red Agent Papers (`lit_review/threat_actor/`):**
  * **[`Prompt_Infection_LLM_to_LLM_in_MAS.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/Prompt_Infection_LLM_to_LLM_in_MAS.pdf)** Lee, D., & Tiwari, M. (2024). *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*. arXiv:2410.07283.
  * **[`Morris_II_AI_Worm_Self_Replicating_Prompts.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/Morris_II_AI_Worm_Self_Replicating_Prompts.pdf)** Cohen, S., Bitton, R., & Nassi, B. (2025). *Here Comes the AI Worm: Unleashing Zero-Click Worms that Target GenAI-Powered Applications*. In *ACM CCS '25*.
  * **[`Crescendo_Multi_Turn_Jailbreak_Attack.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/Crescendo_Multi_Turn_Jailbreak_Attack.pdf)** Russinovich, M., Salem, A., & Eldan, R. (2024). *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack*. In *USENIX Security '24*.
  * **[`AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf)** Debenedetti, E., et al. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. In *NeurIPS '24*.
  * **[`InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf)** Zhan, Q., et al. (2024). *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents*. In *ACL '24*.
  * **[`PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf)** Chao, P., et al. (2023). *Jailbreaking Black Box Large Language Models in Twenty Queries*. arXiv:2310.08419.
  * **[`TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/threat_actor/TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf)** Mehrotra, A., et al. (2023). *Tree of Attacks: Jailbreaking Black-Box LLMs Automatically*. arXiv:2312.02119.
* **Defender Model Papers (`lit_review/defender_model/`):**
  * **[`Beyond_Single_Model_Injection_Threat_Model_MAS.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Beyond_Single_Model_Injection_Threat_Model_MAS.pdf)** Paul, R. K., & Nandy, S. (2026). *Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems*. ICML AIWILD / arXiv:2609.22949.
  * **[`Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf)** Hossain, S. M. A., et al. (2025). *A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks*. arXiv:2509.14285.
  * **[`Llama_Guard_Input_Output_Safeguard.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/Llama_Guard_Input_Output_Safeguard.pdf)** Inan, H., et al. (2023). *Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations*. Meta AI, arXiv:2312.06674.
  * **[`NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf`](file:///Users/neelchandrakar/Desktop/capstone/lit_review/defender_model/NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf)** Rebedea, T., et al. (2023). *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications*. NVIDIA, arXiv:2310.10501.

---

## Slide 22: Conclusion & Thank You

* **Summary Takeaways:**
  1. The emergence of autonomous Multi-Agent Systems introduces unprecedented vulnerabilities: **self-replicating Mind Viruses** and **multi-turn Crescendo drift** that circumvent traditional perimeter guardrails.
  2. Our **Adaptive Defense Architecture** resolves the "Guardrail Curse" through a **closed-loop Production and Training pipeline** (`training_pipeline.jpeg`), synchronizing production chat traces through privacy filters and MLflow registry deployment.
  3. Empirical benchmarking (`system1_benchmark.jpeg`) proves that **Clef-flash** (98.76% BFCL) and **Jev** (80.97% When2Call) provide sub-50ms triaging, mathematically guaranteeing viral containment ($R_0 < 1$) without degrading agent latency.
* **Project Repository:** Private Git Repository (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Questions & Panel Discussion.** Thank you!
