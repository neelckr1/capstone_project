# CLAUDE DIRECTIVE & COMPLETE PRESENTATION SPECIFICATION

> ### 🤖 PROMPT & EXECUTION INSTRUCTIONS FOR CLAUDE:
> **ROLE & CONTEXT:**  
> You are a world-class AI security researcher, presentation engineer, and academic evaluator preparing a high-stakes university Capstone Project Approval presentation (Review 1, PES University, Course Code: **UE24CS320A**).  
> The project title is **"Adaptive Defense for Multi Agent Systems"**.
>
> **WHAT CLAUDE SHOULD DO WITH THIS DOCUMENT:**  
> When the user prompts you with this document, you can execute any of the following requested modes:
> 1. **Mode A — Python-PPTX Generation:** Generate a complete, ready-to-execute `generate_deck.py` script using `python-pptx` (16:9 widescreen layout, dark cybersecurity palette, exact coordinate placement for text boxes, tables, and images from `review_1/ppt/training_pipeline.jpeg` and `review_1/ppt/system1_benchmark.jpeg`).
> 2. **Mode B — Interactive Claude Artifact (React / HTML / Tailwind / Reveal.js):** Render an interactive, beautifully animated single-file slide deck component with keyboard navigation, dark mode styling, and custom SVG diagrams.
> 3. **Mode C — Review 1 Oral Defense Rehearsal:** Act as the PES University evaluation panel, conduct a mock viva, or generate detailed speaker notes and defense strategies.
>
> **TEMPLATE COMPLIANCE DIRECTIVE:**  
> This deck strictly mirrors the 10-slide PES University template ([`sample.pptx`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/sample.pptx)) with the exact slide titles and prompts:
> 1. `UE24CS320A – Capstone Project Approval` (Title Slide)
> 2. `Outline`
> 3. `Problem Statement`
> 4. `Scope and Feasibility study`
> 5. `Background` (Why this problem, Domain context, Literature Survey)
> 6. `Applications/Use cases`
> 7. `Expected Deliverables` (Capstone-I, Capstone-II, Capstone-III)
> 8. `Capstone (Phase-I & Phase-II) Project Timeline` (Gantt chart, tasks, individual efforts)
> 9. `Any other information` (Architecture diagram `training_pipeline.jpeg` & System-1 benchmarks `system1_benchmark.jpeg`)
> 10. `Thank You` (References & Closing)
>
> **DESIGN SYSTEM & COLOR PALETTE:**  
> * Background: Deep Slate Dark (`#0B0F19`) / Card Slate (`#1E293B`)  
> * Primary Typography: Clean White (`#F8FAFC`) / Subtitle Gray (`#94A3B8`)  
> * Defensive / Safe Accents: Emerald Green (`#10B981`)  
> * Threat / Adversarial Accents: Crimson Red (`#EF4444`)  
> * Metrics & Highlights: Electric Cyan (`#06B6D4`) & Amber (`#F59E0B`)  

---

## Slide 1: Title Slide

* **Slide Title:** `UE24CS320A – Capstone Project Approval`
* **Layout:** Centered hero layout with high-contrast cybersecurity framing.

### On-Slide Content:
* **Project Title:** **Adaptive Defense for Multi Agent Systems**
* **Subtitle:** An Active Immune Architecture Against Self-Replicating Mind Viruses, Multi-Turn Injection, and Cascading Subversion in Agentic Swarms
* **Project ID:** `[To be assigned by Capstone Committee]`
* **Project Guide:** `[Assigned Faculty Guide, Department of CSE, PES University]`
* **Project Team:**
  * **Neel Chandrakar** (SRN: PES1UG22CS360, Section 6A)
  * *(Co-authors / Team Collaborators as per allocation)*
* **Academic Track:** Capstone Project Phase-I (5th/6th Semester)
* **Institution:** Department of Computer Science and Engineering, PES University, Bengaluru

