# Dexter / MainGit — Cybersecurity Operator Toolkit

## Project Overview

**Dexter** (aka **MainGit**, **Surz**) is a local-first, Python-based offensive security operator toolkit. It provides an interactive REPL environment that bundles network scanning, packet capture, Metasploit RPC, HTTP utilities, and shell helpers with a RAG-backed knowledge assistant powered by a local LLM (Ollama). The project also includes a PyTorch training pipeline and Docker infrastructure for Open WebUI integration.

Designed around a **REPL-first philosophy**: modules are intended to be imported interactively, not distributed as CLI tools. Many modules mix return values with logging side-effects for rapid operator workflows.

### Repository Alias

The git repo name `git` is an alias. The project identity across code and docs is **Dexter** / **MainGit**.

---

## Architecture

```
git/                           # Project root (alias)
├── SurzsEnviro/               # Core operator toolkit
│   ├── knowledge_bridge.py    # RAG system: SentenceTransformer + Ollama over local .md notes
│   ├── muesem/                # Python modules loaded by bootstrap
│   │   ├── bootstrap.py       # Discovers all SurzsEnviro modules, builds REPL namespace
│   │   ├── catchingpackets.py # Packet capture (pyshark/scapy)
│   │   ├── freshmeat.py       # Payload generation
│   │   ├── metasploiting.py   # Metasploit RPC interface
│   │   ├── netrunning.py      # Network scanning (nmap wrapper)
│   │   ├── shellwalking.py    # Shell/process exploration helpers
│   │   └── target_config.py   # Target configuration management
│   └── showoff.sh             # Bash entry, sets TARGET_DIR and PAYLOAD_DIR
│
├── rag_router.py              # FastAPI bridge: ChromaDB + Ollama → Open WebUI /chat endpoint
├── raggedyanne.sh             # systemd unit file for running rag_router as a service
├── trainer/                   # PyTorch training loop with checkpoint/resume
│   ├── trainer.py             # PersistentTrainer class (background thread, stop/resume)
│   ├── checkpoint.py          # CheckpointManager: save/load model + optimizer state
│   └── api.py                 # FastAPI endpoints to control training remotely
├── tests/
│   └── test_smoke.py          # Parametrized smoke checks (imports, config, env loading)
├── Documents/                 # Git submodule → GitHub:Surzal-kali/Documents
│                              # Contains exploit notes (.md), consumed by knowledge_bridge RAG
├── dockerstuff/               # Docker Compose stack
│   ├── docker-compose.yml     # Open WebUI service bound to port 8080
│   ├── compose.ps1           # PowerShell helper to bring up compose
│   ├── Dockerfile.open-webui  # Open WebUI image (Ollama backend, RAG config)
│   └── Dockerfile.trainer     # PyTorch training container
├── .env.example               # Env template: Ollama URL, Open Terminal API, trainer checkpoint dir
├── requirements.md            # Python dependencies (paramiko, scapy, pyshark, pymetasploit3, etc.)
└── testing.ipynb              # Jupyter notebook for exploratory testing
```

---

## Key Components

### SurzsEnviro / muesem — Operator Modules
- **bootstrap.py** is the entry point. `load_env()` walks all packages under `SurzsEnviro`, imports each module, and populates a flat namespace dict. Hot reload via `reload_all()`. Script export via `add_script()` (supports raw strings, `inspect.getsource`, dill serialization, stdlib fallback).
- Modules are mixed-return/side-effect: designed for fast interactive feedback, not clean API contracts.

### Knowledge Bridge (`knowledge_bridge.py`)
- Crawls `Documents/Exploit_Notes/*.md` files
- Embeds all notes with `all-MiniLM-L6-v2` (SentenceTransformer)
- On query: dot-product similarity search (top 3), then sends context + prompt to Ollama's `llama3`
- Exposes a singleton `ask_notes()` function for REPL use

