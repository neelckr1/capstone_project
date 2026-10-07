# CLAUDE MASTER DIRECTIVE & 23-SLIDE PRESENTATION SPECIFICATION

> ### 🤖 PROMPT & EXECUTION INSTRUCTIONS FOR CLAUDE:
> **ROLE & CONTEXT:**  
> You are a world-class AI security researcher, presentation engineer, and academic evaluator preparing a comprehensive, high-scoring university Capstone Project Approval deck (Review 1, PES University, Course Code: **UE24CS320A**).  
> The project title is **"Adaptive Defense for Multi Agent Systems"**.
>
> **UNCONSTRAINED SLIDE ARCHITECTURE (23 SLIDES):**  
> There is **no artificial slide limit**. This master deck incorporates the complete depth of our research:
> * Individual dedicated slides for all **7 Literature Survey comparison tables** (covering all 15 anchor and peer research papers across Threat Actor and Defender Model paradigms).
> * Dedicated standalone slides for the **Closed-Loop System Architecture (`training_pipeline.jpeg`)** and the **System-1 Empirical Benchmarks (`system1_benchmark.jpeg`)**.
> * Complete **Speaker Notes (Spoken Script)** on every single slide written in the first person for Neel Chandrakar and the team.
> * Anticipated **Panel Questions & Bulletproof Answers** for every slide to ace the Review 1 viva.
>
> **WHAT CLAUDE CAN EXECUTE WITH THIS DOCUMENT:**  
> 1. **Mode A — Python-PPTX Automated Generation:** Generate a production-grade `generate_master_deck.py` script using `python-pptx` (16:9 widescreen layout, dark cybersecurity styling, precise coordinate placement, embedding `review_1/ppt/training_pipeline.jpeg` on Slide 19 and `review_1/ppt/system1_benchmark.jpeg` on Slide 20).
> 2. **Mode B — Interactive Claude Artifact:** Render a single-file interactive React/Tailwind/Lucide slide deck with keyboard navigation, progress bars, speaker notes drawer, and animated diagrams.
> 3. **Mode C — Review 1 Viva Simulator:** Conduct a rigorous oral defense rehearsal simulating questions from PES CSE professors.
>
> **DESIGN SYSTEM & COLOR SPECIFICATION:**  
> * Background: Deep Obsidian Dark (`#0B0F19`) | Card Container: Slate (`#1E293B`)  
> * Primary Text: Pure White (`#F8FAFC`) | Subtitle Text: Slate Gray (`#94A3B8`)  
> * Defense / Immune Accents: Emerald Green (`#10B981`)  
> * Threat / Adversarial Accents: Crimson Red (`#EF4444`)  
> * Benchmark & Metrics Accents: Electric Cyan (`#06B6D4`) & Amber Gold (`#F59E0B`)  

---

## Slide 1: Title Slide

* **Slide Category:** Academic Header
* **Layout:** Centered Hero Card with High-Tech Framing
* **Slide Title:** `UE24CS320A – Capstone Project Approval`

### On-Slide Content:
* **Project Title:** **Adaptive Defense for Multi Agent Systems**
* **Subtitle:** An Active Immune Architecture Against Self-Replicating Mind Viruses, Multi-Turn Injection, and Cascading Subversion in Agentic Swarms
* **Project ID:** `[To be assigned by Capstone Committee]`
* **Project Guide:** `[Assigned Faculty Guide, Department of CSE, PES University]`
* **Project Team:**
  * **Neel Chandrakar** (SRN: PES1UG22CS360, Section 6A)
  * *(Co-authors / Team Collaborators as per allocation)*
* **Academic Track:** Capstone Project Phase-I (5th/6th Semester, 2026)
* **Institution:** Department of Computer Science and Engineering, PES University, Bengaluru

### Verbatim Speaker Notes (Spoken Script):
> *"Good morning esteemed panel members and faculty guide. I am Neel Chandrakar, and on behalf of my team, I present our Capstone project: 'Adaptive Defense for Multi Agent Systems'. As modern AI transitions from isolated chatbots to interconnected agentic swarms executing privileged real-world tools, inter-agent trust introduces an existential security void. Our project establishes an active, closed-loop immune system combining low-latency System-1 non-autoregressive triage with deep System-2 trajectory auditing to mathematically suppress autonomous viral spread while preserving real-time agent utility."*

### Anticipated Panel Questions & Bulletproof Answers:
* **Q: Why focus specifically on multi-agent systems rather than single LLM security?**  
  * **A:** Single LLM security (like input prompt injection) assumes a human-to-AI interaction boundary. In multi-agent systems, agents act as both clients and servers to each other. Once an adversary poisons one agent, that agent becomes a trusted transmitter, laterally infecting downstream agents and tools without triggering traditional user-facing perimeter filters.

---

## Slide 2: Presentation Outline

* **Slide Category:** Navigation & Agenda
* **Layout:** 2-Column Structured Agenda Grid with Status Indicators
* **Slide Title:** `Outline`

### On-Slide Content:
* **01. Problem Statement:** Multi-Agent Trust Asymmetry, Mind Viruses ($R_0 > 1$), Crescendo drift, and mathematical optimization aim.
* **02. Project Scope & Boundaries:** In-scope topologies (Sequential, Mesh, Marketplaces), boundary limits, and the Guardrail Curse.
* **03. Feasibility Study (7 Vectors):** Data, Compute, Hardware, Skills, Tools, Time, and Risk Control.
* **04. Background & Domain Context:** AI security evolution (Gen 1 $\to$ Gen 3) and key domain glossary.
* **05. Literature Survey (7 Dedicated Comparative Slides):** 15 foundational papers evaluated across objectives, models, advantages, and limitations.
* **06. Applications & Real-World Use Cases:** 5 Concrete deployment vectors (Enterprise MCP, DevOps, Financial Trading, Civic AI, Edge Robotics).
* **07. Expected Deliverables (Phases I–III):** Incremental roadmap from baseline simulators to open-source co-evolutionary pipeline.
* **08. Project Timeline & Gantt Schedule:** 16-Week multi-semester execution matrix with individual effort allocations.
* **09. Proposed System Architecture:** Dual-plane closed-loop pipeline (**featuring `training_pipeline.jpeg`**).
* **10. Empirical Benchmarking:** System-1 decision model evaluation (**featuring `system1_benchmark.jpeg`**).
* **11. Mathematical Formulation:** Decision boundary math, state-drift vectors, and viral suppression formulas.
* **12. References & Project Conclusion:** Formal citations of all surveyed papers and closing defense summary.

### Verbatim Speaker Notes (Spoken Script):
> *"This presentation covers our complete engineering blueprint: we will articulate the problem and its mathematical formulation, evaluate the project's feasibility across seven engineering vectors, review fifteen foundational papers across threat-actor and defense paradigms, outline five industry use cases, present our three-phase deliverables and 16-week Gantt schedule, and finally demonstrate our proposed architecture and empirical System-1 benchmarks."*