### Verbatim Speaker Notes (Spoken Script):
> *"Good morning esteemed panel members. I am Neel Chandrakar, and today we present our Capstone project: 'Adaptive Defense for Multi Agent Systems'. As modern AI transitions from isolated chatbots to interconnected agentic swarms executing privileged real-world tools, inter-agent trust introduces an existential security void. Our project establishes an active, closed-loop immune system combining low-latency System-1 non-autoregressive triage with deep System-2 trajectory auditing to mathematically suppress autonomous viral spread while preserving real-time agent utility."*

### Anticipated Panel Questions & Bulletproof Answers:
* **Q: Why focus specifically on multi-agent systems rather than single LLM security?**  
  * **A:** Single LLM security (like input prompt injection) assumes a human-to-AI interaction boundary. In multi-agent systems, agents act as both clients and servers to each other. Once an adversary poisons one agent, that agent becomes a trusted transmitter, laterally infecting downstream agents and tools without triggering traditional user-facing perimeter filters.

---

## Slide 2: Outline

* **Slide Title:** `Outline`
* **Layout:** 2-Column structured agenda grid with accent status indicators.

### On-Slide Content:
1. **Problem Statement:** Shift to MAS, lateral trust asymmetry, Mind Viruses ($R_0 > 1$), Crescendo drift, and mathematical optimization aim.
2. **Scope and Feasibility study:** Topologies in-scope (Sequential, Mesh, Marketplaces), Guardrail Curse, and the 7-Vector Feasibility Matrix.
3. **Background work:** Evolution of agentic autonomy (Gen 1 $\to$ Gen 3) and consolidated 15-paper comparative literature survey.
4. **Applications/Use cases:** 5 Concrete deployment vectors (Enterprise MCP, DevOps, Financial Trading, Civic AI, Edge Robotics).
5. **Expected Deliverables:** Phased milestone deliverables across Capstone-I, Capstone-II, and Capstone-III.
6. **Capstone (Phase-I & Phase-II) Project Timeline:** 16-Week execution Gantt matrix with individual team effort allocations.
7. **Any other information:** Dual-plane architecture (`training_pipeline.jpeg`) and empirical System-1 benchmarks (`system1_benchmark.jpeg`).
8. **References & Closing:** Comprehensive formal citations and defense summary.

### Verbatim Speaker Notes (Spoken Script):
> *"This presentation follows the official department structure: we will articulate the problem and its mathematical formulation, evaluate the project's feasibility across seven engineering vectors, review fifteen foundational papers across threat-actor and defense paradigms, outline five industry use cases, present our three-phase deliverables and 16-week Gantt schedule, and finally demonstrate our proposed architecture and empirical System-1 benchmarks."*

---

## Slide 3: Problem Statement

* **Slide Title:** `Problem Statement`
* **Layout:** 2x2 Quadrant Grid (Domain Context | Observation | Threat Vectors | Mathematical Aim).

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

## Slide 4: Scope and Feasibility study

* **Slide Title:** `Scope and Feasibility study`
* **Layout:** 2-Column Split (Left: Scope & Challenges | Right: 7-Vector Feasibility Table).

### On-Slide Content:
#### Column 1: Scope & Technical Challenges
* **In-Scope Topologies:**
  1. *Sequential Pipelines ($A \to B \to C$):* Supply-chain cumulative poisoning.
  2. *Peer-to-Peer Mesh Networks:* Horizontal epidemic diffusion via gossip protocols.
  3. *Dynamic Marketplaces:* Third-party untrusted tools and skill integrations.
* **Threat Vectors Mitigated:** Mind Viruses ($R_0$), Crescendo multi-turn drift, TAP decision trees, AutoInject RL suffixes, and InjecAgent indirect tool injections.
* **Out-of-Scope:** Physical hardware side-channels, OS kernel exploits, and training foundation LLMs from scratch.
* **The Guardrail Curse:** Heavy LLM-as-a-judge classifiers introduce 2–5 seconds of latency per message, rendering real-time swarms unusable.

