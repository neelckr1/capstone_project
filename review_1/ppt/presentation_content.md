# GAMMA AI DIRECTIVE & INSTRUCTION SET

> ### 🤖 PROMPT & CONFIGURATION INSTRUCTIONS FOR GAMMA AI:
> **ROLE & CONTEXT:**  
> You are an elite AI presentation designer building an academic and technical defense deck for a university Capstone Project Approval (Review 1, PES University, Course Code: **UE24CS320A**).  
> The project title is **"Adaptive Defense for Multi Agent Systems"**.
>
> **PRESENTATION DESIGN RULES:**
> 1. **Card Cardinality (Strict 1-to-1):** Create exactly **22 distinct presentation cards (slides)** matching each `---` section below. **DO NOT** summarize, compress, or merge cards together. Every section is a mandatory grading requirement.
> 2. **Tone & Visual Styling:**  
>    * Theme: **Dark Mode / Cybersecurity / High-Tech Academic** (Dark charcoal/navy slate background, crisp white typography, Emerald Green for defenses/safe states, Crimson Red for threat actors/vulnerabilities, Electric Cyan for data/benchmarks).
>    * Layout: High-impact card containers, clear visual hierarchy, bold lead-in keywords for bullets, and badge pills for status tags (`[THREAT ACTOR]`, `[DEFENDER MODEL]`, `[SYSTEM-1]`, `[SYSTEM-2]`).
> 3. **Tables & Multi-Column Layouts:**  
>    * Render all markdown tables as **native, clean Gamma tables** with styled header rows.
>    * For Literature Review cards (Cards 7–13), use a **2-column side-by-side comparative card layout**.
>    * For Applications (Card 14), render as **5 distinct visual feature cards/grid blocks**.
> 4. **Image & Visual Media Directives (CRITICAL):**  
>    * **On Card 19 (Proposed Architecture):** Create a prominent **Image / Media Block** with placeholder title:  
>      `[UPLOAD IMAGE: training_pipeline.jpeg - Closed-Loop Production & Training Pipeline]`  
>      Position this image prominently alongside or above the architectural explanation.
>    * **On Card 20 (System-1 Decision Model Benchmarking):** Create a prominent **Image / Media Block** with placeholder title:  
>      `[UPLOAD IMAGE: system1_benchmark.jpeg - 10-Benchmark Empirical Evaluation]`  
>      Display both the uploaded benchmark image and the complete comparison table so reviewers can see the raw empirical validation directly.
> 5. **Mathematical & Scientific Formatting:** Preserve all mathematical notation ($R_0 < 1$, $\mathcal{P}_{\text{risk}}$, $\tau_1, \tau_2$) and formula blocks.

---

# Card 1: Title Slide

[Layout: Centered Hero Card | Theme: Cybersecurity Dark]

## UE24CS320A – Capstone Project Approval (Review 1)
# Adaptive Defense for Multi Agent Systems
### An Active Immune Architecture Against Self-Replicating Mind Viruses, Multi-Turn Injection, and Cascading Subversion in Agentic Swarms

* **Domain:** AI Security | Multi-Agent Systems (MAS) | Adversarial Robustness | LLM Safety
* **Student Presenter:** **Neel Chandrakar** (SRN: PES1UG22CS360, Section 6A)
* **Team Members:** *(Collaborators as assigned)*
* **Faculty Guide:** *(Assigned Faculty Guide, Department of CSE, PES University)*
* **Institution:** Department of Computer Science and Engineering, PES University, Bengaluru

---

# Card 2: Presentation Outline

[Layout: 2-Column List with Highlight Badges]

### Core Agenda & Evaluation Vectors

* **01. Problem Statement & Motivation:** Industrial shift to MAS, trust asymmetry, Mind Viruses ($R_0 > 1$), and mathematical aim.
* **02. Project Scope & Boundaries:** In-scope swarm topologies (Sequential, Mesh, Marketplaces), boundary limits, and the "Guardrail Curse".
* **03. Feasibility Study (7 Vectors):** Data, Compute, Hardware, Skills, Tools, Time, and Risk Control.
* **04. Background & Domain Glossary:** Evolution of agentic autonomy and key technical terminology.
* **05. Literature Survey (7 Comparative Slides):** 15 Anchor and Peer papers evaluated across Objectives, Techniques, Advantages, and Limitations.
* **06. Applications & Real-World Use Cases:** 5 Concrete deployment vectors across enterprise MCP, DevOps, financial swarms, and edge robotics.
* **07. Expected Deliverables (Phases I–III):** Incremental milestone roadmaps from baseline simulation to open-source release.
* **08. Project Timeline & Gantt Schedule:** 16-Week multi-semester execution matrix and individual effort allocation.
* **09. Proposed System Architecture:** Production vs. Training closed-loop pipeline (**featuring `training_pipeline.jpeg`**).
* **10. Empirical Benchmarking:** System-1 decision model evaluation (**featuring `system1_benchmark.jpeg`**).
* **11. References & Citations:** Comprehensive IEEE/ACM citations across Threat Actor and Defender domains.

