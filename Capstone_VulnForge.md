# 🧠 Project Concept: VulnForge — An Adaptive, AI-Generated CTF Training Platform

## Overview

**VulnForge** is a local-first, AI-driven cybersecurity training platform that generates unique, vulnerable environments on-demand. It combines Docker containers, local LLMs, and CTF-style problem-solving to create an adaptive learning experience that scales with the user's skill level.

Unlike traditional CTFs with static challenges, VulnForge generates a **new, unknown vulnerable box** every session, provides contextual hints, and offers research guidance—all while running entirely on the user's local machine.

---

## Core Concept

The platform generates a random vulnerable environment using **Docker** templates, spins it up via **Docker Compose**, and challenges the user to compromise it. A local LLM (e.g., Ollama, LM Studio) acts as an adaptive hint system, aware of the vulnerability but only revealing information as needed.

---

## Key Features

| Feature | Description |

|---------|-------------|

| **Dynamic Environments** | Randomly selects a Docker template each session—no two runs are the same |

| **Adaptive Hint System** | LLM provides hints based on user progress, from subtle clues to research topics |

| **Frustration Safeguards** | Tool calls for "topic to research" or "here's a foothold" prevent dead ends |

| **Local-First** | No cloud dependencies—runs entirely on Docker + Hyper-V + local LLM |

| **Self-Improving** | Tracks time-to-exploit and hint usage to adjust difficulty over time |

---

## Technical Architecture

┌─────────────────────────────────────────────────────────┐

│ Orchestrator (Python) │

├─────────────────────────────────────────────────────────┤

│ 1. LLM selects a random Vulhub template │

│ 2. Generates docker-compose.yml dynamically │

│ 3. Launches container with docker-compose up │

│ 4. User manually exploits the target │

│ 5. LLM monitors user input (requests for hints) │

│ 6. Provides graduated assistance: │

│ - "Research this topic: [CVE/service]" │

│ - "Try this foothold: [clue]" │

│ - "Here's the exploit" (last resort) │

│ 7. On success: logs technique, resets, repeats │

└─────────────────────────────────────────────────────────┘

---

## Why This Matters

### For Learning

- **Active recall**: Users must discover the vulnerability themselves

- **Adaptive difficulty**: Hints prevent frustration while maintaining challenge

- **Real-world relevance**: Uses actual CVEs from Vulhub

### For Portfolio

- **Cross-disciplinary**: Security + DevOps + AI integration

- **Demonstrates creativity**: Not just another "run the exploit" project

- **Shows teaching ability**: Designed with educational UX in mind

---

## Technologies Used

| Technology | Role |

|------------|------|

| **Python** | Orchestration, Docker API, prompt logic |

| **Docker / Hyper-V** | Container orchestration and isolation |

| **Ollama / LM Studio** | Local LLM inference |

| **Docker** | Source of vulnerable templates |

| **Markdown** | Report generation and documentation |

---

## Project Timeline (Suggested)

| Phase | Tasks |

|-------|-------|

| **MVP (Week 1-2)** | Single hardcoded Docker template, basic launch script, manual hint system |

| **Core (Week 3-4)** | Random template selection, LLM integration, hint generation |

| **Polish (Week 5-6)** | Tool calls, logging, UX improvements, demo video |

| **Capstone Deliverable** | Full walkthrough video + GitHub repo + written report |

---

## Educational Alignment

| Course | Contribution |

|--------|--------------|

| **AIML 1310** | LLM prompt engineering, tool calling |

| **CIST 1858** | Vulnerability knowledge, exploit logic |

| **CIST 2860** | Forensic logging, artifact analysis |

| **CSCI 1220** | Python glue code, automation |

| **ENGL 1210 / 1160** | Documentation, report writing |

| **PHIL 1120** | Logical hint structuring |

| **BUSA 1110 / 1130** | Business context, professionalism |

---

## Future Enhancements

- **Difficulty tiers**: Beginner → Intermediate → Advanced

- **Score tracking**: Time, hints used, techniques attempted

- **Multi-user mode**: Compete with peers on same generated box

- **Custom template upload**: Users add their own vulnerable services

- **Auto-walkthrough generation**: LLM creates a full report after completion

---

## Why This Is Capstone-Ready

VulnForge is more than a lab—it's a **demonstration of systems thinking**. It combines:

- Deep security knowledge

- Practical DevOps skills

- AI integration

- User experience design

- Educational philosophy

It answers the question: *"Can I build something that teaches other people what I know?"*

---

## Repository Structure (Suggested)

vulnforge/

├── README.md

├── requirements.txt

├── docker-compose.template.yml

├── main.py

├── hints/

│ └── prompt_templates.json

├── templates/

│ └── docker_list.json

├── logs/

│ └── session_*.log

└── docs/

├── architecture.md

└── walkthrough.md

---

## Demo Script (For Presentation)

1. **Launch**: Run `python main.py`

2. **Spawning**: Show container spinning up

3. **Discovery**: User scans target, finds open port

4. **Struggle**: User requests hint → LLM provides research topic

5. **Exploit**: User compromises the box

6. **Analysis**: LLM generates a summary report

7. **Reset**: System resets for next user

---

## Contact & Credit

**Project Lead**: Vanessa Greenwald

**Program**: Computer Information Systems (AAS) – Cyber Security  

**Institution**: Central New Mexico Community College  
*"Don't just run exploits—build the environment that teaches them."*