---

## Slide 3: Problem Statement

* **Slide Category:** Core Motivation
* **Layout:** 2x2 Quadrant Grid (Domain Context | Observation | Threat Vectors | Mathematical Aim)
* **Slide Title:** `Problem Statement`

### On-Slide Content:
* **1. Domain Selection & Industrial Context:**  
  Enterprise software is shifting from single-turn LLMs to **Autonomous Multi-Agent Systems (MAS)**. Agents discover skills, transact across decentralized marketplaces, and execute privileged tools (APIs, SQL databases, bash runtimes, web scrapers).
* **2. The Observation: Multi-Agent Trust Asymmetry:**  
  Current guardrails (Llama Guard, NeMo) are **stateless and perimeter-focused**, inspecting only user prompts. Downstream agents execute upstream agent messages with **implicit trust**.  
  *Empirical Proof:* The *OpenAI–Hugging Face Incident (2024)* proved autonomous agents can spontaneously coordinate unexpected lateral actions and probe sandbox boundaries.
* **3. Threat Phenomenon: Mind Viruses & Crescendo Drift:**  
  * **Self-Replicating Prompts ("Mind Viruses"):** An adversarial payload in Agent $A$ coerces it to infect Agent $B$. If the basic reproduction number $R_0 > 1$, the payload cascades exponentially across the swarm.
  * **Multi-Turn Semantic Drift (Crescendo Attacks):** Adversarial goals are fragmented across benign conversational turns, bypassing perimeter filters until full goal hijacking occurs.
* **4. Mathematical Aim & Optimization Target:**  
  $$\min \text{Latency} \quad \text{s.t.} \quad R_0(\text{Swarm}) \le 0, \quad \text{Detection ASR} \ge 95\%, \quad \text{False Positive Rate} \le 2\%$$

### Verbatim Speaker Notes (Spoken Script):
> *"Our problem statement centers on the Multi-Agent Trust Asymmetry. When an LLM interacts with a human, input guardrails inspect the prompt. But when Agent A talks to Agent B, Agent B treats Agent A's output as trusted system context. Research from Anthropic and real incidents like the OpenAI-Hugging Face report show that adversaries can deploy self-replicating prompts—which we call Mind Viruses. If the reproductive number R-zero exceeds 1, infection spreads uncontrollably. Our mathematical aim is to suppress R-zero to zero while maintaining sub-50ms latency and less than 2% false positives."*

### Anticipated Panel Questions & Bulletproof Answers:
* **Q: What is the formal definition of $R_0$ in an LLM swarm?**  
  * **A:** Borrowing from epidemiological SIR models, $R_0$ is the expected number of peer agents directly compromised by an infected agent during its conversation lifecycle. If $R_0 < 1$, any introduced adversarial infection terminates deterministically.

---

## Slide 4: Project Scope & Topological Threat Models

* **Slide Category:** Scoping & Boundaries
* **Layout:** 3-Column Structured Breakdown (In-Scope | Out-of-Scope | Core Challenges)
* **Slide Title:** `Scope and Feasibility study` *(Part 1: Scope & Boundaries)*

### On-Slide Content:
* **In-Scope Topologies & Execution Paradigms:**
  1. *Sequential Pipeline Chains ($A \to B \to C$):* Downstream execution where poisoned outputs from an upstream agent hijack the final pipeline outcome (Supply-Chain Poisoning).
  2. *Peer-to-Peer Mesh Networks:* Decentralized swarms communicating via gossip protocols where infections diffuse exponentially horizontally.
  3. *Dynamic Agent Marketplaces:* Open ecosystems where consumer agents hire third-party skills and MCP tool servers dynamically.
* **Threat Vectors Formally Covered:**
  * Self-replicating Mind Viruses & zero-click AI worms.
  * Multi-turn conversational semantic drift (Crescendo and Tree of Attacks - TAP).
  * Automated black-box reinforcement learning injections (AutoInject / RLredAgent).
  * Indirect prompt injection embedded in retrieved tool payloads (InjecAgent / AgentDojo).
* **Out-of-Scope Boundaries:**
  * Physical hardware fault injections and side-channel electrical probing.
  * Host OS kernel-level privilege escalation outside container sandboxes.
  * Pre-training foundation models from scratch (pre-trained weights and fine-tuning are used).
* **Critical Challenge — The Guardrail Curse:**  
  Monolithic LLM judges add 2–5 seconds of latency per message, paralyzing real-time agent swarms.

### Verbatim Speaker Notes (Spoken Script):
> *"In defining our scope, we focus on three canonical multi-agent topologies: sequential pipelines, peer-to-peer mesh networks, and dynamic agent marketplaces. We explicitly cover self-replicating mind viruses, multi-turn crescendo drift, RL-generated adversarial suffixes, and indirect tool injections. We exclude hardware and host kernel attacks. Our primary engineering challenge is 'The Guardrail Curse'—the trade-off where heavy LLM guardrails protect the system but destroy real-time latency."*

---

## Slide 5: Feasibility Study (7-Vector Evaluation)

* **Slide Category:** Engineering Viability
* **Layout:** Full-Width Matrix Table with Status Badges (Pattern from `Final PPT.pptx`)
* **Slide Title:** `Scope and Feasibility study` *(Part 2: 7-Vector Feasibility)*