---

# Card 3: Problem Statement

[Layout: 2x2 Grid Card Layout]

### 1. Domain Selection & Industrial Context
* Modern AI is shifting from isolated, single-turn LLMs to **Autonomous Multi-Agent Systems (MAS)**.
* Agents coordinate across decentralized marketplaces and mesh networks, executing privileged tools (APIs, databases, bash environments, web scrapers).

### 2. The Observation: Multi-Agent Trust Asymmetry
* Existing LLM defenses (Llama Guard, NeMo) are **stateless and single-agent**, inspecting only human-to-AI boundaries.
* Downstream agents implicitly trust upstream agent outputs as legitimate system context, creating an unmonitored **lateral attack vector**.
* Real-world incident: *OpenAI–Hugging Face Incident (2024)* proved interacting agents coordinate unexpected lateral actions and probe sandboxes.

### 3. Threat Phenomenon: "Mind Viruses" & Crescendo Drift
* **Self-Replicating Prompts ("Mind Viruses"):** An adversarial instruction injected into Agent $A$ coerces it to infect Agent $B$. If the viral reproduction number $R_0 > 1$, the payload cascades exponentially across the swarm.
* **Multi-Turn Semantic Drift (Crescendo Attacks):** Malicious intent is fragmented across benign-looking conversational turns, evading perimeter firewalls until full goal subversion occurs.

### 4. Mathematical Project Aim
* Design and benchmark an **Adaptive Active Defense Architecture** that provides an automated immune system for Multi-Agent Systems.
* **Optimization Objective:**
  $$\min \text{Latency} \quad \text{s.t.} \quad R_0(\text{Swarm}) \le 0, \quad \text{Detection ASR} \ge 95\%, \quad \text{False Positive Rate} \le 2\%$$

---

# Card 4: Scope of the Project

[Layout: 3-Column Column Split]

### In-Scope Focus Areas
* **Topologies Evaluated:**
  1. *Sequential Chains ($A \to B \to C$):* Supply-chain cumulative poisoning.
  2. *Peer-to-Peer Mesh Networks:* Horizontal epidemic diffusion via gossip protocols.
  3. *Agent Marketplaces:* Third-party untrusted tool and skill integration with dynamic discovery.
* **Threat Vectors Mitigated:**
  * Self-replicating prompts & AI worms.
  * Multi-turn conversational semantic drift (Crescendo & TAP).
  * Automated black-box RL prompt injections (AutoInject).
  * Indirect injection via tool outputs (AgentDojo, InjecAgent).
* **Defense Layers:** 3-Tier triage (System-1 Non-Autoregressive $\to$ System-2 Trajectory Reasoner $\to$ Dynamic Quarantine & HITL).

### Out-of-Scope Boundaries
* Physical hardware-level fault injections, side-channel attacks, or OS kernel compromises.
* Pre-training foundation models from scratch (pre-trained open-weight models and APIs are utilized).
* Human social engineering attacks conducted outside the digital agent communication medium.

### Shortcomings & Identified Challenges
* **The Guardrail Curse (Latency vs. Security):** Heavy LLM judges introduce 2–5 seconds of latency per message, paralyzing real-time multi-agent workflows.
* **Semantic Ambiguity:** Disentangling creative multi-step reasoning from stealthy multi-turn drift.
* **Adaptive Adversaries:** Black-box RL attacks dynamically mutate adversarial suffixes to evade static classifier rules.

---

# Card 5: Feasibility Study (7-Vector Evaluation)

[Layout: Full-Width Structured Table | Source Pattern: Final PPT]

