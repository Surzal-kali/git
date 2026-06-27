# Surzal's CTF Workflow — Challenges Workspace

## Purpose

This directory is an **active CTF operations workspace**, not a software project. It is used during live capture-the-flag engagements to track targets, store payloads, document research, and archive write-ups. A reasoning agent (e.g., Qwen Code) operates from this folder alongside the operator toolkit (`../SurzsEnviro/`) and the exploit knowledge base (`../Exploit_Notes/`).

---

## Directory Layout

```
Challenges/
├── payloads/              # Crafted payloads, reverse shells, exploit scripts
├── research_topics/       # Focused research on techniques encountered during runs
├── topology/             # Network maps and target architecture diagrams (Mermaid + PNG)
└── write-ups/            # Per-box recon notes, vuln chains, creds, flags, escalation paths
```

---

## Working Relationship to Sister Directories

### `../SurzsEnviro/` — The Operator Toolkit
Python modules loaded into an interactive REPL via `bootstrap.load_env()`. During a CTF run, the agent imports this toolkit for:
- Network scanning (`netrunning`)
- Packet capture analysis (`catchingpackets`)
- Metasploit RPC (`metasploiting`)
- Payload generation (`freshmeat`)
- Target configuration management (`target_config`)

Key entry point: `python -c "from SurzsEnviro.muesem.bootstrap import load_env; ns = load_env(); code.interact(local=ns)"`

### `../Exploit_Notes/` — The Exploit Knowledge Base (~455 markdown files)
A searchable reference library organized by technique and platform:
- **Windows**: Privilege escalation (SUID, capabilities, kernel CVEs, AD attacks), protocols (RDP, WinRM, LDAP, Kerberos), forensics
- **Web**: SQLi, XXE, SSRF, SSTI, XSS, WAF evasion, file upload bypass, deserialization, template engine exploits
- **Malware/C2**: Collection, exfiltration, evasion, command-and-control patterns
- **Tools**: Burp Suite, Radare2, Wireshark, Turbo Intruder workflows

Query via the knowledge bridge RAG system: `from SurzsEnviro.knowledge_bridge import ask_notes; print(ask_notes("kerberoasting steps"))`

### `../../rag_router.py` — RAG FastAPI Bridge
Proxies chat requests through ChromaDB + Ollama to Open WebUI. Use this when running headless or integrating the knowledge base into an external agent loop.

---

## CTF Run Workflow

### Phase 1: Network Discovery
1. Scan target range using `netrunning` from SurzsEnviro REPL
2. Map open ports and services → document findings in `topology/` as Mermaid diagrams
3. Identify attack surface and prioritize targets by risk tier

### Phase 2: Reconnaissance & Exploitation
1. Fingerprint services, enumerate web endpoints, assess configurations
2. Search `../Exploit_Notes/` for known vulnerability patterns matching discovered services
3. Select and craft payloads → store in `payloads/` (named after target or technique)
4. Execute exploits, capture initial access, verify shell

### Phase 3: Credential Harvesting & Pivot
1. Dump credentials from config files, databases, memory, SSH keys
2. Map lateral movement paths across the network topology
3. Document confirmed creds in the box-specific write-up

### Phase 4: Privilege Escalation
1. Enumerate SUID/SGID, capabilities, cron jobs, systemd services, kernel version
2. Cross-reference `../Exploit_Notes/exploits/exploit/*privilege-escalation*/` for matching vectors
3. Execute escalation → capture root/domain admin
4. Log the full attack chain in write-up

### Phase 5: Post-Compromise & Write-Up
1. Capture all flags, document technique and CVEs used
2. Archive complete write-up under `write-ups/<box-name>.md`
3. If interesting techniques emerged, expand research notes in `research_topics/`

---

## Naming Conventions

| Location | Convention | Example |
|----------|------------|---------|
| `payloads/` | `<target-or-box>-<type>` or standalone technique name | `mercury-exploit.py`, `eatthis.sh` |
| `write-ups/` | Lowercase, box-target name with `.md` extension | `mercury.md`, `qdpmvictim.md` |
| `research_topics/` | TitleCase filename, topic-focused | `fileUploadEvasion.md`, `Radare2.md` |
| `topology/` | Box-specific or network-wide diagrams | `topology.mmd`, `46818.md` |

---

## Agent Behavior Guidance

### When Operating in CTF Mode
- **Reason first, exploit second.** Map the attack surface before reaching for payloads.
- **Always log findings.** If it's not written down in a write-up, it didn't happen. Credentials, vuln chains, and flags are ephemeral once the box resets.
- **Search the knowledge base before Googling.** Exploit Notes is curated from actual engagements — it contains battle-tested techniques.
- **Pay attention to constraints.** Note which users can read what, where writable files live, and which CVEs apply to the discovered kernel/service versions.
- **Prefer logical escalation over kernel exploits where possible.** Systemd service abuse, SUID/capability misuse, or cron misconfiguration are cleaner paths than Dirty Pipe when available.

### When Writing Payloads
- Store in `payloads/` alongside the target name for traceability
- Reverse shells should match the operator's attacker IP (check current session config)
- Mark typos and dead ends (e.g., `eaththis.sh` vs `eatthis.sh`) rather than deleting — they are part of the trail

### When Documenting Write-Ups
Use this structure:
```markdown
# BOX_NAME (IP) — Confirmed Facts
## Target Profile (OS, ports, services, kernel)
## Credentials (SSH, DB, app-level)
## Vulnerability Chain (endpoint → exploit technique → impact)
## Flags (user ✅/🔒, root ✅/🔒)
## Privilege Escalation Vectors Evaluated (table: vector, finding, status)
## Key Constraints
## Next Steps / Open Paths
```

---

## Quick Reference Commands

| Task | Command |
|------|---------|
| Launch SurzsEnviro REPL | `python -c "from SurzsEnviro.muesem.bootstrap import load_env; ns = load_env(); code.interact(local=ns)"` |
| Query exploit knowledge base | `python -c "from SurzsEnviro.knowledge_bridge import ask_notes; print(ask_notes('your question'))"` |
| Start Docker services (Open WebUI + trainer) | `cd dockerstuff && pwsh -File compose.ps1` |
| Run smoke tests | `pytest tests/test_smoke.py -v` |
| Check RAG router health | `curl http://localhost:8000/docs` |
