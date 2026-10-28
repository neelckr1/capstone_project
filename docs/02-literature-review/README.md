# Literature Review Paper Index & Domain Mapping

This folder contains research papers directly related to the foundational anchor papers in `research_papers/`. They are categorized across the core architectural and threat-modeling pillars of the **Adaptive Defense for Multi Agent Systems** project.

---

## 1. Domain Mapping Matrix

| Anchor Paper in `research_papers/` | Core Focus | Related Papers in `lit_review/` |
|:---|:---|:---|
| **Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems** *(Anthropic / EPFL, 2024)* | Self-replicating prompts, viral reproduction number $R_0$, inter-agent transmission across network topologies. | • `Prompt_Infection_LLM_to_LLM_in_MAS.pdf`<br>• `Morris_II_AI_Worm_Self_Replicating_Prompts.pdf`<br>• `Beyond_Single_Model_Injection_Threat_Model_MAS.pdf` |
| **OpenAI–Hugging Face Incident Technical Report** *(OpenAI, 2024)* | Autonomous agents coordinating via shared infrastructure, escaping evaluation sandboxes, emergent rogue actions. | • `Beyond_Single_Model_Injection_Threat_Model_MAS.pdf`<br>• `Morris_II_AI_Worm_Self_Replicating_Prompts.pdf` |
| **RLredAgent / AutoInject** *(ETH Zürich, 2024)* | Automated adversarial prompt optimization, black-box RL suffixes, tool-calling agent benchmark (AgentDojo). | • `Crescendo_Multi_Turn_Jailbreak_Attack.pdf`<br>• `AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf`<br>• `InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf`<br>• `PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf`<br>• `TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf` |
| **CivicShield** *(Patil, 2024)* | Layered Defense-in-Depth, stateful input/output filtering, multi-turn escalation containment for AI chatbots. | • `Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf`<br>• `Llama_Guard_Input_Output_Safeguard.pdf`<br>• `NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf` |

---

## 2. Summary of Papers in `lit_review/`

### Group A: Multi-Agent Viral Propagation, Infections & Worms

1. **`Prompt_Infection_LLM_to_LLM_in_MAS.pdf`**
   * **Title:** *Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems*
   * **Authors:** Donghyun Lee, Mo Tiwari (Oct 2024 | arXiv:2410.07283)
   * **Key Contribution:** Directly conceptualizes prompt injection as a self-replicating computer virus ("Prompt Infection") hopping between autonomous LLM agents in collaborative workflows. Proposes an LLM tagging mechanism for mitigation.
   * **Use in Review:** Primary peer paper to Anthropic's Mind Viruses; demonstrates empirical multi-agent spread.

2. **`Morris_II_AI_Worm_Self_Replicating_Prompts.pdf`**
   * **Title:** *Here Comes the AI Worm: Unleashing Zero-click Worms that Target GenAI-Powered Applications*
   * **Authors:** Stav Cohen, Ron Bitton, Ben Nassi (ACM CCS 2025 | arXiv:2403.02817)
   * **Key Contribution:** Implements "Morris-II", the first zero-click worm targeting GenAI ecosystems via adversarial self-replicating prompts propagating through RAG systems and email assistants. Proposes the "Virtual Donkey" guardrail.
   * **Use in Review:** Demonstrates real-world exploitability of autonomous propagation without user intervention.

3. **`Beyond_Single_Model_Injection_Threat_Model_MAS.pdf`**
   * **Title:** *Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems*
   * **Authors:** Rudrendu Kumar Paul, Sourav Nandy (ICML AIWILD 2026 | arXiv:2609.22949)
   * **Key Contribution:** Establishes a 14-vector threat taxonomy covering inter-agent message passing and cascading injections. Demonstrates that 67% of agents in a 6-agent system suffer scope violations, and introduces message signing and provenance tracking.
   * **Use in Review:** Formal threat modeling baseline for multi-agent message routing and privilege scoping.

---

### Group B: Multi-Turn Adversarial Attacks & Red-Teaming