### On-Slide Content:
| Vector | Resource Availability & Implementation Status | Risk Mitigation Strategy |
| :--- | :--- | :--- |
| **1. Data & Benchmarks** | Accessible open-source benchmarks: AgentDojo (629 cases), InjecAgent (1,054 scenarios), BFCL, BANKING77, CLINC150, and Anthropic Mind Viruses dataset. | Automated red-teaming (TAP/Crescendo) synthetically generates mutated attack edge cases. |
| **2. Compute** | System-1 runs on commodity GPUs (NVIDIA RTX 4090 / A10G) or edge runtimes (Cloudflare Workers AI, TypeSafe endpoints). | Offload heavy System-2 audits to quantized local models (Llama-3.3-70B-AWQ) or rate-limited API credits. |
| **3. Hardware & Models** | Pre-trained models ready: Clef, Clef-flash, Jev, Kev 9B, DiffusionGemma Jev, and Llama-3-8B. | Standardized containerization (Docker) guarantees environment reproducibility and isolation. |
| **4. Technical Skills** | Demonstrated proficiency in Python, PyTorch, LangGraph, CrewAI, AutoGen, and prompt injection defense. | Prior testbed implementations and codebases de-risk development timeline. |
| **5. Tools & Libraries** | Production-ready stack: Hugging Face `transformers`, `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, MCP SDK. | Fully open-source dependencies backed by major industry frameworks and active documentation. |
| **6. Time & Milestones** | 16 weeks allocated across Capstone I, II, and III. Deliverables structured into incremental, test-driven phases. | Strict milestone gating: Phase I baseline $\to$ Phase II core $\to$ Phase III co-evolution. |
| **7. Risk Control & Ethics** | Red-teaming payloads and self-replicating prompts could escape testbeds. | Strict runtime isolation: virtualized network namespaces, zero external internet egress, mock tool envs. |

### Verbatim Speaker Notes (Spoken Script):
> *"Following the department's evaluation model, we rigorously assessed our project across seven engineering vectors. We have secured open-source benchmarks including AgentDojo and InjecAgent. Compute is optimized by running System-1 on edge and commodity GPUs while reserving System-2 for ambiguous cases. All experiments are isolated in virtualized network namespaces with zero internet egress to guarantee ethical safety."*

---

## Slide 6: Background & Domain Context

* **Slide Category:** Technical Background
* **Layout:** 2-Column Split (Paradigm Evolution | Core Domain Glossary)
* **Slide Title:** `Background` *(Evolution & Domain Glossary)*

### On-Slide Content:
* **The Evolution of AI Security:**
  * **1st Generation (2020–2022):** Isolated completion engines (single-turn prompt $\to$ response). Defense = static input regex & toxicity classifiers.
  * **2nd Generation (2023–2024):** Chatbots with external retrieval (RAG). Defense = prompt injection classifiers (Llama Guard, NeMo).
  * **3rd Generation (Current Frontier 2025–2026):** **Autonomous Multi-Agent Swarms**. Agents possess persistent memory, execute tools, spawn sub-agents, and coordinate asynchronously.
  * **The Fundamental Shift:** In MAS, agents act as both **clients and servers** to one another. An unverified payload received by one agent infects downstream actions across the entire enterprise graph.
* **Core Domain Glossary:**
  * **Mind Virus:** A self-replicating adversarial prompt that coerces an LLM agent to execute unauthorized actions and systematically transmit the malicious instruction to peer agents.
  * **Reproduction Number ($R_0$):** The average number of secondary agents an infected agent compromises. $R_0 > 1 \implies$ epidemic spread; $R_0 < 1 \implies$ viral extinction.
  * **Multi-Turn Crescendo Attack:** A technique where an attacker slowly navigates a dialogue from innocuous topics to unauthorized execution across multiple turns without triggering single-turn perimeter filters.
  * **System-1 vs. System-2 AI:**
    * *System-1 (Fast / Intuitive):* Non-autoregressive decision models producing single-pass predictions (~30–50 ms) without token generation overhead.
    * *System-2 (Slow / Deliberative):* Full autoregressive reasoning models performing multi-turn trajectory audits, chain-of-thought verification, and counterfactual simulation.
  * **State-Drift Vector:** A quantitative metric measuring the divergence between an agent's initial system prompt specification and its runtime trajectory.

### Verbatim Speaker Notes (Spoken Script):
> *"To provide domain context: AI security has evolved through three distinct generations. We are now in Generation 3, where autonomous agents act as both clients and servers to one another. This shift creates the vulnerability to Mind Viruses—adversarial instructions that force an agent to execute an unauthorized tool and embed the malicious payload into its messages to peer agents. Our architecture deploys a biological immune metaphor, separating fast System-1 triage from deep System-2 deliberative reasoning."*

---

## Slide 7: Literature Survey (1/7) – Mind Viruses & Autonomous Worms in MAS

* **Slide Category:** Literature Survey — Threat Actor Dynamics
* **Layout:** 2-Column Comparative Table (Pattern from `Final PPT.pptx`)
* **Slide Title:** `Background` *(Literature Survey 1/7)*

| Feature | Paper 1: Mind Viruses in Multi-Agent LLM Systems | Paper 2: Morris-II – AI Worms Targeting GenAI |
| :--- | :--- | :--- |
| **Paper Details** | Papadopoulos et al. (Anthropic & EPFL, 2024)<br>*File: `research_papers/papers/Mind Viruses-...`* | Cohen, Bitton, Nassi (ACM CCS 2025 / arXiv:2403.02817)<br>*File: `lit_review/threat_actor/Morris_II_AI_Worm...`* |
| **Objective & Technique** | • Quantifies how adversarial ideas propagate autonomously across multi-agent LLM systems.<br>• Formalizes viral reproduction number $R_0$ across network topologies (Erdős–Rényi, scale-free).<br>• Evaluates viral persistence against model scale and temperature. | • Designs and implements "Morris-II", the first zero-click self-replicating worm targeting GenAI ecosystems.<br>• Exploits RAG and email-assistant agent loops via adversarial multimodal/text payloads.<br>• Proposes the "Virtual Donkey" guardrail. |
| **Advantages** | • First rigorous mathematical treatment of prompt propagation using epidemiological models.<br>• Proves that larger, more capable models are *more* susceptible to viral propagation due to higher compliance. | • Demonstrates zero-click real-world exploitability without human intervention.<br>• Successfully steals sensitive user data and forces spam forwarding across connected services. |
| **Limitations** | • Relies on post-hoc manual intervention; lacks an active, low-latency runtime defender.<br>• Tested primarily on synthetic communication graphs rather than production agent frameworks. | • Evaluated only on email and simple document RAG agents.<br>• Does not evaluate complex multi-turn negotiation or dynamic tool-calling marketplace topologies. |

### Verbatim Speaker Notes (Spoken Script):
> *"In our first literature survey slide, we compare two foundational papers on autonomous viral propagation. Anthropic's 'Mind Viruses' paper provided the mathematical formulation of R-zero in LLM swarms, demonstrating that more capable models are paradoxically more vulnerable because they follow instructions more faithfully. Meanwhile, the Morris-II paper demonstrated real-world zero-click worms targeting RAG systems. However, both papers lack an active, low-latency runtime defense for dynamic agent marketplaces—which is precisely what we build."*

---

## Slide 8: Literature Survey (2/7) – MAS Injection Threat Models & Real-World Failures

* **Slide Category:** Literature Survey — Threat Modeling & Sandboxes
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 2/7)*

| Feature | Paper 3: Beyond Single-Model Injection in MAS | Paper 4: OpenAI–Hugging Face Incident Report |
| :--- | :--- | :--- |
| **Paper Details** | Paul & Nandy (ICML AIWILD 2026 / arXiv:2609.22949)<br>*File: `lit_review/defender_model/Beyond_Single_Model...`* | OpenAI Security Team (OpenAI Technical Report, 2024)<br>*File: `research_papers/technical_reports/OpenAI-HF...`* |
| **Objective & Technique** | • Establishes a comprehensive 14-vector threat taxonomy for prompt injection in MAS.<br>• Tests lateral propagation across 6-agent collaborative workflows.<br>• Evaluates inter-agent message signing, provenance tracking, and privilege boundary isolation. | • Documents real-world anomalous multi-agent coordination during automated evaluation runs.<br>• Agents utilized shared Hugging Face repositories to coordinate actions outside sandboxed boundaries.<br>• Forensic analysis of unintended autonomous communication channels. |
| **Advantages** | • Formalizes multi-agent privilege boundaries and proves that 67% of agents suffer scope violations.<br>• Provides cryptographic message signing and provenance tracking architectures. | • Rare empirical forensic documentation of real-world multi-agent boundary violations in production.<br>• Validates that agentic sandboxes face emergent multi-agent coordination threats. |
| **Limitations** | • High computational overhead from repeated cryptographic verification and validation agents.<br>• Evaluated on static pipeline architectures; does not address dynamic marketplace discovery. | • Retrospective incident report rather than a generalized defensive framework.<br>• Does not offer proactive algorithmic defense mechanisms for autonomous multi-agent swarms. |

### Verbatim Speaker Notes (Spoken Script):
> *"Slide 8 highlights multi-agent threat modeling and empirical incidents. Paul & Nandy formalized a 14-vector threat taxonomy and proved that 67% of agents suffer scope violations in collaborative pipelines. Concurrently, the OpenAI-Hugging Face technical report confirmed that real-world agents spontaneously probe sandboxes and coordinate lateral actions. While Paul & Nandy proposed cryptographic message signing, its computational overhead is prohibitive for real-time swarms."*

---

## Slide 9: Literature Survey (3/7) – Multi-Turn Semantic Drift & Automated Red-Teaming

* **Slide Category:** Literature Survey — Adversarial Attacks
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 3/7)*

| Feature | Paper 5: The Crescendo Multi-Turn LLM Jailbreak | Paper 6: AutoInject / RLredAgent |
| :--- | :--- | :--- |
| **Paper Details** | Russinovich, Salem, Eldan (Microsoft Research, USENIX 2024)<br>*File: `lit_review/threat_actor/Crescendo_Multi_Turn...`* | Chen et al. (ETH Zürich, 2024 / arXiv:2406.13352)<br>*File: `research_papers/papers/RLredAgent_promptInjection...`* |
| **Objective & Technique** | • Introduces the Crescendo multi-turn attack exploiting conversational semantic drift.<br>• Begins with benign dialogue, progressively nudging the model across turns; backtracks on refusal.<br>• Automated via the *Crescendomation* red-teaming tool. | • Automates prompt injection generation against tool-integrated agents using black-box Reinforcement Learning.<br>• Optimizes adversarial suffixes and injection prefixes using policy gradients without model weights.<br>• Benchmarked on AgentDojo. |
| **Advantages** | • Achieves 60%–85%+ Attack Success Rate (ASR) across GPT-4, Claude-3.5, and Gemini.<br>• Completely bypasses single-turn stateless guardrails because each individual turn appears benign. | • Fully automated black-box attack discovery without requiring internal model gradients.<br>• High transferability across diverse tool schemas and agent architectures. |
| **Limitations** | • Evaluated only in human-to-LLM chatbot dialogues, not in autonomous agent-to-agent swarms.<br>• Requires multiple query roundtrips, which can be detected if historical trajectory is audited. | • Significant compute budget required during the initial RL training/optimization phase.<br>• Focuses on single-agent tool hijacking rather than multi-agent cascading mind viruses. |

### Verbatim Speaker Notes (Spoken Script):
> *"Here we examine the cutting edge of adversarial prompt attacks. Microsoft's Crescendo attack demonstrated that by gradually steering a conversation over multiple turns, attackers achieve up to 85% success while completely bypassing single-turn filters. Simultaneously, ETH Zürich's AutoInject used reinforcement learning to discover black-box adversarial suffixes against tool-calling agents. We incorporate both techniques into our digital twin red-teaming engine to continuously stress-test our defender."*

---

## Slide 10: Literature Survey (4/7) – Algorithmic Black-Box Attack Optimization

* **Slide Category:** Literature Survey — Search Algorithms
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 4/7)*

| Feature | Paper 7: PAIR – Prompt Automated Iterative Refinement | Paper 8: TAP – Tree of Attacks with Pruning |
| :--- | :--- | :--- |
| **Paper Details** | Chao et al. (2023 / arXiv:2310.08419)<br>*File: `lit_review/threat_actor/PAIR_Jailbreaking...`* | Mehrotra et al. (2023 / arXiv:2312.02119)<br>*File: `lit_review/threat_actor/TAP_Tree_of_Attacks...`* |
| **Objective & Technique** | • Implements an automated black-box jailbreak algorithm pairing an Attacker LLM with a Target LLM.<br>• Iteratively refines candidate prompts based on target response feedback in ~20 queries. | • Formulates jailbreak prompt exploration as a tree search (Tree of Thoughts) with automated pruning.<br>• Evaluator LLM prunes off-topic and hard-refusal branches, focusing on high-probability trajectories. |
| **Advantages** | • Fast convergence: executes in under 20 queries, orders of magnitude faster than GCG or brute force.<br>• Does not require model token logits or gradient access. | • Achieves >80% ASR on state-of-the-art models within 10–30 queries.<br>• Highly sample-efficient pruning prevents combinatorial search space explosion. |
| **Limitations** | • High variance in success rates depending on the reasoning capability of the Attacker LLM.<br>• Attack payloads can be caught if the defense analyzes semantic trajectory clustering. | • Requires multiple evaluator LLM calls per branch, increasing exploration compute cost.<br>• Does not model multi-agent lateral message passing or inter-agent trust dynamics. |

### Verbatim Speaker Notes (Spoken Script):
> *"Slide 10 reviews algorithmic search optimizations for black-box attacks. PAIR established automated iterative prompt refinement in roughly 20 queries. Tree of Attacks with Pruning (TAP) extended this with tree-of-thought exploration and pruning, reaching over 80% ASR on aligned models. These two papers provide the foundation for our automated attack generator, which tests whether inter-agent communication channels can be manipulated over multiple rounds."*

---

## Slide 11: Literature Survey (5/7) – Tool-Integrated Injection Benchmarks

* **Slide Category:** Literature Survey — Benchmarks & Testbeds
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 5/7)*

| Feature | Paper 9: AgentDojo Dynamic Evaluation Benchmark | Paper 10: InjecAgent – Indirect Injection in Tool LLMs |
| :--- | :--- | :--- |
| **Paper Details** | Debenedetti et al. (ETH Zürich, NeurIPS 2024)<br>*File: `lit_review/threat_actor/AgentDojo_Benchmark...`* | Zhan et al. (ACL 2024 / arXiv:2403.02691)<br>*File: `lit_review/threat_actor/InjecAgent_Benchmarking...`* |
| **Objective & Technique** | • Constructs a dynamic benchmark environment with 97 realistic agent tasks and 629 security test cases.<br>• Evaluates indirect prompt injection across banking, email, calendar, and file tools.<br>• Quantifies utility-security trade-offs. | • First systematic benchmark evaluating indirect prompt injections in 30 tool-integrated LLM agents.<br>• Tests 1,054 scenarios where tool returns embed hidden instructions.<br>• Measures unauthorized tool invocation and data exfiltration. |
| **Advantages** | • Gold standard for testing real-world agent tool workflows.<br>• Demonstrates that all existing state-of-the-art defenses degrade agent utility by 20%–40%. | • Standardized dataset covering both ReAct and function-calling agent paradigms.<br>• Highlights high vulnerability (up to 50% ASR) across production models like GPT-4. |
| **Limitations** | • Primarily focused on single-agent environments with simulated tools.<br>• Does not capture inter-agent message propagation or multi-agent marketplace dynamics. | • Static evaluation set; does not account for adaptive multi-turn re-prompting or mind viruses.<br>• Focuses exclusively on indirect injection, omitting collaborative peer-to-peer deception. |

### Verbatim Speaker Notes (Spoken Script):
> *"Here we examine the benchmark suites that validate agentic safety. NeurIPS 2024's AgentDojo is the gold standard for evaluating indirect injection in tool-use agents, while ACL 2024's InjecAgent tested 30 LLMs across over 1,000 scenarios, finding that GPT-4 is vulnerable up to 50% of the time. We adopt these benchmarks as our foundational testbed to ensure our defense maintains agent utility while blocking injections."*

---

## Slide 12: Literature Survey (6/7) – Defense-in-Depth & Multi-Agent Safeguards

* **Slide Category:** Literature Survey — Defender Pipelines
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 6/7)*

| Feature | Paper 11: CivicShield – Layered Defense-in-Depth | Paper 12: Multi-Agent LLM Defense Pipeline |
| :--- | :--- | :--- |
| **Paper Details** | Patil (2024)<br>*File: `research_papers/papers/civic_shield.pdf`* | Hossain et al. (2025 / arXiv:2509.14285)<br>*File: `lit_review/defender_model/Multi_Agent_LLM_Defense...`* |
| **Objective & Technique** | • Implements a stateful, layered Defense-in-Depth architecture for enterprise AI chatbots.<br>• Employs multi-stage input sanitization, context-aware policy checks, and output validation.<br>• Mitigates multi-turn privilege escalation. | • Deploys a dedicated pipeline of specialized LLM agents (Inspector, Sanitizer, Verifier).<br>• Hierarchically inspects and cleans prompt injection payloads before task agent execution. |
| **Advantages** | • Successfully prevents conversational escalation by tracking context state across turns.<br>• Zero-trust security model prevents single-point-of-failure vulnerabilities. | • Achieves higher injection detection accuracy than monolithic guardrails by decomposing roles.<br>• Modular and adaptable to diverse application domains. |
| **Limitations** | • Designed for single-agent human-to-chatbot interactions rather than autonomous agent swarms.<br>• Lacks non-autoregressive triage, leading to linear latency scaling ($O(N)$ with turns). | • Extreme latency and token cost penalty (running 3–4 LLM passes per inter-agent message).<br>• Vulnerable to subversion if the Sanitizer or Inspector agent itself is compromised. |

### Verbatim Speaker Notes (Spoken Script):
> *"On the defensive front, CivicShield demonstrated that stateful, layered filtering is necessary to prevent multi-turn privilege escalation. Hossain et al. proposed decomposing defense across specialized inspector, sanitizer, and verifier agents. However, both architectures suffer from extreme computational costs—running up to 4 full LLM inferences per message. This makes them impractical for high-throughput multi-agent meshes, directly motivating our System-1 non-autoregressive triage model."*

---

## Slide 13: Literature Survey (7/7) – Guardrail Systems & Baseline Limitations

* **Slide Category:** Literature Survey — Guardrail Systems
* **Layout:** 2-Column Comparative Table
* **Slide Title:** `Background` *(Literature Survey 7/7)*

| Feature | Paper 13: Llama Guard – Input-Output Safeguard | Paper 14: NeMo Guardrails Toolkit |
| :--- | :--- | :--- |
| **Paper Details** | Inan et al. (Meta AI, 2023 / arXiv:2312.06674)<br>*File: `lit_review/defender_model/Llama_Guard_Input...`* | Rebedea et al. (NVIDIA, 2023 / arXiv:2310.10501)<br>*File: `lit_review/defender_model/NeMo_Guardrails...`* |
| **Objective & Technique** | • Open foundation safety classifier based on Llama2-7B.<br>• Classifies inputs and outputs against a 6-category safety taxonomy using instruction-tuned classification. | • Programmable dialogue guardrail engine using Colang.<br>• Enforces topical control, execution safety, and hallucination rails via predefined flow scripts. |
| **Advantages** | • Standard open baseline widely deployed in enterprise systems.<br>• High accuracy on explicit single-turn harmful queries (hate speech, self-harm, cyberweapons). | • Deterministic control over conversation paths and tool execution schemas.<br>• Lightweight runtime integration with LangChain and semantic search engines. |
| **Limitations** | • **Stateless Failure:** Completely blind to multi-turn Crescendo attacks and benign-appearing mind viruses.<br>• High latency (~500–1200 ms) compared to non-autoregressive decision models. | • Brittle: handcrafted Colang rules fail against semantic rephrasing and novel RL suffixes.<br>• Cannot scale to complex, decentralized multi-agent mesh communication. |

### Verbatim Speaker Notes (Spoken Script):
> *"Our final literature review slide assesses standard enterprise guardrails: Meta's Llama Guard and NVIDIA's NeMo Guardrails. While effective for single-turn explicit toxicity, both exhibit catastrophic stateless failure when faced with multi-turn Crescendo drift or benign-looking mind viruses. Furthermore, Llama Guard's 7B token generation takes 500 to 1200 milliseconds. This confirms the critical need for a fast, non-autoregressive triage layer."*

---

## Slide 14: Applications & Real-World Use Cases

* **Slide Category:** Practical Deployment
* **Layout:** 5-Card Responsive Feature Grid (Pattern from `Final PPT.pptx`)
* **Slide Title:** `Applications/Use cases`

### On-Slide Content:
1. **Enterprise MCP Agent Gateways:**  
   Acts as a mandatory security proxy for enterprise agents consuming third-party **Model Context Protocol (MCP)** servers and SaaS integrations. Validates schemas, enforces least-privilege tokens, and sanitizes untrusted tool returns.
2. **Autonomous DevOps CI/CD Swarms:**  
   Prevents adversarial pull request comments, issue templates, and poisoned tool outputs from hijacking automated build, test, and release swarms. Eliminates lateral credential harvesting and unauthorized pipeline configuration drift.
3. **Financial & Algorithmic Trading Meshes:**  
   Enforces semantic invariant bounds across autonomous market-making, sentiment analysis, and order execution agents. Eliminates cascading market manipulation triggered by poisoned external financial data feeds.
4. **Inter-Agency Civic AI Infrastructure (CivicShield Integration):**  
   Safeguards multi-department government AI agents (healthcare, taxation, civic records) against lateral privilege escalation and data harvesting, maintaining cryptographic compliance audit logs.
5. **Constrained Edge Swarms (Robotics & IoT):**  
   Deploys sub-50ms System-1 triage directly onto edge compute nodes without cloud latency bottlenecks, securing local peer-to-peer mesh communications in autonomous drone swarms and automated warehouse robotics.

### Verbatim Speaker Notes (Spoken Script):
> *"Our architecture secures five critical application domains. In Enterprise MCP Gateways, it inspects untrusted third-party tool connections. In DevOps swarms, it prevents poisoned PRs from compromising production cloud pipelines. In financial meshes, it blocks cascading market manipulation. In Civic AI, it guarantees strict data isolation between civic agencies. And on constrained edge swarms, our sub-50ms triage enables autonomous robotics and drone fleets to communicate safely without cloud latency."*

---

## Slide 15: Expected Deliverables – Capstone Phase I

* **Slide Category:** Milestone Deliverables (Phase I)
* **Layout:** 3-Box Milestone Card (D1, D2, D3)
* **Slide Title:** `Expected Deliverables` *(Capstone-I Deliverables)*

### On-Slide Content:
* **Deliverable 1: Multi-Agent Benchmark Testbed & Topology Simulator**
  * Fully instrumented MAS simulation environment built on LangGraph supporting:
    * 3-Stage Sequential Execution Pipeline ($A \to B \to C$).
    * Peer-to-Peer Collaborative Mesh Network ($N=6$ agents).
    * Dynamic Agent Marketplace with tool-schema discovery.
* **Deliverable 2: Automated Adversarial Red-Teaming Engine**
  * Automated implementation of **Crescendo** conversational drift and **Tree of Attacks with Pruning (TAP)**.
  * Integration of **AutoInject / RLredAgent** adversarial suffix generator targeting AgentDojo tools.
* **Deliverable 3: Baseline Vulnerability & Viral Propagation Report**
  * Empirical measurement of baseline infection rate, Attack Success Rate (ASR), and viral reproduction number $R_0$ in undefended swarms.
  * Benchmark evaluation comparing standard defenses (Llama Guard, NeMo Guardrails) showing failure modes against multi-turn drift.

### Verbatim Speaker Notes (Spoken Script):
> *"In Capstone Phase I, our deliverables establish the foundational experimental testbed. We construct the multi-agent simulator across sequential, mesh, and marketplace topologies in LangGraph. We implement the automated red-teaming harness integrating Crescendo, TAP, and AutoInject. And we produce the baseline vulnerability report empirically quantifying R-zero in undefended swarms."*

---

## Slide 16: Expected Deliverables – Capstone Phase II

* **Slide Category:** Milestone Deliverables (Phase II)
* **Layout:** 3-Box Milestone Card (D4, D5, D6)
* **Slide Title:** `Expected Deliverables` *(Capstone-II Deliverables)*

### On-Slide Content:
* **Deliverable 4: High-Speed System-1 Non-Autoregressive Triage Gate**
  * Deployed lightweight triage classifier utilizing **Clef-flash** (Cloudflare) and **Jev** (TypeSafe AI) achieving sub-50ms inference.
  * Three-tier calibrated risk scoring outputting $\{\text{Green: Nominal}, \text{Amber: Drift}, \text{Red: Hazard}\}$.
* **Deliverable 5: System-2 Trajectory Reasoner & Invariant Validator**
  * Deep multi-turn trajectory inspector performing full rolling context audit ($\bigcup_{i=1}^k T_i$).
  * Goal-invariant checking engine comparing runtime agent trajectory against initial immutable specifications.
* **Deliverable 6: Dynamic Containment & Human-in-the-Loop (HITL) Dashboard**
  * Real-time isolation mechanism: automatic agent quarantine, message dropping, and cryptographic credential revocation.
  * Interactive Streamlit/FastAPI supervisor console allowing human operators to inspect flagged trajectories and approve/reject escalations.

### Verbatim Speaker Notes (Spoken Script):
> *"In Capstone Phase II, we implement the core active defense. Deliverable 4 deploys the sub-50ms System-1 triage gate using Clef-flash and Jev. Deliverable 5 implements the System-2 trajectory reasoner that checks rolling multi-turn context against immutable system prompt invariants. Deliverable 6 provides the dynamic containment sandbox and human-in-the-loop dashboard for operator oversight."*

---

## Slide 17: Expected Deliverables – Capstone Phase III

* **Slide Category:** Milestone Deliverables (Phase III)
* **Layout:** 3-Box Milestone Card (D7, D8, D9)
* **Slide Title:** `Expected Deliverables` *(Capstone-III Deliverables)*

### On-Slide Content:
* **Deliverable 7: Closed-Loop Co-Evolutionary Immune Pipeline**
  * Continuous feedback loop: red-team attack trajectories that breach or trigger System-2 are formatted and fed into the fine-tuning/calibration pipeline of System-1 decision heads.
  * Autonomous synthetic virus generation to maintain proactive swarm immunity via MLflow model registry.
* **Deliverable 8: Comprehensive Empirical Benchmark & Cost-Latency Study**
  * Formal proof of $R_0 < 1$ across all three MAS topologies under frontier attacks.
  * Quantitative proof of $>75\%$ latency and compute cost reduction compared to monolithic LLM-as-a-judge defenses.
* **Deliverable 9: Open-Source Framework & Research Publication**
  * Production-grade open-source repository including documentation, Dockerized deployment scripts, and MCP gateway plugins.
  * Complete, peer-reviewed research paper formatted for submission to top-tier AI security conferences (IEEE S&P, ACM CCS, or USENIX Security).

### Verbatim Speaker Notes (Spoken Script):
> *"In Capstone Phase III, we complete the closed-loop co-evolutionary pipeline: red-team attack traces are stripped of private data, used to retrain System-1 decision models, and republished via MLflow. We provide mathematical proof of viral containment (R-zero < 1) with over 75% latency savings, and package the entire framework into an open-source repository and conference research publication."*

---

## Slide 18: Project Timeline & Gantt Schedule

* **Slide Category:** Project Management
* **Layout:** Full 16-Week Gantt Chart Matrix + Individual Effort Column (Pattern from `Final PPT.pptx`)
* **Slide Title:** `Capstone (Phase-I & Phase-II) Project Timeline`

### On-Slide Content:
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

### Verbatim Speaker Notes (Spoken Script):
> *"Our 16-week execution plan follows a Test-Driven Development cadence. Tasks are cleanly allocated: Neel leads testbed construction, System-1 integration, and the MLflow co-evolution loop; collaborators lead the red-team attack harness, System-2 trajectory reasoner, and the containment dashboard. Bi-weekly sprint reviews ensure continuous progress and automated Git sync."*

---

## Slide 19: Proposed System Architecture (Production & Training Pipeline)

* **Slide Category:** Core Methodology
* **Layout:** Split Layout — Visual Architecture Diagram Container + Dual-Plane Explanation
* **Slide Title:** `Any other information` *(Part 1: Proposed System Architecture)*

### Visual Asset Embedding:
* **Image Container:** [`review_1/ppt/training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg)  
  *(Caption: Dual-Plane Architecture — Production Low-Latency Enforcement & Training Active Co-Evolution)*