#### Column 2: 7-Vector Feasibility Study
| Vector | Resource Availability & Implementation Status | Risk Mitigation Strategy |
| :--- | :--- | :--- |
| **1. Data** | AgentDojo (629 cases), InjecAgent (1,054), BFCL, Anthropic Mind Viruses dataset. | Automated red-teaming (TAP/Crescendo) generates synthetic edge cases. |
| **2. Compute** | System-1 runs on commodity GPUs / edge runtimes (Cloudflare, TypeSafe endpoints). | Offload deep System-2 trajectory audits to quantized local models (AWQ). |
| **3. Hardware** | Pre-trained models ready: Clef, Clef-flash, Jev, Kev 9B, Llama-3-8B. | Standardized Docker containers guarantee reproducible testbed isolation. |
| **4. Skills** | Demonstrated proficiency in Python, PyTorch, LangGraph, agent state machines. | Prior testbed implementations de-risk development timeline. |
| **5. Tools** | Stack: `vLLM`, `AgentDojo`, `NeMo-Guardrails`, `FastAPI`, `Streamlit`, MCP SDK. | Fully open-source dependencies backed by major industry frameworks. |
| **6. Time** | 16-week multi-semester timeline with bi-weekly test-driven milestones. | Strict phase gating: Phase I baseline $\to$ Phase II core $\to$ Phase III co-evolution. |
| **7. Risk Control** | Red-teaming payloads and self-replicating prompts could escape testbeds. | Virtualized network namespaces, zero external internet egress, mock tool envs. |

### Verbatim Speaker Notes (Spoken Script):
> *"To ensure academic and engineering rigor, we evaluated our project against seven feasibility vectors. We have confirmed access to standard benchmarks like AgentDojo and InjecAgent. Crucially, we overcome 'The Guardrail Curse'—where heavy LLM judges introduce 2 to 5 seconds of latency—by deploying non-autoregressive System-1 decision engines that execute in 30 to 50 milliseconds. All experiments run in isolated Docker containers with zero external internet egress to prevent live payload escape."*

---

## Slide 5: Background

* **Slide Title:** `Background`
* **Layout:** Top Header (Why this problem & Domain Context) + Bottom Consolidated Literature Survey Table.

### On-Slide Content:
* **Why This Problem:** Evolution from Gen 1 (isolated chatbots) to Gen 3 (**Autonomous Multi-Agent Swarms**). Agents are both clients and servers to one another; an unverified payload received by one agent infects downstream actions across the entire enterprise graph.
* **Domain Context:** Multi-Agent Systems (MAS), Self-Replicating Memes / Mind Viruses ($R_0$), Multi-Turn Semantic Drift (Crescendo), and Non-Autoregressive System-1 vs. Autoregressive System-2 Triage.

#### Consolidated Literature Review (15 Anchor & Peer Papers)
| Research Pillar | Key Papers & Citations | Core Techniques / Models | Advantages | Critical Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Viral Propagation & Worms (Threat Actor)** | • Mind Viruses *(Anthropic 2024)*<br>• Morris-II AI Worm *(ACM CCS 2025)*<br>• Prompt Infection *(Lee & Tiwari 2024)* | Epidemiological $R_0$ modeling in MAS; Zero-click RAG/email worm injection payloads. | Mathematical proof that larger models are more susceptible; real-world exploit proof. | Lacks active runtime defense; tested only on synthetic graphs or email tools. |
| **Multi-Turn Red Teaming (Threat Actor)** | • Crescendo *(USENIX 2024)*<br>• AutoInject / RLredAgent *(ETH 2024)*<br>• TAP & PAIR *(Chao 2023, Mehrotra 2023)* | Conversational semantic drift; Black-box RL policy gradients; Tree-of-Attacks with pruning. | 60%–85%+ ASR bypassing single-turn filters; fully automated adversarial suffix discovery. | High optimization compute; does not model multi-agent lateral message passing. |
| **Agent Benchmarks (Testbeds)** | • AgentDojo *(NeurIPS 2024)*<br>• InjecAgent *(ACL 2024)* | 97 dynamic agent tasks & 629 security test cases; 1,054 indirect injection scenarios. | Gold standard for tool-use evaluation; quantifies utility-security trade-offs. | Single-agent evaluation; omits multi-agent peer-to-peer deception. |
| **Defense-in-Depth & Pipelines (Defender)** | • CivicShield *(Patil 2024)*<br>• Multi-Agent Defense *(Hossain 2025)*<br>• Beyond Single-Model *(ICML 2026)* | Stateful layered filtering; Hierarchical Inspector/Sanitizer agents; Message signing. | Zero-trust context tracking; role decomposition beats monolithic guardrails. | Extreme latency penalty (3–4 LLM calls/message); vulnerable if sanitizer is hijacked. |
| **Stateless Baselines (Guardrails)** | • Llama Guard *(Meta 2023)*<br>• NeMo Guardrails *(NVIDIA 2023)* | Instruction-tuned 7B safety classifier; Colang programmable dialogue rails. | Industry standard open baselines; deterministic execution safety rules. | **Stateless Failure:** Blind to multi-turn Crescendo drift & benign mind viruses; high latency. |