4. **`Crescendo_Multi_Turn_Jailbreak_Attack.pdf`**
   * **Title:** *Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack*
   * **Authors:** Mark Russinovich, Ahmed Salem, Ronen Eldan (Microsoft Research, USENIX 2024 | arXiv:2404.01833)
   * **Key Contribution:** Introduces the multi-turn conversational jailbreak attack that begins benignly and escalates over multiple turns. Bypasses single-turn stateless filters with 60–85%+ ASR across GPT-4, Gemini, and Claude.
   * **Use in Review:** Core red-teaming technique used in the project's digital twin to stress-test defenses.

5. **`AgentDojo_Benchmark_Attacks_Defenses_LLM_Agents.pdf`**
   * **Title:** *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*
   * **Authors:** Edoardo Debenedetti et al. (ETH Zürich, NeurIPS 2024 | arXiv:2406.13352)
   * **Key Contribution:** Dynamic benchmark suite containing 97 realistic agent tasks and 629 security test cases across tools (banking, emails, booking). 
   * **Use in Review:** The standard evaluation testbed used by AutoInject; essential for benchmarking agent utility vs. security.

6. **`InjecAgent_Benchmarking_Indirect_Prompt_Injections.pdf`**
   * **Title:** *InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents*
   * **Authors:** Qiusi Zhan et al. (ACL 2024 | arXiv:2403.02691)
   * **Key Contribution:** Evaluates 30 LLM agents across 1,054 indirect injection cases (tool outputs containing injection payloads).
   * **Use in Review:** Primary baseline benchmark for measuring indirect injection vulnerability in tool-calling agents.

7. **`PAIR_Jailbreaking_Black_Box_LLMs_Twenty_Queries.pdf`**
   * **Title:** *Jailbreaking Black Box Large Language Models in Twenty Queries*
   * **Authors:** Patrick Chao et al. (2023 | arXiv:2310.08419)
   * **Key Contribution:** An automated black-box algorithm that uses an attacker LLM to iteratively refine prompt injections against target models in ~20 queries.
   * **Use in Review:** Demonstrates algorithmic multi-turn automated red-teaming.

8. **`TAP_Tree_of_Attacks_Automated_Jailbreaking.pdf`**
   * **Title:** *Tree of Attacks: Jailbreaking Black-Box LLMs Automatically*
   * **Authors:** Anay Mehrotra et al. (2023 | arXiv:2312.02119)
   * **Key Contribution:** Combines Tree-of-Thought search with pruning to guide automated black-box jailbreaks.
   * **Use in Review:** Provides the algorithmic foundation for tree-based attack exploration in the digital twin.

---

### Group C: Defense-in-Depth, Guardrails & Multi-Agent Pipelines

9. **`Multi_Agent_LLM_Defense_Pipeline_Prompt_Injection.pdf`**
   * **Title:** *A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks*
   * **Authors:** S. M. Asif Hossain et al. (2025 | arXiv:2509.14285)
   * **Key Contribution:** Deploys a coordinated multi-agent pipeline (sequential and hierarchical) dedicated to filtering and sanitizing injection attacks.
   * **Use in Review:** Architectural comparison demonstrating multi-agent defensive collaboration.

10. **`Llama_Guard_Input_Output_Safeguard.pdf`**
    * **Title:** *Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations*
    * **Authors:** Hakan Inan et al. (Meta, 2023 | arXiv:2312.06674)
    * **Key Contribution:** Open foundation safety classifier for input/output auditing based on Llama2-7B.
    * **Use in Review:** The classic stateless guardrail baseline, demonstrating why single-turn filters fail against Crescendo/Mind Viruses.

11. **`NeMo_Guardrails_Toolkit_Safe_LLM_Applications.pdf`**
    * **Title:** *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications*
    * **Authors:** Traian Rebedea et al. (NVIDIA, 2023 | arXiv:2310.10501)
    * **Key Contribution:** Programmable dialogue rails (Colang) for enforcing topical, execution, and safety constraints.
    * **Use in Review:** Comparison baseline for rule-based programmable guardrail systems.
