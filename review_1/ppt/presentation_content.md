# GAMMA AI DIRECTIVE & INSTRUCTION SET (STRICT SAMPLE.PPTX COMPLIANCE)

> ### 🤖 PROMPT & CONFIGURATION INSTRUCTIONS FOR GAMMA AI:
> **ROLE & CONTEXT:**  
> You are an elite academic AI presentation designer building a university Capstone Project Approval deck (Review 1, PES University, Course Code: **UE24CS320A**).  
> The project title is **"Adaptive Defense for Multi Agent Systems"**.
>
> **STRICT TEMPLATE & CARDINALITY COMPLIANCE:**
> * **Exact 10 Slides (Cards):** This presentation strictly mirrors the official 10-slide PES University template ([`sample.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/sample.pptx)) and complies with the **Gamma Free 10-slide limit**.
> * **Exact Slide Headers:** Slide headers must exactly match `sample.pptx`:
>   1. `UE24CS320A – Capstone Project Approval`
>   2. `Outline`
>   3. `Problem Statement`
>   4. `Scope and Feasibility study`
>   5. `Background`
>   6. `Applications/Use cases`
>   7. `Expected Deliverables`
>   8. `Capstone (Phase-I & Phase-II) Project Timeline`
>   9. `Any other information`
>   10. `Thank You`
>
> **VISUAL STYLING & MEDIA DIRECTIVES:**
> * **Theme:** **Dark Mode / Cybersecurity Academic** (Charcoal/navy slate background, crisp white typography, Emerald Green for defense/safe states, Crimson Red for threats, Electric Cyan for data/benchmarks).
> * **Images on Card 9 (CRITICAL):** Card 9 (`Any other information`) houses:
>   1. `[UPLOAD IMAGE: training_pipeline.jpeg]` (Dual-Plane Closed Loop Architecture)
>   2. `[UPLOAD IMAGE: system1_benchmark.jpeg]` (Empirical System-1 Benchmark Table)
> * **Data Integrity:** Render all comparative tables, deliverables, timeline grids, and formulas ($R_0 < 1$, $\mathcal{P}_{\text{risk}}$) intact.

---

# Card 1: Title Slide

[Layout: Centered Hero Card | Theme: Cybersecurity Dark]

## UE24CS320A – Capstone Project Approval
# Project Title: Adaptive Defense for Multi Agent Systems
### An Active Immune Architecture Against Self-Replicating Mind Viruses, Multi-Turn Injection, and Cascading Subversion in Agentic Swarms

* **Project ID:** *(To be assigned by Capstone Committee)*
* **Project Guide:** *(Assigned Faculty Guide, Department of CSE, PES University)*
* **Project Team:**
  * **Neel Chandrakar** (SRN: PES1UG22CS360, Section 6A)
  * *(Co-authors / Team Collaborators as per allocation)*
* **Domain:** AI Security | Multi-Agent Systems (MAS) | Adversarial Robustness | LLM Safety
* **Institution:** Department of Computer Science and Engineering, PES University, Bengaluru

---

# Card 2: Outline

[Layout: 2-Column Agenda List | Exact sample.pptx Structure]

### Agenda

* **• Problem Statement** (Domain selection, observation of trust asymmetry, Mind Viruses $R_0 > 1$, mathematical aim)
* **• Scope and Feasibility study** (Topological boundaries, Guardrail Curse, and 7-vector feasibility evaluation)
* **• Background work** (Evolution of agentic autonomy, domain concepts, and 15-paper comparative literature survey)
* **• Applications/Use cases** (5 Concrete deployment vectors across enterprise MCP, DevOps, finance, and edge swarms)
* **• Expected Deliverables** (Structured breakdown across Capstone-I, Capstone-II, and Capstone-III)
* **• Capstone (Phase-I Phase-II, Phase-III) Project Timeline** (16-Week Gantt chart, stage tasks, individual efforts)
* **• Any other information** (Closed-loop architecture `training_pipeline.jpeg` & empirical benchmarks `system1_benchmark.jpeg`)
* **• References & Closing** (Formal IEEE/ACM citations of surveyed papers)

---

# Card 3: Problem Statement

[Layout: 2x2 Grid Card Layout | sample.pptx Prompt: Well defined problem statement specifying the problem clearly]

### 1. Domain Selection & Industrial Context
* Modern enterprise AI is transitioning from isolated LLMs to **Autonomous Multi-Agent Systems (MAS)** collaborating across marketplaces, mesh networks, and execution pipelines.
* Agents autonomously execute privileged tools (APIs, databases, bash environments, web scrapers) and recruit third-party sub-agents.

### 2. Observation: The Multi-Agent Trust Asymmetry
* Existing LLM guardrails (Llama Guard, NeMo) are **stateless and perimeter-focused**, inspecting only human-to-AI boundaries.
* Downstream agents implicitly trust upstream agent outputs as legitimate system context, creating an unmonitored **lateral attack vector**.
* Real-world incident: *OpenAI–Hugging Face Incident (2024)* proved interacting agents spontaneously coordinate anomalous actions and probe sandboxes.

### 3. The Core Threat: Mind Viruses & Multi-Turn Drift
* **Self-Replicating Prompts ("Mind Viruses"):** An adversarial payload injected into Agent $A$ coerces it to infect Agent $B$. If reproduction number $R_0 > 1$, the payload cascades exponentially across the swarm.
* **Semantic Drift (Crescendo Attacks):** Malicious intent is distributed across benign conversational turns, bypassing perimeter filters until full subversion occurs.

### 4. Mathematical Project Aim
* Design and empirically benchmark an **Adaptive Active Defense Architecture** that establishes an automated immune system for MAS:
  $$\min \text{Latency} \quad \text{s.t.} \quad R_0(\text{Swarm}) \le 0, \quad \text{Detection ASR} \ge 95\%, \quad \text{False Positive Rate} \le 2\%$$

---

# Card 4: Scope and Feasibility study

[Layout: 2-Column Split | sample.pptx Prompts: Overview of scope + Possible Shortcomings/Challenges & Feasibility]

### Overview of Project Scope & Challenges
* **In-Scope Topologies:**
  1. *Sequential Chains ($A \to B \to C$):* Supply-chain cumulative poisoning.
  2. *Peer Mesh Networks:* Horizontal epidemic diffusion via gossip protocols.
  3. *Agent Marketplaces:* Third-party untrusted tool and skill integration.
* **Threat Vectors Covered:** Mind Viruses ($R_0$), Crescendo multi-turn drift, TAP decision-tree attacks, AutoInject RL suffixes, and InjecAgent indirect injections.
* **Out-of-Scope:** Hardware-level side-channel attacks, OS kernel exploits, pre-training foundation LLMs from scratch.
* **Shortcomings & Challenges (The Guardrail Curse):** Monolithic LLM judges add 2–5s latency per inter-agent message, paralyzing real-time agent swarms.

### Feasibility Study for Solving This Problem (7 Vectors)
| Feasibility Vector | Status & Resource Availability | Risk Control Strategy |
| :--- | :--- | :--- |
| **1. Data & Benchmarks** | Open datasets: AgentDojo (629 cases), InjecAgent (1,054), BFCL, Anthropic dataset. | Automated red-teaming (TAP/Crescendo) generates synthetic edge cases. |
| **2. Compute** | System-1 runs on commodity GPUs / edge APIs (Cloudflare Workers, TypeSafe endpoints). | Offload heavy System-2 audits to local quantized models (Llama-3.3-70B-AWQ). |
| **3. Hardware & Models** | Pre-trained models available: Clef, Clef-flash, Jev, Kev 9B, Llama-3-8B. | Isolated containerization (Docker) ensures reproducibility. |
| **4. Skills** | Established team proficiency in Python, PyTorch, LangGraph, agent state machines. | Prior testbed implementations mitigate development risks. |
| **5. Tools & Libraries** | Stack: `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, MCP SDK. | Fully open-source dependencies with enterprise backing. |
| **6. Time & Milestones** | 16 weeks structured across Capstone I, II, and III with bi-weekly milestones. | Strict phase gating: Phase I baseline $\to$ Phase II core $\to$ Phase III co-evolution. |
| **7. Risk Control** | Red-teaming payloads and self-replicating prompts could escape testbeds. | Virtualized network namespaces, zero external internet egress, mock tool envs. |

---

# Card 5: Background

[Layout: Top: Domain Evolution & Context | Bottom: Consolidated Literature Review Table]

### Why This Problem & Domain Context
* **Why This Problem:** Shift from Gen 1 (isolated chatbots) to Gen 3 (**Autonomous Multi-Agent Swarms**). Agents are both clients and servers to one another; an unverified payload received by one agent infects downstream actions across the entire enterprise graph.
* **Domain Context:** Multi-Agent Systems (MAS), Self-Replicating Memes / Mind Viruses ($R_0$), Multi-Turn Semantic Drift (Crescendo), and Non-Autoregressive System-1 vs. Autoregressive System-2 Triage.

### Consolidated Literature Review (15 Anchor & Peer Papers)
| Research Domain | Key Papers & Citations | Core Techniques / Models | Advantages | Critical Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Viral Propagation & Worms (Threat Actor)** | • Mind Viruses *(Anthropic 2024)*<br>• Morris-II AI Worm *(ACM CCS 2025)*<br>• Prompt Infection *(Lee & Tiwari 2024)* | Epidemiological $R_0$ modeling in MAS; Zero-click RAG/email worm injection payloads. | Mathematical proof that larger models are more susceptible; real-world exploit proof. | Lacks active runtime defense; tested only on synthetic graphs or email tools. |
| **Multi-Turn Red Teaming (Threat Actor)** | • Crescendo *(USENIX 2024)*<br>• AutoInject / RLredAgent *(ETH 2024)*<br>• TAP & PAIR *(Chao 2023, Mehrotra 2023)* | Conversational semantic drift; Black-box RL policy gradients; Tree-of-Attacks with pruning. | 60%–85%+ ASR bypassing single-turn filters; fully automated adversarial suffix discovery. | High optimization compute; does not model multi-agent lateral message passing. |
| **Agent Benchmarks (Testbeds)** | • AgentDojo *(NeurIPS 2024)*<br>• InjecAgent *(ACL 2024)* | 97 dynamic agent tasks & 629 security test cases; 1,054 indirect injection scenarios. | Gold standard for tool-use evaluation; quantifies utility-security trade-offs. | Single-agent evaluation; omits multi-agent peer-to-peer deception. |
| **Defense-in-Depth & Pipelines (Defender)** | • CivicShield *(Patil 2024)*<br>• Multi-Agent Defense *(Hossain 2025)*<br>• Beyond Single-Model *(ICML 2026)* | Stateful layered filtering; Hierarchical Inspector/Sanitizer agents; Message signing. | Zero-trust context tracking; role decomposition beats monolithic guardrails. | Extreme latency penalty (3–4 LLM calls/message); vulnerable if sanitizer is hijacked. |
| **Stateless Baselines (Guardrails)** | • Llama Guard *(Meta 2023)*<br>• NeMo Guardrails *(NVIDIA 2023)* | Instruction-tuned 7B safety classifier; Colang programmable dialogue rails. | Industry standard open baselines; deterministic execution safety rules. | **Stateless Failure:** Blind to multi-turn Crescendo drift & benign mind viruses; high latency. |

---

# Card 6: Applications/Use cases

[Layout: 5 Visual Cards Grid | sample.pptx Prompt: Describe applications and use cases of your project]

### 1. Enterprise MCP Agent Gateways
* Acts as a non-bypassable security proxy for enterprise agents consuming third-party **Model Context Protocol (MCP)** servers and SaaS connectors.
* Validates schemas, enforces least-privilege tokens, and sanitizes untrusted tool returns.

### 2. Autonomous DevOps CI/CD Swarms
* Prevents adversarial pull request comments, issue templates, and poisoned tool outputs from hijacking automated build, test, and release swarms.
* Eliminates lateral credential harvesting and unauthorized infrastructure configuration drift.

### 3. Financial & Algorithmic Trading Meshes
* Enforces semantic invariant bounds across autonomous market-making, sentiment analysis, and order execution agents.
* Eliminates cascading market manipulation triggered by poisoned external financial data feeds.

### 4. Inter-Agency Civic AI Infrastructure (CivicShield Integration)
* Safeguards multi-department government AI agents (healthcare, taxation, civic records) against lateral privilege escalation.
* Maintains verifiable cryptographic audit trails for compliance with public data regulations.

### 5. Constrained Edge Swarms (Robotics & IoT)
* Deploys sub-50ms System-1 triage directly onto edge compute nodes without cloud latency bottlenecks.
* Secures local peer-to-peer mesh communications in autonomous drone swarms and automated warehouse robotics.

---

# Card 7: Expected Deliverables

[Layout: 3-Column Milestone Cards | sample.pptx Prompts: Capstone-I, Capstone-II, Capstone-III deliverables]

### Capstone-I deliverables (Current Phase)
* **D1: Multi-Agent Benchmark Testbed:** Instrumented simulation environment built on LangGraph supporting Sequential, Mesh ($N=6$), and Dynamic Marketplace topologies.
* **D2: Automated Adversarial Red-Team Engine:** Implementation of Crescendo drift, Tree of Attacks (TAP), and AutoInject RL suffixes.
* **D3: Baseline Vulnerability Report:** Empirical measurement of baseline infection rate, ASR, and $R_0$ in undefended swarms vs. perimeter guardrail baselines.

### Capstone-II deliverables (Next Phase)
* **D4: High-Speed System-1 Triage Gate:** Lightweight non-autoregressive classifier (**Clef-flash / Jev**) achieving sub-50ms inference and calibrated risk scoring.
* **D5: System-2 Trajectory Reasoner:** Multi-turn trajectory auditor ($\bigcup_{i=1}^k T_i$) and goal-invariant checker against initial immutable specifications.
* **D6: Dynamic Containment & HITL Dashboard:** Real-time isolation mechanism (agent quarantine, message dropping, credential revocation) and Streamlit supervisor console.

### Capstone-III deliverables (Final Phase)
* **D7: Closed-Loop Co-Evolutionary Pipeline:** Continuous retraining of System-1 decision heads using production chat traces via MLflow model registry.
* **D8: Full Empirical Benchmark Study:** Formal proof of $R_0 < 1$ across all topologies with $>75\%$ latency and compute cost reduction over LLM judges.
* **D9: Open-Source Release & Research Paper:** Production-ready GitHub repository, Dockerized deployment scripts, and peer-reviewed conference publication.

---

# Card 8: Capstone (Phase-I & Phase-II) Project Timeline

[Layout: Gantt Schedule Table + Responsibility Matrix | sample.pptx Prompts: Timelines, Gantt chart, Individual efforts, Tasks in stages]

| Stage & Task Description | W1-2 | W3-4 | W5-6 | W7-8 | W9-10 | W11-12 | W13-14 | W15-16 | Individual Effort Allocation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Stage 1: Threat Modeling & Lit Taxonomy** | █ | | | | | | | | All Members (Baseline Research) |
| **Stage 2: MAS Topology Testbed (LangGraph)** | | █ | | | | | | | Neel Chandrakar (Testbed Architecture) |
| **Stage 3: Automated Red-Team Engine (TAP)** | | | █ | | | | | | Team Collaborators (Attack Harness) |
| **Stage 4: System-1 Triage Gate (Clef/Jev)** | | | | █ | | | | | Neel Chandrakar (Model Integration) |
| **Stage 5: System-2 Trajectory Reasoner** | | | | | █ | | | | Team Collaborators (Reasoning Logic) |
| **Stage 6: Quarantine & HITL Dashboard** | | | | | | █ | | | Team Collaborators (UI & Containment) |
| **Stage 7: Co-Evolutionary Loop (MLflow)** | | | | | | | █ | | Neel Chandrakar (Training Pipeline) |
| **Stage 8: Final Benchmarks, Validation & Paper** | | | | | | | | █ | All Members (Dissemination & Defense) |

* **Execution Plan:** Test-Driven Development (TDD) with bi-weekly sprint reviews and automated collaborative Git synchronization.

---

# Card 9: Any other information

[Layout: 2-Column Split | sample.pptx Prompt: Provide any other information you wish to add on]

> ### 📢 DIRECT SLIDE INSTRUCTIONS FOR GAMMA AI / PPT BUILDER:
> 1. **Left Container:** Embed [`training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg)  
>    `[INSERT_IMAGE: review_1/ppt/training_pipeline.jpeg]`
> 2. **Right Container:** Embed [`system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg)  
>    `[INSERT_IMAGE: review_1/ppt/system1_benchmark.jpeg]`

### 1. Proposed Architecture: Closed-Loop Active Defense Pipeline (`training_pipeline.jpeg`)
* **Production Runtime Plane:** Threat Actor (RED Agent) $\to$ **Defender Model (System-1 Triage)** inspects traffic in ~30–50ms $\to$ safe messages reach **Multi-Agent Application** $\to$ execution logs saved to **DB** $\to$ synced to training plane.
* **Training & Co-Evolution Plane:** Chat Traces $\to$ Trace Extraction $\to$ **Privacy Filter (Removal of PII)** $\to$ Prepare Training Data $\to$ Model Retraining $\to$ **Model Registry (MLflow)** $\to$ **Publish** updated weights back to Defender Model.

### 2. Empirical System-1 Benchmarks & Key Insights (`system1_benchmark.jpeg`)
* **Tool Invocation Precision:** **Clef-flash** dominates with **98.76%** on BFCL exact-case and **93.11%** on API-Bank, establishing it as the premier edge gate for validating tool schemas.
* **Intervention Boundary:** **Jev** leads on When2Call accuracy (**80.97%** vs. Clef's 72.37%), uniquely qualifying it to decide when interactions require System-2 escalation.
* **Conversational Edge Collapse:** **Laya** fails on complex agent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving generic edge conversational models cannot secure agent swarms without specialized tuning.

---

# Card 10: Thank You

[Layout: 2-Column Split | sample.pptx Closing Slide]

### Formal References & Citations
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
* **The Vulnerability:** Autonomous MAS suffers from lateral trust asymmetry; Mind Viruses ($R_0 > 1$) and multi-turn Crescendo drift bypass perimeter defenses.
* **The Solution:** Our dual-plane closed loop balances **sub-50ms System-1 triage** with **System-2 trajectory verification**, mathematically ensuring $R_0 < 1$ with $>75\%$ cost reduction.
* **Active Co-Evolution:** Continuous retraining via MLflow guarantees persistent resilience against mutating adversarial strategies.

* **Project Repository:** Private Git (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Panel Feedback & Questions. Thank you!**