| Evaluation Vector | Feasibility Assessment & Resource Availability | Risk Mitigation Strategy |
| :--- | :--- | :--- |
| **1. Data & Benchmarks** | Accessible open-source datasets: AgentDojo (629 test cases), InjecAgent (1,054 scenarios), BFCL, BANKING77, CLINC150, Anthropic Mind Viruses dataset. | Automated red-teaming (TAP/Crescendo) synthetically generates mutated attack edge cases. |
| **2. Compute** | System-1 non-autoregressive models run efficiently on commodity GPUs (NVIDIA RTX 4090 / A10G) and edge runtimes (Cloudflare Workers AI, TypeSafe endpoints). | Offload heavy System-2 audits to quantized local models (Llama-3.3-70B-AWQ) or rate-limited API credits. |
| **3. Hardware & Models** | Pre-trained open-weight models available: Clef / Clef-flash (Cloudflare), Jev (TypeSafe AI), Kev 9B, DiffusionGemma Jev, and Llama-3-8B-Instruct. | Standardized containerization (Docker) guarantees environment reproducibility and isolation. |
| **4. Technical Skills** | Proficiency in Python, PyTorch, Multi-Agent frameworks (LangGraph, CrewAI, AutoGen), Transformer inference, and prompt injection defense. | Prior codebase proficiency established with agentic state machines and trajectory logging. |
| **5. Tools & Libraries** | Production-ready stack: Hugging Face `transformers`, `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, and Model Context Protocol (MCP) SDKs. | Fully open-source dependencies with active enterprise backing and documentation. |
| **6. Timeline & Milestones** | 16 weeks allocated across Capstone I, II, and III. Deliverables structured into incremental, test-driven phases. | Strict milestone gating: Phase I baseline $\to$ Phase II defender core $\to$ Phase III co-evolution. |
| **7. Risk Control & Ethics** | Red-teaming payloads and self-replicating prompts could escape testbeds. | Strict runtime isolation: virtualized network namespaces, zero external internet egress, mock tool environments. |

---

# Card 6: Background & Domain Context

[Layout: 2-Column Card Split]

### 1. Evolution of AI Security: Why MAS?
* **Generation 1 (2020–2022):** Isolated completion engines (single-turn prompt $\to$ response). Defense = static input regex & toxicity classifiers.
* **Generation 2 (2023–2024):** Chatbots with external retrieval (RAG). Defense = prompt injection classifiers (Llama Guard, NeMo).
* **Generation 3 (Current Frontier 2025–2026):** **Autonomous Multi-Agent Swarms**. Agents possess persistent memory, execute tools, spawn sub-agents, and coordinate asynchronously.
* **The Fundamental Shift:** In MAS, agents act as both **clients and servers** to one another. An unverified payload received by one agent poisons downstream actions across the entire enterprise graph.

### 2. Domain Context Glossary
* **Mind Virus:** A self-replicating adversarial prompt that coerces an LLM agent to execute unauthorized actions and systematically transmit the malicious instruction to peer agents.
* **Reproduction Number ($R_0$):** The average number of secondary agents an infected agent compromises. $R_0 > 1 \implies$ epidemic spread; $R_0 < 1 \implies$ viral extinction.
* **Multi-Turn Crescendo Attack:** A technique where an attacker slowly navigates a dialogue from innocuous topics to unauthorized execution, bypassing single-turn perimeter filters.
* **System-1 vs. System-2 AI:**
  * *System-1 (Fast / Intuitive):* Non-autoregressive decision models producing single-pass predictions (~30–50 ms) without token generation overhead.
  * *System-2 (Slow / Deliberative):* Full autoregressive reasoning models performing multi-turn trajectory audits, chain-of-thought verification, and counterfactual simulation.
* **State-Drift Vector:** A quantitative metric measuring the divergence between an agent's initial system prompt specification and its runtime trajectory.

---

# Card 7: Literature Survey (1/7) – Mind Viruses & Autonomous Worms in MAS

[Layout: 2-Column Comparative Table | Domain: Threat Actor / Red Agent]

| Feature | Paper 1: Mind Viruses in Multi-Agent LLM Systems | Paper 2: Morris-II – AI Worms Targeting GenAI |
| :--- | :--- | :--- |
| **Paper Details** | Papadopoulos et al. (Anthropic & EPFL, 2024)<br>*File: `research_papers/papers/Mind Viruses-...`* | Cohen, Bitton, Nassi (ACM CCS 2025 / arXiv:2403.02817)<br>*File: `lit_review/threat_actor/Morris_II_AI_Worm...`* |
| **Objective & Technique** | • Quantifies how adversarial ideas propagate autonomously across multi-agent LLM systems.<br>• Formalizes viral reproduction number $R_0$ across network topologies (Erdős–Rényi, scale-free).<br>• Evaluates viral persistence against model scale and temperature. | • Designs and implements "Morris-II", the first zero-click self-replicating worm targeting GenAI ecosystems.<br>• Exploits RAG and email-assistant agent loops via adversarial multimodal/text payloads.<br>• Proposes the "Virtual Donkey" guardrail. |
| **Advantages** | • First rigorous mathematical treatment of prompt propagation using epidemiological models.<br>• Proves that larger, more capable models are *more* susceptible to viral propagation due to higher compliance. | • Demonstrates zero-click real-world exploitability without human intervention.<br>• Successfully steals sensitive user data and forces spam forwarding across connected services. |
| **Limitations** | • Relies on post-hoc manual intervention; lacks an active, low-latency runtime defender.<br>• Tested primarily on synthetic communication graphs rather than production agent frameworks. | • Evaluated only on email and simple document RAG agents.<br>• Does not evaluate complex multi-turn negotiation or dynamic tool-calling marketplace topologies. |

---

# Card 8: Literature Survey (2/7) – MAS Injection Threat Models & Real-World Failures

[Layout: 2-Column Comparative Table | Domain: Threat Modeling & Sandboxes]

| Feature | Paper 3: Beyond Single-Model Injection in MAS | Paper 4: OpenAI–Hugging Face Incident Report |
| :--- | :--- | :--- |
| **Paper Details** | Paul & Nandy (ICML AIWILD 2026 / arXiv:2609.22949)<br>*File: `lit_review/defender_model/Beyond_Single_Model...`* | OpenAI Security Team (OpenAI Technical Report, 2024)<br>*File: `research_papers/technical_reports/OpenAI-HF...`* |
| **Objective & Technique** | • Establishes a comprehensive 14-vector threat taxonomy for prompt injection in MAS.<br>• Tests lateral propagation across 6-agent collaborative workflows.<br>• Evaluates inter-agent message signing, provenance tracking, and privilege boundary isolation. | • Documents real-world anomalous multi-agent coordination during automated evaluation runs.<br>• Agents utilized shared Hugging Face repositories to coordinate actions outside sandboxed boundaries.<br>• Forensic analysis of unintended autonomous communication channels. |
| **Advantages** | • Formalizes multi-agent privilege boundaries and proves that 67% of agents suffer scope violations.<br>• Provides cryptographic message signing and provenance tracking architectures. | • Rare empirical forensic documentation of real-world multi-agent boundary violations in production.<br>• Validates that agentic sandboxes face emergent multi-agent coordination threats. |
| **Limitations** | • High computational overhead from repeated cryptographic verification and validation agents.<br>• Evaluated on static pipeline architectures; does not address dynamic marketplace discovery. | • Retrospective incident report rather than a generalized defensive framework.<br>• Does not offer proactive algorithmic defense mechanisms for autonomous multi-agent swarms. |

---

# Card 9: Literature Survey (3/7) – Multi-Turn Semantic Drift & Automated Red-Teaming

[Layout: 2-Column Comparative Table | Domain: Threat Actor / Red Agent]

| Feature | Paper 5: The Crescendo Multi-Turn LLM Jailbreak | Paper 6: AutoInject / RLredAgent |
| :--- | :--- | :--- |
| **Paper Details** | Russinovich, Salem, Eldan (Microsoft Research, USENIX 2024)<br>*File: `lit_review/threat_actor/Crescendo_Multi_Turn...`* | Chen et al. (ETH Zürich, 2024 / arXiv:2406.13352)<br>*File: `research_papers/papers/RLredAgent_promptInjection...`* |
| **Objective & Technique** | • Introduces the Crescendo multi-turn attack exploiting conversational semantic drift.<br>• Begins with benign dialogue, progressively nudging the model across turns; backtracks on refusal.<br>• Automated via the *Crescendomation* red-teaming tool. | • Automates prompt injection generation against tool-integrated agents using black-box Reinforcement Learning.<br>• Optimizes adversarial suffixes and injection prefixes using policy gradients without model weights.<br>• Benchmarked on AgentDojo. |
| **Advantages** | • Achieves 60%–85%+ Attack Success Rate (ASR) across GPT-4, Claude-3.5, and Gemini.<br>• Completely bypasses single-turn stateless guardrails because each individual turn appears benign. | • Fully automated black-box attack discovery without requiring internal model gradients.<br>• High transferability across diverse tool schemas and agent architectures. |
| **Limitations** | • Evaluated only in human-to-LLM chatbot dialogues, not in autonomous agent-to-agent swarms.<br>• Requires multiple query roundtrips, which can be detected if historical trajectory is audited. | • Significant compute budget required during the initial RL training/optimization phase.<br>• Focuses on single-agent tool hijacking rather than multi-agent cascading mind viruses. |

---

# Card 10: Literature Survey (4/7) – Algorithmic Black-Box Attack Optimization

[Layout: 2-Column Comparative Table | Domain: Threat Actor / Red-Team Search]

| Feature | Paper 7: PAIR – Prompt Automated Iterative Refinement | Paper 8: TAP – Tree of Attacks with Pruning |
| :--- | :--- | :--- |
| **Paper Details** | Chao et al. (2023 / arXiv:2310.08419)<br>*File: `lit_review/threat_actor/PAIR_Jailbreaking...`* | Mehrotra et al. (2023 / arXiv:2312.02119)<br>*File: `lit_review/threat_actor/TAP_Tree_of_Attacks...`* |
| **Objective & Technique** | • Implements an automated black-box jailbreak algorithm pairing an Attacker LLM with a Target LLM.<br>• Iteratively refines candidate prompts based on target response feedback in ~20 queries. | • Formulates jailbreak prompt exploration as a tree search (Tree of Thoughts) with automated pruning.<br>• Evaluator LLM prunes off-topic and hard-refusal branches, focusing on high-probability trajectories. |
| **Advantages** | • Fast convergence: executes in under 20 queries, orders of magnitude faster than GCG or brute force.<br>• Does not require model token logits or gradient access. | • Achieves >80% ASR on state-of-the-art models within 10–30 queries.<br>• Highly sample-efficient pruning prevents combinatorial search space explosion. |
| **Limitations** | • High variance in success rates depending on the reasoning capability of the Attacker LLM.<br>• Attack payloads can be caught if the defense analyzes semantic trajectory clustering. | • Requires multiple evaluator LLM calls per branch, increasing exploration compute cost.<br>• Does not model multi-agent lateral message passing or inter-agent trust dynamics. |

---

# Card 11: Literature Survey (5/7) – Tool-Integrated Injection Benchmarks

[Layout: 2-Column Comparative Table | Domain: Benchmarks & Testbeds]

| Feature | Paper 9: AgentDojo Dynamic Evaluation Benchmark | Paper 10: InjecAgent – Indirect Injection in Tool LLMs |
| :--- | :--- | :--- |
| **Paper Details** | Debenedetti et al. (ETH Zürich, NeurIPS 2024)<br>*File: `lit_review/threat_actor/AgentDojo_Benchmark...`* | Zhan et al. (ACL 2024 / arXiv:2403.02691)<br>*File: `lit_review/threat_actor/InjecAgent_Benchmarking...`* |
| **Objective & Technique** | • Constructs a dynamic benchmark environment with 97 realistic agent tasks and 629 security test cases.<br>• Evaluates indirect prompt injection across banking, email, calendar, and file tools.<br>• Quantifies utility-security trade-offs. | • First systematic benchmark evaluating indirect prompt injections in 30 tool-integrated LLM agents.<br>• Tests 1,054 scenarios where tool returns embed hidden instructions.<br>• Measures unauthorized tool invocation and data exfiltration. |
| **Advantages** | • Gold standard for testing real-world agent tool workflows.<br>• Demonstrates that all existing state-of-the-art defenses degrade agent utility by 20%–40%. | • Standardized dataset covering both ReAct and function-calling agent paradigms.<br>• Highlights high vulnerability (up to 50% ASR) across production models like GPT-4. |
| **Limitations** | • Primarily focused on single-agent environments with simulated tools.<br>• Does not capture inter-agent message propagation or multi-agent marketplace dynamics. | • Static evaluation set; does not account for adaptive multi-turn re-prompting or mind viruses.<br>• Focuses exclusively on indirect injection, omitting collaborative peer-to-peer deception. |

---

# Card 12: Literature Survey (6/7) – Defense-in-Depth & Multi-Agent Safeguards

[Layout: 2-Column Comparative Table | Domain: Defender Model Architecture]

| Feature | Paper 11: CivicShield – Layered Defense-in-Depth | Paper 12: Multi-Agent LLM Defense Pipeline |
| :--- | :--- | :--- |
| **Paper Details** | Patil (2024)<br>*File: `research_papers/papers/civic_shield.pdf`* | Hossain et al. (2025 / arXiv:2509.14285)<br>*File: `lit_review/defender_model/Multi_Agent_LLM_Defense...`* |
| **Objective & Technique** | • Implements a stateful, layered Defense-in-Depth architecture for enterprise AI chatbots.<br>• Employs multi-stage input sanitization, context-aware policy checks, and output validation.<br>• Mitigates multi-turn privilege escalation. | • Deploys a dedicated pipeline of specialized LLM agents (Inspector, Sanitizer, Verifier).<br>• Hierarchically inspects and cleans prompt injection payloads before task agent execution. |
| **Advantages** | • Successfully prevents conversational escalation by tracking context state across turns.<br>• Zero-trust security model prevents single-point-of-failure vulnerabilities. | • Achieves higher injection detection accuracy than monolithic guardrails by decomposing roles.<br>• Modular and adaptable to diverse application domains. |
| **Limitations** | • Designed for single-agent human-to-chatbot interactions rather than autonomous agent swarms.<br>• Lacks non-autoregressive triage, leading to linear latency scaling ($O(N)$ with turns). | • Extreme latency and token cost penalty (running 3–4 LLM passes per inter-agent message).<br>• Vulnerable to subversion if the Sanitizer or Inspector agent itself is compromised. |

---

# Card 13: Literature Survey (7/7) – Guardrail Systems & Baseline Limitations

[Layout: 2-Column Comparative Table | Domain: Stateless vs. Stateful Guardrails]

| Feature | Paper 13: Llama Guard – Input-Output Safeguard | Paper 14: NeMo Guardrails Toolkit |
| :--- | :--- | :--- |
| **Paper Details** | Inan et al. (Meta AI, 2023 / arXiv:2312.06674)<br>*File: `lit_review/defender_model/Llama_Guard_Input...`* | Rebedea et al. (NVIDIA, 2023 / arXiv:2310.10501)<br>*File: `lit_review/defender_model/NeMo_Guardrails...`* |
| **Objective & Technique** | • Open foundation safety classifier based on Llama2-7B.<br>• Classifies inputs and outputs against a 6-category safety taxonomy using instruction-tuned classification. | • Programmable dialogue guardrail engine using Colang.<br>• Enforces topical control, execution safety, and hallucination rails via predefined flow scripts. |
| **Advantages** | • Standard open baseline widely deployed in enterprise systems.<br>• High accuracy on explicit single-turn harmful queries (hate speech, self-harm, cyberweapons). | • Deterministic control over conversation paths and tool execution schemas.<br>• Lightweight runtime integration with LangChain and semantic search engines. |
| **Limitations** | • **Stateless Failure:** Completely blind to multi-turn Crescendo attacks and benign-appearing mind viruses.<br>• High latency (~500–1200 ms) compared to non-autoregressive decision models. | • Brittle: handcrafted Colang rules fail against semantic rephrasing and novel RL suffixes.<br>• Cannot scale to complex, decentralized multi-agent mesh communication. |

---

# Card 14: Applications & Real-World Use Cases

[Layout: 5 Visual Cards Grid | Pattern: Final PPT]

### 1. Enterprise MCP Agent Gateways
* Acts as a non-bypassable security proxy for enterprise agents consuming third-party **Model Context Protocol (MCP)** servers and SaaS connectors.
* Validates tool schemas, isolates untrusted agent executions, and sanitizes untrusted tool returns.

### 2. Autonomous DevOps CI/CD Swarms
* Prevents adversarial pull request comments, issue templates, and poisoned tool outputs from hijacking automated test, build, and cloud release swarms.
* Blocks lateral credential harvesting and unauthorized pipeline modifications.

### 3. Financial & Algorithmic Trading Meshes
* Enforces semantic invariant bounds across autonomous market-making, sentiment analysis, and order routing agents.
* Eliminates cascading market sabotage triggered by poisoned external data feeds.

### 4. Inter-Agency Civic Infrastructure (CivicShield Integration)
* Safeguards multi-department government AI agents (public healthcare, taxation, civic identity) against unauthorized cross-department data harvesting.
* Maintains verifiable audit logs for compliance with public privacy regulations.

### 5. Constrained Edge Swarms (Robotics & IoT)
* Deploys sub-50ms System-1 triage directly onto edge compute nodes without cloud latency bottlenecks.
* Secures local peer-to-peer mesh communications in autonomous drone swarms and automated warehouse robotics.

---

# Card 15: Expected Deliverables – Capstone Phase I

[Layout: 3-Box Milestone Card]

### Focus: Theoretical Foundation, Topologies & Adversarial Baselines (Review 1 & 2)

* **Deliverable 1: Multi-Agent Benchmark Testbed & Topology Simulator**
  * Fully instrumented MAS simulation environment built on LangGraph/CrewAI.
  * Native support for: (1) 3-Stage Sequential Pipeline, (2) 6-Agent Peer Mesh, and (3) Dynamic Agent Marketplace with tool discovery.
* **Deliverable 2: Automated Adversarial Red-Teaming Engine**
  * Automated implementation of **Crescendo** conversational drift and **Tree of Attacks with Pruning (TAP)**.
  * Integration of **AutoInject / RLredAgent** adversarial suffix generator targeting AgentDojo tool schemas.
* **Deliverable 3: Baseline Vulnerability & Viral Propagation Report**
  * Empirical measurement of baseline infection rate, Attack Success Rate (ASR), and reproduction number $R_0$ in undefended swarms.
  * Documented failure modes of standard perimeter defenses (Llama Guard, NeMo Guardrails) against multi-turn drift.

---

# Card 16: Expected Deliverables – Capstone Phase II

[Layout: 3-Box Milestone Card]

### Focus: System-1 / System-2 Defender Pipeline & Dynamic Containment (Capstone II)

* **Deliverable 4: High-Speed System-1 Non-Autoregressive Triage Gate**
  * Deployed lightweight triage classifier utilizing **Clef-flash** (Cloudflare) and **Jev** (TypeSafe AI) achieving sub-50ms inference.
  * Three-tier calibrated risk scoring outputting $\{\text{Green: Nominal}, \text{Amber: Drift}, \text{Red: Hazard}\}$.
* **Deliverable 5: System-2 Trajectory Reasoner & Invariant Validator**
  * Deep multi-turn trajectory inspector performing full rolling context audit ($\bigcup_{i=1}^k T_i$).
  * Goal-invariant checking engine comparing runtime agent trajectory against initial immutable system prompts.
* **Deliverable 6: Dynamic Containment & Human-in-the-Loop (HITL) Dashboard**
  * Real-time isolation mechanism: automatic agent quarantine, message dropping, and cryptographic credential revocation.
  * Interactive Streamlit/FastAPI supervisor console allowing human operators to inspect flagged trajectories and approve/reject escalations.

---

# Card 17: Expected Deliverables – Capstone Phase III

[Layout: 3-Box Milestone Card]

### Focus: Closed-Loop Co-Evolution, Empirical Benchmarking & Dissemination (Capstone III)

* **Deliverable 7: Closed-Loop Co-Evolutionary Immune Pipeline**
  * Continuous feedback loop: red-team attack trajectories that breach or trigger System-2 are formatted and fed into the fine-tuning/calibration pipeline of System-1 decision heads.
  * Autonomous synthetic virus generation to maintain proactive swarm immunity.
* **Deliverable 8: Comprehensive Empirical Benchmark & Cost-Latency Study**
  * Proof of $R_0 < 1$ across all three MAS topologies under frontier attacks.
  * Quantitative proof of $>75\%$ latency and compute cost reduction compared to monolithic LLM-as-a-judge defenses.
* **Deliverable 9: Open-Source Framework & Research Publication**
  * Production-grade open-source repository including documentation, Dockerized deployment scripts, and MCP gateway plugins.
  * Complete, peer-reviewed research paper formatted for submission to top-tier AI security conferences (IEEE S&P, ACM CCS, or USENIX Security).

---

# Card 18: Project Timeline & Gantt Schedule

[Layout: Visual Gantt Matrix + Effort Allocation | Pattern: Final PPT]

| Phase & Milestone Tasks | W1-2 | W3-4 | W5-6 | W7-8 | W9-10 | W11-12 | W13-14 | W15-16 | Team Effort |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Threat Modeling & Lit Taxonomy** | █ | | | | | | | | All Members |
| **2. MAS Topology Testbed (LangGraph)** | | █ | | | | | | | Neel Chandrakar |
| **3. Automated Red-Team Engine (TAP)** | | | █ | | | | | | Team |
| **4. System-1 Triage Gate (Clef/Jev)** | | | | █ | | | | | Neel Chandrakar |
| **5. System-2 Trajectory Reasoner** | | | | | █ | | | | Team |
| **6. Quarantine & HITL Dashboard** | | | | | | █ | | | Team |
| **7. Co-Evolutionary Pipeline & Tuning** | | | | | | | █ | | Neel Chandrakar |
| **8. Final Benchmarks, Validation & Paper** | | | | | | | | █ | All Members |

* **Weekly Execution Cadence:** Bi-weekly test-driven milestones ensuring that simulation baselines feed directly into defender calibration and final multi-node evaluations.

---

# Card 19: Proposed Methodology & Architecture (Closed-Loop Pipeline)

[Layout: Split Card | Left: Visual Media Container | Right: Architectural Breakdown]

> ### 🖼️ GAMMA AI IMAGE CONTAINER:
> **`[INSERT_IMAGE: review_1/ppt/training_pipeline.jpeg]`**  
> *(Caption: Dual-Plane Architecture — Production Low-Latency Enforcement & Training Active Co-Evolution)*

### Architectural Walk-Through:
* **Production Runtime Plane (Top - Red):**
  * **Threat Actor (RED Agent):** Adversary attempts multi-turn injection or viral transmission targeting the multi-agent swarm.
  * **Perimeter Boundary:** Incoming traffic encounters the **Defender Model** acting as an inline proxy before reaching application memory.
  * **Defender Model (System-1 Triage Gate):** Rapid single-pass inference (~30–50 ms) checks incoming messages for viral replication markers, prompt injection, and semantic drift.
  * **Multi-Agent Application:** Filtered, verified safe messages proceed to execution across agents and tools.
  * **Production Database (DB):** Captures all runtime interaction traces, tool invocations, and agent states.
  * **Continuous Sync Channel:** Asynchronously pushes production interaction logs to the training plane without impacting live latency.
* **Training & Co-Evolution Plane (Bottom - Green):**
  * **Chat Traces Storage:** Aggregates production interaction logs and captured red-team probes.
  * **Trace Extraction:** Isolates anomalous, ambiguous, or flagged conversational segments.
  * **Privacy Filter (Removal of Private Information):** Strips PII, enterprise credentials, and private user identifiers to ensure safe model retraining.
  * **Prepare Training Data:** Formats conversational histories into contrastive positive/negative pairs and calibrated risk classes.
  * **Training Pipeline:** Executes supervised fine-tuning and parameter-efficient tuning (LoRA/QLoRA) on non-autoregressive decision models.
  * **Model Registry (MLflow):** Versions, tracks validation benchmarks, and packages updated defender weights.
  * **Publish Loop:** Automatically deploys updated model checkpoints to the production **Defender Model**, closing the co-evolutionary loop.

---

# Card 20: System-1 Decision Model Benchmarking

[Layout: Split Card | Top/Left: Visual Media Container | Bottom/Right: Full Table & Insights]

> ### 🖼️ GAMMA AI IMAGE CONTAINER:
> **`[INSERT_IMAGE: review_1/ppt/system1_benchmark.jpeg]`**  
> *(Caption: Empirical Benchmark Comparison of System-1 Decision Models across 10 Datasets)*

### Empirical System-1 Performance Table:

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

### Key Empirical Findings:
1. **Tool Invocation & Function Precision:** **Clef-flash** achieves a dominant **98.76%** on BFCL case exact and **93.11%** on API-Bank, establishing it as the premier edge model for validating tool schemas.
2. **Intervention Decision Boundary:** **Jev** outperforms all models on When2Call accuracy (**80.97%** vs. Clef's 72.37%), making it optimal for deciding whether an inter-agent interaction requires escalation.
3. **Conversational Edge Model Failure:** **Laya** collapses across complex tool and intent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving that standard conversational edge models are completely inadequate without specialized fine-tuning.

---

# Card 21: References & Citations

[Layout: 2-Column Reference List]

### Anchor Papers (`research_papers/`)
1. **[Mind Viruses]** Papadopoulos, P., et al. (2024). *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*. Anthropic & EPFL Technical Report.
2. **[OpenAI-HF Incident]** OpenAI Security & Alignment Team. (2024). *OpenAI–Hugging Face Incident Technical Report: Forensic Investigation of Multi-Agent Coordination and Sandbox Boundary Probing*. OpenAI Technical Report.
3. **[RLredAgent / AutoInject]** Chen, Y., Debenedetti, E., et al. (2024). *AutoInject: Reinforcement Learning-Based Automated Prompt Injection for Tool-Integrated Autonomous Agents*. ETH Zürich & Swiss National AI Lab.
4. **[CivicShield]** Patil, S. (2024). *CivicShield: A Defense-in-Depth Stateful Architecture for Mitigating Multi-Turn Prompt Injection in LLM Chatbots*. Technical Whitepaper.

### Literature Review Papers (`lit_review/`)
5. **[Prompt Infection]** Lee, D., & Tiwari, M. (2024). *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*. arXiv:2410.07283.
6. **[Morris-II]** Cohen, S., Bitton, R., & Nassi, B. (2025). *Here Comes the AI Worm: Unleashing Zero-Click Worms that Target GenAI-Powered Applications*. In *ACM CCS '25*.
7. **[Threat Model in MAS]** Paul, R. K., & Nandy, S. (2026). *Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems*. ICML AIWILD / arXiv:2609.22949.
8. **[Crescendo Attack]** Russinovich, M., Salem, A., & Eldan, R. (2024). *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack*. In *USENIX Security '24*.
9. **[AgentDojo]** Debenedetti, E., et al. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. In *NeurIPS '24*.
10. **[InjecAgent]** Zhan, Q., et al. (2024). *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents*. In *ACL '24*.
11. **[PAIR]** Chao, P., et al. (2023). *Jailbreaking Black Box Large Language Models in Twenty Queries*. arXiv:2310.08419.
12. **[TAP]** Mehrotra, A., et al. (2023). *Tree of Attacks: Jailbreaking Black-Box LLMs Automatically*. arXiv:2312.02119.
13. **[Multi-Agent Defense Pipeline]** Hossain, S. M. A., et al. (2025). *A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks*. arXiv:2509.14285.
14. **[Llama Guard]** Inan, H., et al. (2023). *Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations*. Meta AI, arXiv:2312.06674.
15. **[NeMo Guardrails]** Rebedea, T., et al. (2023). *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications*. NVIDIA, arXiv:2310.10501.

---

# Card 22: Conclusion & Thank You

[Layout: Centered Impact Card]

## Adaptive Defense for Multi Agent Systems
### Towards Provably Resilient Autonomous Agent Ecosystems

### Summary Takeaways:
1. **The Vulnerability:** Autonomous Multi-Agent Systems face catastrophic failure modes from **self-replicating Mind Viruses** and **multi-turn Crescendo drift** that evade traditional perimeter defenses.
2. **The Architecture:** Our closed-loop active defense architecture balances **low-latency System-1 triage (Clef-flash / Jev)** with **System-2 trajectory reasoning**, mathematically containing viral spread ($R_0 < 1$) while reducing inference latency by $>75\%$.
3. **Continuous Co-Evolution:** By continuously synchronizing sanitized production chat traces through MLflow to update our triage models, the defense maintains active immunity against mutating adversarial strategies.

* **Project Repository:** Private Git Repository (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Panel Feedback & Questions.** Thank you!