### Verbatim Speaker Notes (Spoken Script):
> *"In our background analysis, we synthesized fifteen foundational papers across two distinct categories: Threat Actors and Defender Models. On the threat side, Anthropic's Mind Viruses and the Morris-II worm proved that self-replicating prompts can compromise entire agent ecosystems. On the defense side, prior work like CivicShield and multi-agent defense pipelines introduced layered filtering, but suffered from severe latency penalties of up to 4 LLM calls per message. This highlights the gap our project addresses: providing low-latency, active multi-agent defense."*

---

## Slide 6: Applications/Use cases

* **Slide Title:** `Applications/Use cases`
* **Layout:** 5-Card Responsive Grid with Visual Icons / Badges.

### On-Slide Content:
1. **Enterprise MCP Agent Gateways:**  
   Acts as a mandatory security proxy for enterprise agents consuming third-party **Model Context Protocol (MCP)** servers and SaaS integrations. Validates tool schemas, enforces least-privilege tokens, and sanitizes untrusted tool returns.
2. **Autonomous DevOps CI/CD Swarms:**  
   Prevents adversarial pull request comments, issue templates, and poisoned tool outputs from hijacking automated build, test, and release swarms. Eliminates lateral credential harvesting and unauthorized pipeline configuration drift.
3. **Financial & Algorithmic Trading Meshes:**  
   Enforces semantic invariant bounds across autonomous market-making, sentiment analysis, and order execution agents. Eliminates cascading market manipulation triggered by poisoned external financial data feeds.
4. **Inter-Agency Civic AI Infrastructure (CivicShield Integration):**  
   Safeguards multi-department government AI agents (healthcare, taxation, civic records) against lateral privilege escalation and data harvesting, maintaining cryptographic compliance audit logs.
5. **Constrained Edge Swarms (Robotics & IoT):**  
   Deploys sub-50ms System-1 triage directly onto edge compute nodes without cloud latency bottlenecks, securing local peer-to-peer mesh communications in autonomous drone swarms and automated warehouse robotics.

### Verbatim Speaker Notes (Spoken Script):
> *"Our architecture addresses five high-impact industrial applications. First, Enterprise MCP Gateways, securing Model Context Protocol connections against poisoned third-party tools. Second, Autonomous DevOps swarms, preventing poisoned PRs from hijacking cloud build pipelines. Third, Algorithmic Trading meshes, protecting multi-agent financial systems against cascading manipulation. Fourth, Civic AI, ensuring cross-agency government chatbots maintain strict isolation. And fifth, Constrained Edge Swarms, where lightweight sub-50ms decision models protect autonomous drone and robotic fleets without relying on the cloud."*

---

## Slide 7: Expected Deliverables

* **Slide Title:** `Expected Deliverables`
* **Layout:** 3-Column Milestone Cards (Capstone-I | Capstone-II | Capstone-III).

