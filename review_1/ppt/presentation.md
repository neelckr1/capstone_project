# GAMMA AI DIRECTIVE & INSTRUCTION SET (10-SLIDE STRICT LIMIT)

> ### 🤖 PROMPT & CONFIGURATION INSTRUCTIONS FOR GAMMA AI:
> **ROLE & CONTEXT:**  
> You are an elite AI presentation designer building an academic and technical defense deck for a university Capstone Project Approval (Review 1, PES University, Course Code: **UE24CS320A**).  
> The project title is **"Adaptive Defense for Multi Agent Systems"**.
>
> **CRITICAL SLIDE COUNT CONSTRAINT:**
> * **Exactly 10 Slides (Cards):** This document is strictly budgeted for **Gamma Free (10 cards max)** and complies 1-to-1 with the official PES University template ([`sample.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/sample.pptx)).
> * **Card Cardinality:** Generate exactly **10 distinct cards**, separated by `---`. Do not create fewer or more cards.
>
> **VISUAL STYLING & LAYOUT:**
> * **Theme:** **Dark Mode / Cybersecurity Academic** (Charcoal/navy slate background, crisp white typography, Emerald Green for defense/safe states, Crimson Red for threats, Electric Cyan for data/benchmarks).
> * **Native Tables & Multi-Columns:** Render all tables with clean header rows. Use 2-column or grid layouts where indicated.
> * **Visual Assets & Images (CRITICAL FOR CARD 9):**
>   * Card 9 combines the **System Architecture Diagram** and the **System-1 Benchmark**:
>     1. Media Block 1: `[UPLOAD IMAGE: training_pipeline.jpeg]` (Closed-Loop Production vs. Training Architecture).
>     2. Media Block 2: `[UPLOAD IMAGE: system1_benchmark.jpeg]` (10-Benchmark Empirical Validation).
> * **Preserve Math & Scientific Metrics:** Preserve all formulas ($R_0 < 1$, $\mathcal{P}_{\text{risk}}$, $\tau_1, \tau_2$) and empirical percentage values verbatim.

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

[Layout: 2-Column Agenda with Accent Badges]

### Agenda & Evaluation Vectors

* **01. Problem Statement & Mathematical Aim:** Paradigm shift to MAS, lateral trust asymmetry, Mind Viruses ($R_0 > 1$), and optimization target.
* **02. Scope & 7-Vector Feasibility Study:** Topological boundaries (Sequential, Mesh, Marketplaces), Guardrail Curse, and feasibility matrix.
* **03. Background & Consolidated Literature Survey:** Evolution from chatbots to agentic swarms + 15-paper comparative synthesis.
* **04. Applications & Real-World Use Cases:** 5 Concrete deployment vectors (Enterprise MCP, DevOps, Financial Trading, Civic AI, Edge Robotics).
* **05. Expected Deliverables (Phases I–III):** Incremental roadmap from baseline simulators to open-source co-evolutionary pipeline.
* **06. Project Timeline & Gantt Schedule:** 16-Week multi-semester execution matrix with individual effort allocations.
* **07. Proposed Architecture & System-1 Benchmarks:** Dual-plane closed-loop pipeline (**with `training_pipeline.jpeg`**) & empirical evaluation (**with `system1_benchmark.jpeg`**).
* **08. References & Project Conclusion:** Formal citations of all surveyed papers and closing defense summary.

---

# Card 3: Problem Statement

[Layout: 2x2 Grid Card Layout]

### 1. Industrial Context & Paradigm Shift
* Enterprise AI is transitioning from isolated LLMs to **Autonomous Multi-Agent Systems (MAS)** collaborating across marketplaces, mesh networks, and tool execution pipelines.
* Agents execute privileged tools (APIs, databases, bash shells, web browsing) and dynamically recruit third-party sub-agents.

### 2. The Observation: Multi-Agent Trust Asymmetry
* Existing LLM guardrails (Llama Guard, NeMo) are **stateless and perimeter-focused**, inspecting only human-to-AI boundaries.
* Downstream agents implicitly trust upstream agent messages as verified system context, opening an unmonitored **lateral attack vector**.
* Real-world incident: *OpenAI–Hugging Face Incident (2024)* proved interacting agents coordinate anomalous lateral actions and probe sandboxes.

### 3. Threat Phenomenon: Mind Viruses & Crescendo Drift
* **Self-Replicating Prompts ("Mind Viruses"):** An adversarial payload injected into Agent $A$ forces it to infect Agent $B$. If reproduction number $R_0 > 1$, infection cascades exponentially across the swarm.
* **Multi-Turn Semantic Drift (Crescendo Attacks):** Malicious intent is distributed across benign-looking conversational turns, evading perimeter filters until full subversion occurs.

### 4. Mathematical Project Aim
* Build an **Adaptive Active Defense Architecture** providing an automated immune system for MAS.
* **Optimization Target:**
  $$\min \text{Latency} \quad \text{s.t.} \quad R_0(\text{Swarm}) \le 0, \quad \text{Detection ASR} \ge 95\%, \quad \text{False Positive Rate} \le 2\%$$

---

# Card 4: Scope & Feasibility Study (7-Vector Evaluation)

[Layout: 2-Column Split | Left: Project Scope | Right: Feasibility Matrix]

### Project Scope & Boundaries
* **In-Scope Topologies:**
  1. *Sequential Chains ($A \to B \to C$):* Supply-chain cumulative poisoning.
  2. *Peer Mesh Networks:* Horizontal epidemic diffusion via gossip protocols.
  3. *Agent Marketplaces:* Third-party untrusted tool and skill integration.
* **Threats Covered:** Mind Viruses ($R_0$), Crescendo multi-turn drift, TAP decision-tree attacks, AutoInject RL suffixes, and InjecAgent indirect injections.
* **Out-of-Scope:** Hardware fault attacks, OS kernel exploits, pre-training LLMs from scratch.
* **The Guardrail Curse:** Heavy LLM judges introduce 2–5s latency per message, paralyzing real-time agent swarms.

### 7-Vector Feasibility Study (Final PPT Model)
| Vector | Resource Availability & Feasibility Status |
| :--- | :--- |
| **1. Data** | Open benchmarks: AgentDojo (629 cases), InjecAgent (1,054), BFCL, Anthropic dataset. |
| **2. Compute** | System-1 runs on commodity GPUs / edge APIs (Cloudflare, TypeSafe); local quantized System-2. |
| **3. Hardware** | Pre-trained models ready: Clef, Clef-flash, Jev, Kev 9B, Llama-3-8B. Isolated via Docker. |
| **4. Skills** | Established team proficiency in Python, PyTorch, LangGraph, agent state machines. |
| **5. Tools** | Stack: `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, Model Context Protocol (MCP). |
| **6. Time** | 16-week structured multi-semester timeline with bi-weekly test-driven milestones. |
| **7. Risk Control** | Strict virtualized network namespaces, zero external internet egress, mock tool environments. |

---

# Card 5: Background & Consolidated Literature Survey

[Layout: Top: Domain Background | Bottom: Comparative Literature Table]

### Background: Evolution of AI Security
* **Gen 1 (2020–22):** Isolated completion engines $\to$ static regex & toxicity filters.
* **Gen 2 (2023–24):** Retrieval chatbots (RAG) $\to$ perimeter injection classifiers (Llama Guard).
* **Gen 3 (Current Frontier 2025–26):** **Autonomous Multi-Agent Swarms** acting as both clients and servers to each other, creating cascading lateral vulnerabilities.

### Consolidated Comparative Literature Review (15 Anchor & Peer Papers)
| Research Pillar | Key Papers & Citations | Core Techniques / Models | Advantages | Critical Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Viral Propagation & Worms (Threat Actor)** | • Mind Viruses *(Anthropic 2024)*<br>• Morris-II AI Worm *(ACM CCS 2025)*<br>• Prompt Infection *(Lee & Tiwari 2024)* | Epidemiological $R_0$ modeling in MAS; Zero-click RAG/email worm injection payloads. | Mathematical proof that larger models are more susceptible; real-world exploit proof. | Lacks active runtime defense; tested only on synthetic graphs or email tools. |
| **Multi-Turn Red Teaming (Threat Actor)** | • Crescendo *(USENIX 2024)*<br>• AutoInject / RLredAgent *(ETH 2024)*<br>• TAP & PAIR *(Chao 2023, Mehrotra 2023)* | Conversational semantic drift; Black-box RL policy gradients; Tree-of-Attacks with pruning. | 60%–85%+ ASR bypassing single-turn filters; fully automated adversarial suffix discovery. | High optimization compute; does not model multi-agent lateral message passing. |
| **Agent Benchmarks (Testbeds)** | • AgentDojo *(NeurIPS 2024)*<br>• InjecAgent *(ACL 2024)* | 97 dynamic agent tasks & 629 security test cases; 1,054 indirect injection scenarios. | Gold standard for tool-use evaluation; quantifies utility-security trade-offs. | Single-agent evaluation; omits multi-agent peer-to-peer deception. |
| **Defense-in-Depth & Pipelines (Defender)** | • CivicShield *(Patil 2024)*<br>• Multi-Agent Defense *(Hossain 2025)*<br>• Beyond Single-Model *(ICML 2026)* | Stateful layered filtering; Hierarchical Inspector/Sanitizer agents; Message signing. | Zero-trust context tracking; role decomposition beats monolithic guardrails. | Extreme latency penalty (3–4 LLM calls/message); vulnerable if sanitizer is hijacked. |
| **Stateless Baselines (Guardrails)** | • Llama Guard *(Meta 2023)*<br>• NeMo Guardrails *(NVIDIA 2023)* | Instruction-tuned 7B safety classifier; Colang programmable dialogue rails. | Industry standard open baselines; deterministic execution safety rules. | **Stateless Failure:** Blind to multi-turn Crescendo drift & benign mind viruses; high latency. |

---

# Card 6: Applications & Real-World Use Cases

[Layout: 5 Visual Feature Cards Grid | Pattern: Final PPT]

### 1. Enterprise MCP Agent Gateways
* Mandatory security proxy for enterprise agents consuming third-party **Model Context Protocol (MCP)** servers and SaaS integrations.
* Validates schemas, enforces least-privilege tokens, and sanitizes untrusted tool returns.

### 2. Autonomous DevOps CI/CD Swarms
* Prevents adversarial pull request comments, issues, and tool outputs from hijacking automated test, build, and cloud release swarms.
* Blocks lateral credential harvesting and unauthorized pipeline modifications.

### 3. Financial & Algorithmic Trading Meshes
* Enforces semantic invariant bounds across autonomous market-making, sentiment analysis, and order routing agents.
* Eliminates cascading market manipulation triggered by poisoned external financial data feeds.

### 4. Inter-Agency Civic AI Infrastructure (CivicShield Integration)
* Safeguards multi-department government AI agents (healthcare, taxation, civic records) against lateral privilege escalation.
* Maintains verifiable cryptographic audit trails for compliance with public privacy regulations.

### 5. Constrained Edge Swarms (Robotics & IoT)
* Deploys sub-50ms System-1 triage directly onto edge compute nodes without cloud latency bottlenecks.
* Secures local peer-to-peer mesh communications in autonomous drone swarms and automated warehouse robotics.

---

# Card 7: Expected Deliverables (Phases I, II, and III)

[Layout: 3-Column Milestone Cards | Pattern: Final PPT]

### Capstone Phase I (Review 1 & 2)
* **D1: MAS Topology Testbed:** Simulation environment (LangGraph) supporting Sequential, Mesh ($N=6$), and Dynamic Marketplace topologies.
* **D2: Automated Red-Team Engine:** Implementation of Crescendo drift, Tree of Attacks (TAP), and AutoInject RL suffixes.
* **D3: Baseline Vulnerability Report:** Empirical measurement of baseline infection rate, ASR, and $R_0$ in undefended swarms vs. perimeter baselines.

### Capstone Phase II (Capstone II)
* **D4: System-1 Triage Gate:** High-speed non-autoregressive classifier (**Clef-flash / Jev**) achieving sub-50ms inference and calibrated risk scoring.
* **D5: System-2 Trajectory Reasoner:** Multi-turn trajectory auditor ($\bigcup_{i=1}^k T_i$) and goal-invariant checker against initial specifications.
* **D6: Dynamic Containment & HITL:** Real-time quarantine sandbox, credential revocation, and interactive Streamlit supervisor console.

### Capstone Phase III (Capstone III)
* **D7: Closed-Loop Co-Evolution:** Continuous feedback loop retraining System-1 decision heads using MLflow model registry.
* **D8: Full Empirical Benchmark:** Proof of $R_0 < 1$ across all topologies with $>75\%$ latency/cost reduction over LLM judges.
* **D9: Open-Source Release & Paper:** Production-ready GitHub repository, Dockerized deployment, and conference research publication.

---

# Card 8: Project Timeline & Gantt Schedule

[Layout: Gantt Schedule Table + Responsibility Matrix | Pattern: Final PPT]

| Phase & Milestone Tasks | W1-2 | W3-4 | W5-6 | W7-8 | W9-10 | W11-12 | W13-14 | W15-16 | Team Effort Allocation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Threat Modeling & Lit Taxonomy** | █ | | | | | | | | All Members (Foundation) |
| **2. MAS Topology Simulator (LangGraph)** | | █ | | | | | | | Neel Chandrakar (Lead) |
| **3. Automated Red-Team Engine (TAP)** | | | █ | | | | | | Team Collaborators |
| **4. System-1 Triage Gate (Clef/Jev)** | | | | █ | | | | | Neel Chandrakar (Lead) |
| **5. System-2 Trajectory Reasoner** | | | | | █ | | | | Team Collaborators |
| **6. Quarantine & HITL Dashboard** | | | | | | █ | | | Team Collaborators |
| **7. Co-Evolutionary Loop (MLflow)** | | | | | | | █ | | Neel Chandrakar (Lead) |
| **8. Benchmarks, Validation & Paper** | | | | | | | | █ | All Members (Publication) |

* **Execution Methodology:** Test-Driven Development (TDD) with bi-weekly sprint reviews; automated CI/CD synchronization via GitHub repository.

---

# Card 9: Proposed Architecture & Empirical System-1 Benchmarks

[Layout: 2-Column Visual Media Card | Left: Architecture | Right: Benchmark & Metrics]

> ### 📢 DIRECT SLIDE INSTRUCTIONS FOR GAMMA AI / PPT BUILDER:
> 1. **Left Container:** Embed [`training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg)  
>    `[INSERT_IMAGE: review_1/ppt/training_pipeline.jpeg]`
> 2. **Right Container:** Embed [`system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg)  
>    `[INSERT_IMAGE: review_1/ppt/system1_benchmark.jpeg]`

### 1. Dual-Plane Active Defense Architecture (`training_pipeline.jpeg`)
* **Production Runtime Plane:** Threat Actor (RED Agent) $\to$ **Defender Model (System-1 Triage)** inspects traffic in ~30–50ms $\to$ safe messages reach **Multi-Agent Application** $\to$ execution logs saved to **DB** $\to$ synced to training plane.
* **Training & Co-Evolution Plane:** Chat Traces $\to$ Trace Extraction $\to$ **Privacy Filter (Removal of PII)** $\to$ Prepare Training Data $\to$ Model Retraining $\to$ **Model Registry (MLflow)** $\to$ **Publish** updated weights back to Defender Model.

### 2. Empirical Benchmark Takeaways (`system1_benchmark.jpeg`)
* **Tool Invocation Precision:** **Clef-flash** dominates with **98.76%** on BFCL exact-case and **93.11%** on API-Bank, making it the premier edge gate for validating tool schemas.
* **Intervention Boundary:** **Jev** leads on When2Call accuracy (**80.97%** vs. Clef's 72.37%), uniquely qualifying it to decide when interactions require System-2 escalation.
* **Conversational Edge Collapse:** **Laya** fails on complex agent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving generic edge conversational models cannot secure agent swarms without specialized tuning.

---

# Card 10: References, Conclusion & Thank You

[Layout: 2-Column Split | Left: References | Right: Summary & Closing]

### Formal References (Anchor & Peer Papers)
1. **[Mind Viruses]** Papadopoulos et al. (Anthropic & EPFL, 2024). *`research_papers/papers/`*
2. **[OpenAI-HF Incident]** OpenAI Security Team. (OpenAI Technical Report, 2024). *`research_papers/technical_reports/`*
3. **[AutoInject / RLredAgent]** Chen, Debenedetti, et al. (ETH Zürich, 2024). *`research_papers/papers/`*
4. **[CivicShield]** Patil, S. (Technical Whitepaper, 2024). *`research_papers/papers/`*
5. **[Prompt Infection]** Lee & Tiwari. (arXiv:2410.07283, 2024). *`lit_review/threat_actor/`*
6. **[Morris-II AI Worm]** Cohen, Bitton, Nassi. (ACM CCS '25, 2025). *`lit_review/threat_actor/`*
7. **[Threat Model in MAS]** Paul & Nandy. (ICML AIWILD, 2026). *`lit_review/defender_model/`*
8. **[Crescendo Attack]** Russinovich, Salem, Eldan. (USENIX Security, 2024). *`lit_review/threat_actor/`*
9. **[AgentDojo]** Debenedetti et al. (NeurIPS, 2024). *`lit_review/threat_actor/`*
10. **[InjecAgent]** Zhan et al. (ACL, 2024). *`lit_review/threat_actor/`*
11. **[TAP & PAIR]** Mehrotra et al. (2023) & Chao et al. (2023). *`lit_review/threat_actor/`*
12. **[Multi-Agent Defense Pipeline]** Hossain et al. (arXiv:2509.14285, 2025). *`lit_review/defender_model/`*
13. **[Llama Guard & NeMo]** Inan et al. (Meta, 2023) & Rebedea et al. (NVIDIA, 2023). *`lit_review/defender_model/`*

### Project Summary & Takeaways
* **The Threat:** Autonomous MAS suffers from lateral trust asymmetry; Mind Viruses ($R_0 > 1$) and multi-turn Crescendo drift bypass perimeter defenses.
* **The Solution:** Our dual-plane closed loop balances **sub-50ms System-1 triage** with **System-2 trajectory verification**, mathematically ensuring $R_0 < 1$ with $>75\%$ cost reduction.
* **Active Co-Evolution:** Continuous retraining via MLflow guarantees persistent resilience against mutating adversarial strategies.

* **Repository:** Private Git (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Panel Questions.** Thank you!