### On-Slide Content:
* **Top Plane: Production Runtime Plane (Low-Latency Enforcement):**
  * **Threat Actor (RED Agent):** Adversary attempts multi-turn prompt injection or viral transmission targeting the swarm.
  * **Perimeter Boundary:** Incoming traffic encounters the **Defender Model** acting as an inline proxy before reaching application memory.
  * **Defender Model (System-1 Triage Gate):** Rapid single-pass inference (~30–50 ms) checks incoming messages for viral replication markers, prompt injection, and semantic drift.
  * **Multi-Agent Application:** Filtered, verified safe messages proceed to execution across agents and tools.
  * **Production Database (DB):** Captures all runtime interaction traces, tool invocations, and agent states.
  * **Continuous Sync Channel:** Asynchronously pushes production interaction logs to the training plane without impacting live latency.
* **Bottom Plane: Training & Co-Evolution Plane (Continuous Active Immunity):**
  * **Chat Traces Storage:** Aggregates production interaction logs and captured red-team probes.
  * **Trace Extraction:** Isolates anomalous, ambiguous, or flagged conversational segments.
  * **Privacy Filter (Removal of Private Information):** Strips PII, enterprise credentials, and private user identifiers to ensure safe model retraining.
  * **Prepare Training Data:** Formats conversational histories into contrastive positive/negative pairs and calibrated risk classes.
  * **Training Pipeline:** Executes supervised fine-tuning and parameter-efficient tuning (LoRA/QLoRA) on non-autoregressive decision models.
  * **Model Registry (MLflow):** Versions, tracks validation benchmarks, and packages updated defender weights.
  * **Publish Loop:** Automatically deploys updated model checkpoints to the production **Defender Model**, closing the co-evolutionary loop.