### On-Slide Content:
#### Capstone-I deliverables (Current Phase)
* **D1: Multi-Agent Benchmark Testbed:** Instrumented simulation environment built on LangGraph supporting Sequential, Mesh ($N=6$), and Dynamic Marketplace topologies.
* **D2: Automated Adversarial Red-Team Engine:** Implementation of Crescendo drift, Tree of Attacks (TAP), and AutoInject RL suffixes.
* **D3: Baseline Vulnerability Report:** Empirical measurement of baseline infection rate, ASR, and $R_0$ in undefended swarms vs. perimeter guardrail baselines.

#### Capstone-II deliverables (Next Phase)
* **D4: High-Speed System-1 Triage Gate:** Lightweight non-autoregressive classifier (**Clef-flash / Jev**) achieving sub-50ms inference and calibrated risk scoring.
* **D5: System-2 Trajectory Reasoner:** Multi-turn trajectory auditor ($\bigcup_{i=1}^k T_i$) and goal-invariant checker against initial immutable specifications.
* **D6: Dynamic Containment & HITL Dashboard:** Real-time isolation mechanism (agent quarantine, message dropping, credential revocation) and Streamlit supervisor console.

#### Capstone-III deliverables (Final Phase)
* **D7: Closed-Loop Co-Evolutionary Pipeline:** Continuous retraining of System-1 decision heads using production chat traces via MLflow model registry.
* **D8: Full Empirical Benchmark Study:** Formal proof of $R_0 < 1$ across all topologies with $>75\%$ latency and compute cost reduction over LLM judges.
* **D9: Open-Source Release & Research Paper:** Production-ready GitHub repository, Dockerized deployment scripts, and peer-reviewed conference publication.

### Verbatim Speaker Notes (Spoken Script):
> *"Our project deliverables are structured across all three Capstone phases. In Capstone-I, we deliver the multi-agent testbeds, the automated red-teaming harness, and baseline vulnerability benchmarks. In Capstone-II, we deploy the core defense: our sub-50ms System-1 triage gate, the System-2 trajectory auditor, and the human-in-the-loop quarantine dashboard. In Capstone-III, we connect the closed-loop co-evolutionary pipeline via MLflow, prove mathematical viral suppression (R-zero < 1), and publish our open-source codebase and research paper."*

---

## Slide 8: Capstone (Phase-I & Phase-II) Project Timeline

* **Slide Title:** `Capstone (Phase-I & Phase-II) Project Timeline`
* **Layout:** Gantt Matrix Table + Individual Effort Allocation Column.

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
> *"Our 16-week timeline follows a Test-Driven Development methodology. The first four weeks focus on threat modeling and building the LangGraph topology simulator. Weeks 5 to 8 cover red-team automation and deploying the System-1 triage classifier. Weeks 9 to 12 implement System-2 trajectory reasoning and containment dashboards. The final month closes the co-evolutionary retraining loop, conducts comprehensive benchmarking, and finalizes our conference paper."*

---

## Slide 9: Any other information

* **Slide Title:** `Any other information`
* **Layout:** 2-Column Split (Left: Proposed Closed-Loop Architecture | Right: System-1 Empirical Benchmarks).