### RAG Router (`rag_router.py`)
- FastAPI app exposing `/chat` — proxied to Open WebUI at port 3000
- Supports both streaming (SSE) and non-streaming responses
- Includes ChromaDB helpers for document collections (ephemeral by default — data lost on restart)

### Trainer (`trainer/`)
- `PersistentTrainer`: runs in a daemon thread, supports start/stop/resume
- CheckpointManager: saves model + optimizer state to `/workspace/checkpoints` with JSON metadata
- Designed to survive session disconnects (controlled via FastAPI API or terminal server)

### Docker Infrastructure
- **Open WebUI** on port 8080, Ollama backend pointed at a remote Tailnet URL
- RAG embedding: `nomic-embed-text` via Ollama
- Compose managed via `compose.ps1` (PowerShell), also runs via systemd (`raggedyanne.sh`)

---

## Building and Running

### Prerequisites
- Python 3.10+ with venv
- Docker Desktop (WSL2 backend on Windows, or native Linux)
- Ollama running locally or reachable at the configured URL
- Git LFS for the `Documents` submodule

### Setup
```powershell
# Initialize git submodule (exploit notes)
git submodule update --init --recursive

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies from requirements.md
pip install -r requirements.md
```

### Run the REPL Environment
Interactive exploration via bootstrap:
```bash
python -c "from SurzsEnviro.muesem.bootstrap import load_env; ns = load_env(); code.interact(local=ns)"
```

Or use IPython:
```bash
ipython -i SurzsEnviro/muesem/bootstrap.py
```

### Docker Stack (PowerShell)
```powershell
cd dockerstuff
.\compose.ps1  # Builds and starts Open WebUI + trainer services
```

### RAG Router as a Service (Linux systemd)
Copy `raggedyanne.sh` to `/etc/systemd/system/rag-router.service`, adjust paths, then:
```bash
systemctl enable --now rag-router
```

### Tests
```bash
pytest tests/test_smoke.py -v
```

---

## Development Conventions

- **REPL-first design**: Functions often print as well as return. Do not refactor to remove side-effects unless the behavior is broken.
- **Module naming in `muesem/`**: Keep names consistent with actual package structure; avoid duplicates that cause namespace conflicts when `bootstrap.load_env()` flattens everything.
- **Environment variables**: Never commit `.env`. Copy from `.env.example` and customize. Ollama URL points to the operator's local or remote Tailnet endpoint.
- **ChromaDB is ephemeral by default**: `rag_router.py` uses `EphemeralClient`. If persistent storage is needed, switch to a `PersistentClient` with a disk path.
- **Checkpoints live in `/workspace/checkpoints`**: Mountable from Docker volumes; configured via `TRAINER_CHECKPOINT_DIR` env var.

### Linting / Formatting
Dependencies include `ruff`, `pyright`, and `black`. Run manually:
```bash
ruff check SurzsEnviro/ trainer/
pyright SurzsEnviro/ trainer/
```

---

## Environment Variables

| Variable | Purpose |
|---|---|
| `OLLAMA_BASE_URL` | Ollama API endpoint (default: local 11434) |
| `RAG_EMBEDDING_ENGINE` | Embedding backend for Open WebUI RAG (`ollama`) |
| `RAG_EMBEDDING_MODEL` | Embedding model name (`nomic-embed-text`) |
| `OPEN_TERMINAL_API_KEY` | Auth key for the terminal server web UI |
| `CORS_ALLOWED_ORIGINS` | CORS whitelist for Open WebUI |
| `TRAINER_CHECKPOINT_DIR` | Directory where PyTorch checkpoints are saved |

---

## Git Notes

- `Documents/` is a **submodule** pointing to `https://github.com/Surzal-kali/Documents.git`. Always run `git submodule update --init --recursive` after clone.
- `.gitignore` aggressively filters Python cache, venvs, logs, databases, and environment files. Burp config JSON files are explicitly allowed.