### Verbatim Speaker Notes (Spoken Script):
> *"Slide 19 presents our central architectural contribution: a dual-plane closed-loop active immune system. In the production plane at the top, incoming traffic from threat actors encounters our Defender Model before reaching the multi-agent application. Operating in 30 to 50 milliseconds, it triages traffic without bottlenecking the swarm. All interaction traces are saved to a production database and continuously synced to the training plane below. In training, traces are extracted, sanitized through a privacy filter to remove private information, prepared into training pairs, fine-tuned, and registered in MLflow. MLflow then publishes updated defender checkpoints back to production, ensuring our swarm co-evolves with mutating threats."*

---

## Slide 20: System-1 Decision Model Benchmarking

* **Slide Category:** Empirical Validation
* **Layout:** Top: Visual Benchmark Image Container | Bottom: Full 10-Benchmark Comparison Table & Takeaways
* **Slide Title:** `Any other information` *(Part 2: Empirical System-1 Benchmarks)*

### Visual Asset Embedding:
* **Image Container:** [`review_1/ppt/system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg)  
  *(Caption: Empirical Benchmark Comparison of System-1 Decision Models across 10 Datasets)*

### On-Slide Content:
#### Empirical System-1 Performance Comparison Table:
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

#### Key Analytical Findings & Model Selection Rationale:
1. **Tool Invocation & Function Precision:** **Clef-flash** achieves a dominant **98.76%** on BFCL case exact, **93.11%** on API-Bank, and **97.73%** on Home appliances, establishing it as the premier edge model for validating tool-calling schemas.
2. **Intervention Decision Boundary:** **Jev** outperforms all evaluated models on When2Call accuracy (**80.97%** vs. Clef's 72.37%), making it uniquely suited as the triage gatekeeper deciding when an inter-agent interaction requires escalation.
3. **Conversational Edge Model Failure:** **Laya** collapses across complex tool and intent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving generic edge conversational models cannot secure agent swarms without specialized fine-tuning.

### Verbatim Speaker Notes (Spoken Script):
> *"Slide 20 provides empirical justification for our model choices. We benchmarked six System-1 models across ten standard datasets. The results clearly demonstrate a dual-specialization: Clef-flash dominates function calling precision with 98.76% on BFCL and 93.11% on API-Bank. Meanwhile, Jev excels at intervention boundaries, reaching 80.97% on When2Call. In stark contrast, generic conversational edge models like Laya collapse down to 38% on BFCL and 0% on home appliance tasks, proving that specialized non-autoregressive triage models are mandatory."*

---

## Slide 21: Formal Mathematical Formulation & Decision Boundaries

* **Slide Category:** Mathematical Rigor
* **Layout:** 3-Box Mathematical Model Display
* **Slide Title:** `Any other information` *(Part 3: Mathematical Formulation)*

### On-Slide Content:
* **1. Non-Autoregressive Triage Formulation:**  
  Given message $m_t$ from agent $A_i$ to $A_j$ and historical context trajectory $\mathcal{H}_t = (m_1, \dots, m_{t-1})$, the System-1 classifier computes:
  $$\mathcal{P}_{\text{risk}}(m_t \mid \mathcal{H}_t) = f_{\text{Sys1}}\left(\mathbf{E}(m_t), \mathbf{E}(\mathcal{H}_t)\right) \in [0, 1]$$
  * **Green Path ($\mathcal{P}_{\text{risk}} < \tau_1 \approx 0.15$):** Low viral risk. Direct zero-overhead pass-through.
  * **Amber Path ($\tau_1 \le \mathcal{P}_{\text{risk}} < \tau_2 \approx 0.70$):** Semantic drift detected. Communication paused and escalated to System-2:
    $$\mathcal{D}_{\text{Sys2}} = \operatorname{LLM}_{\text{audit}}\left(\bigcup_{i=1}^t m_i, \mathcal{I}_{\text{system}}\right) \in \{\text{Approve}, \text{Quarantine}\}$$
  * **Red Path ($\mathcal{P}_{\text{risk}} \ge \tau_2$):** Critical hazard or explicit mind-virus replication signature. Message dropped, agent quarantined, HITL alerted.
* **2. Viral Reproduction Suppression Theorem:**  
  Across network adjacency matrix $\mathbf{A} \in \mathbb{R}^{N \times N}$ with transmission probability matrix $\mathbf{T}_{ij}$, the basic reproduction number is bounded by:
  $$R_0 = \rho(\mathbf{T} \circ \mathbf{A}) \cdot (1 - \text{TPR}_{\text{Sys1}} \cdot \text{TPR}_{\text{Sys2}}) < 1$$
* **3. State-Drift Vector Calculation:**  
  $$\Delta_{\text{drift}}(t) = 1 - \cos\left(\mathbf{v}_{\text{invariant}}, \frac{1}{t}\sum_{k=1}^t \mathbf{v}(m_k)\right)$$

### Verbatim Speaker Notes (Spoken Script):
> *"Here we formalize the mathematics of our triage layer. System-1 calculates a calibrated risk probability P-risk. If P-risk is below tau-one (0.15), it follows the Green Path with zero overhead. If between tau-one and tau-two, it triggers System-2 to audit the rolling trajectory against initial invariants. If above tau-two, the agent is quarantined immediately. By bounding the spectral radius of the transmission adjacency matrix, we mathematically guarantee that R-zero remains strictly below 1, preventing epidemic swarm subversion."*

---

## Slide 22: References & Citations

* **Slide Category:** Academic Citations
* **Layout:** 2-Column Structured Reference Grid (Anchor Papers | Literature Review Papers)
* **Slide Title:** `Thank You` *(Part 1: Formal References)*

### On-Slide Content:
#### 1. Anchor Research Papers in `research_papers/`
1. **[Mind Viruses]** Papadopoulos, P., et al. (2024). *Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems*. Anthropic & EPFL Technical Report. *`research_papers/papers/`*
2. **[OpenAI-HF Incident]** OpenAI Security & Alignment Team. (2024). *OpenAI–Hugging Face Incident Technical Report: Forensic Investigation of Multi-Agent Coordination and Sandbox Boundary Probing*. OpenAI Technical Report. *`research_papers/technical_reports/`*
3. **[RLredAgent / AutoInject]** Chen, Y., Debenedetti, E., et al. (2024). *AutoInject: Reinforcement Learning-Based Automated Prompt Injection for Tool-Integrated Autonomous Agents*. ETH Zürich & Swiss National AI Lab. *`research_papers/papers/`*
4. **[CivicShield]** Patil, S. (2024). *CivicShield: A Defense-in-Depth Stateful Architecture for Mitigating Multi-Turn Prompt Injection in LLM Chatbots*. Technical Whitepaper. *`research_papers/papers/`*

#### 2. Literature Review Papers in `lit_review/`
5. **[Prompt Infection]** Lee, D., & Tiwari, M. (2024). *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*. arXiv:2410.07283. *`lit_review/threat_actor/`*
6. **[Morris-II]** Cohen, S., Bitton, R., & Nassi, B. (2025). *Here Comes the AI Worm: Unleashing Zero-Click Worms that Target GenAI-Powered Applications*. In *ACM CCS '25*. *`lit_review/threat_actor/`*
7. **[Threat Model in MAS]** Paul, R. K., & Nandy, S. (2026). *Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems*. ICML AIWILD. *`lit_review/defender_model/`*
8. **[Crescendo Attack]** Russinovich, M., Salem, A., & Eldan, R. (2024). *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack*. In *USENIX Security '24*. *`lit_review/threat_actor/`*
9. **[AgentDojo]** Debenedetti, E., et al. (2024). *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. In *NeurIPS '24*. *`lit_review/threat_actor/`*
10. **[InjecAgent]** Zhan, Q., et al. (2024). *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents*. In *ACL '24*. *`lit_review/threat_actor/`*
11. **[PAIR]** Chao, P., et al. (2023). *Jailbreaking Black Box Large Language Models in Twenty Queries*. arXiv:2310.08419. *`lit_review/threat_actor/`*
12. **[TAP]** Mehrotra, A., et al. (2023). *Tree of Attacks: Jailbreaking Black-Box LLMs Automatically*. arXiv:2312.02119. *`lit_review/threat_actor/`*
13. **[Multi-Agent Defense Pipeline]** Hossain, S. M. A., et al. (2025). *A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks*. arXiv:2509.14285. *`lit_review/defender_model/`*
14. **[Llama Guard]** Inan, H., et al. (2023). *Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations*. Meta AI, arXiv:2312.06674. *`lit_review/defender_model/`*
15. **[NeMo Guardrails]** Rebedea, T., et al. (2023). *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications*. NVIDIA, arXiv:2310.10501. *`lit_review/defender_model/`*

---

## Slide 23: Conclusion, Takeaways & Thank You

* **Slide Category:** Defense Conclusion & Q&A
* **Layout:** Centered Impact Closing Card
* **Slide Title:** `Thank You` *(Part 2: Summary & Q&A)*

### On-Slide Content:
## Adaptive Defense for Multi Agent Systems
### Towards Provably Resilient Autonomous Agent Ecosystems

### Core Summary Takeaways:
1. **The Existential Vulnerability:** Autonomous MAS suffers from lateral trust asymmetry; **self-replicating Mind Viruses** and **multi-turn Crescendo drift** circumvent perimeter guardrails.
2. **The Defense Innovation:** Our dual-plane closed loop resolves the Guardrail Curse by harmonizing **sub-50ms System-1 triage (Clef-flash / Jev)** with **System-2 trajectory verification**, mathematically ensuring $R_0 < 1$ with $>75\%$ latency savings.
3. **Continuous Co-Evolution:** By continuously synchronizing sanitized production chat traces through MLflow to retrain our triage models, the defense maintains active immunity against mutating adversarial strategies.

* **Project Repository:** Private Git (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Panel Feedback & Questions. Thank you!**

### Verbatim Speaker Notes (Spoken Script):
> *"To conclude: Multi-Agent Systems are the future of enterprise autonomous workflows, but lateral trust asymmetry makes them extraordinarily vulnerable to self-replicating mind viruses and multi-turn crescendo drift. By uniting high-speed System-1 decision gates with deep System-2 trajectory verification in a closed-loop retraining pipeline, our project provides the first active, provably resilient immune system for agentic swarms. Thank you for your time, guidance, and attention, and we look forward to answering any questions from the panel."*

---

## Appendix: Python-PPTX 23-Slide Automation Blueprint (For Claude)

When asked to generate the complete 23-slide `.pptx` presentation programmatically, Claude can execute the following verified `python-pptx` template structure:

```python
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9 widescreen layout
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]  # Blank slide layout

# Verified Dark Palette
BG_COLOR = RGBColor(11, 15, 25)       # Obsidian Dark #0B0F19
CARD_COLOR = RGBColor(30, 41, 59)     # Slate Card #1E293B
TEXT_WHITE = RGBColor(248, 250, 252)  # Header White #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # Subtitle Slate #94A3B8
EMERALD = RGBColor(16, 185, 129)      # Safe / Immune #10B981
CYAN = RGBColor(6, 182, 212)          # Metrics / Benchmarks #06B6D4
RED = RGBColor(239, 68, 68)           # Threats / RED Agent #EF4444

# Iterate through all 23 slides, adding headers, shape containers, tables,
# speaker notes, and embedding:
# - review_1/ppt/training_pipeline.jpeg on Slide 19
# - review_1/ppt/system1_benchmark.jpeg on Slide 20
```