### Visual Assets & File Embeddings:
1. **Left Image Container:** [`review_1/ppt/training_pipeline.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/training_pipeline.jpeg)  
   *(Caption: Dual-Plane Architecture — Production Low-Latency Enforcement & Training Active Co-Evolution)*
2. **Right Image Container:** [`review_1/ppt/system1_benchmark.jpeg`](file:///Users/neelchandrakar/Desktop/capstone/review_1/ppt/system1_benchmark.jpeg)  
   *(Caption: Empirical Benchmark Comparison of System-1 Decision Models across 10 Datasets)*

### On-Slide Content:
#### 1. Proposed Closed-Loop Architecture (`training_pipeline.jpeg`)
* **Production Runtime Plane:** Threat Actor (RED Agent) $\to$ **Defender Model (System-1 Triage)** inspects traffic in ~30–50ms $\to$ safe messages reach **Multi-Agent Application** $\to$ execution logs saved to **DB** $\to$ synced to training plane.
* **Training & Co-Evolution Plane:** Chat Traces $\to$ Trace Extraction $\to$ **Privacy Filter (Removal of PII)** $\to$ Prepare Training Data $\to$ Model Retraining $\to$ **Model Registry (MLflow)** $\to$ **Publish** updated weights back to Defender Model.

#### 2. Empirical Benchmark Takeaways (`system1_benchmark.jpeg`)
* **Tool Invocation Precision:** **Clef-flash** dominates with **98.76%** on BFCL exact-case and **93.11%** on API-Bank, establishing it as the premier edge gate for validating tool schemas.
* **Intervention Boundary:** **Jev** leads on When2Call accuracy (**80.97%** vs. Clef's 72.37%), uniquely qualifying it to decide when interactions require System-2 escalation.
* **Conversational Edge Collapse:** **Laya** fails on complex agent tasks (38.13% BFCL, 11.41% API-Bank, 0.00% Home appliances), proving generic edge conversational models cannot secure agent swarms without specialized tuning.

### Verbatim Speaker Notes (Spoken Script):
> *"Under 'Any Other Information', we present our core architectural and empirical breakthroughs. On the left, our training pipeline diagram illustrates our closed-loop architecture: in production, a low-latency Defender Model triages incoming red-agent traffic before reaching the multi-agent application. Chat traces are synced, stripped of private information via privacy filters, used to retrain the models, and republished through MLflow. On the right, our empirical benchmark across ten datasets shows why we select Clef-flash for tool precision—achieving 98.76% on BFCL—and Jev for intervention decisions, achieving 80.97% on When2Call, while naive conversational models like Laya collapse completely."*

### Anticipated Panel Questions & Bulletproof Answers:
* **Q: Why do you need both Clef-flash and Jev instead of just one model?**  
  * **A:** They solve distinct mathematical sub-problems: Clef-flash specializes in structured function-calling and schema compliance (98.76% BFCL), whereas Jev specializes in intent boundary detection (80.97% When2Call)—knowing exactly *when* an inter-agent interaction has drifted enough to warrant deep System-2 intervention.

---

## Slide 10: Thank You

* **Slide Title:** `Thank You`
* **Layout:** 2-Column Split (Left: Formal References | Right: Project Summary & Q&A).

### On-Slide Content:
#### Formal References & Citations
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

#### Summary Takeaways
* **The Vulnerability:** Autonomous MAS suffers from lateral trust asymmetry; Mind Viruses ($R_0 > 1$) and multi-turn Crescendo drift bypass perimeter defenses.
* **The Solution:** Our dual-plane closed loop balances **sub-50ms System-1 triage** with **System-2 trajectory verification**, mathematically ensuring $R_0 < 1$ with $>75\%$ cost reduction.
* **Active Co-Evolution:** Continuous retraining via MLflow guarantees persistent resilience against mutating adversarial strategies.

* **Project Repository:** Private Git (`PES1UG22CS360 / adaptive-defense-mas`)
* **Open for Panel Feedback & Questions. Thank you!**

### Verbatim Speaker Notes (Spoken Script):
> *"To conclude: Multi-Agent Systems are the future of enterprise autonomous workflows, but lateral trust asymmetry makes them extraordinarily vulnerable to self-replicating mind viruses and multi-turn crescendo drift. By uniting high-speed System-1 decision gates with deep System-2 trajectory verification in a closed-loop retraining pipeline, our project provides the first active, provably resilient immune system for agentic swarms. Thank you for your time and guidance, and we welcome any questions from the panel."*

---

## Appendix: Python-PPTX Automation Blueprint (For Claude)

When asked to generate the `.pptx` file directly, Claude can use the following verified `python-pptx` template structure:

```python
import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9 widescreen
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]  # Blank slide

# Color Palette
BG_COLOR = RGBColor(11, 15, 25)       # Dark slate #0B0F19
CARD_COLOR = RGBColor(30, 41, 59)     # Slate #1E293B
TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
EMERALD = RGBColor(16, 185, 129)      # #10B981
CYAN = RGBColor(6, 182, 212)          # #06B6D4
RED = RGBColor(239, 68, 68)           # #EF4444

# Add slides, shapes, tables, and images programmatically...
```
