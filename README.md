# MainGit — SurzsEnviro toolkit & Exploit Notes

PLEASE NOTE THIS READ ME IS FOR THE BASE LOGIC.

The docker files and compose scripts are in fact helper's to run the base AI assistant logic housed within the container. Consider it a peek into a cluttered student's desk full of Cybersecurity notes, scripts, and tools. 

Open-webui is there to provide a user-friendly interface (however it's very underdeveloped in my opinion, as the functions and tools provided to the AI in each session are usually ephermual, prone to change, and not easily indexed or documented in a static way).

Open-terminal is shelved for now, but is a quick way to give the AI a terminal interface to run commands in. It's probably the next project to be brought back up to speed.

The trainer is a helper script to run the AI through a training session, where it can be given a set of notes and scripts to learn from, and then tested on its ability to recall and use that information in a simulated attack scenario. It's a way to help the AI build up its knowledge base and practice using it in a realistic context.

As for the AI. His name (and the project name at large) is Dexter. If you find references in the comments, heads up, NES is fantastic and you should probably check it out more under the hood.

A REPL-first operator toolkit paired with a Markdown knowledge base for offensive-security workflows.

This repository bundles two complementary parts:

- SurzsEnviro — a scripts-first Python toolkit (operator helpers, network utilities, packet capture, logging helpers, and small CLIs).
- Exploit_Notes — a markdown knowledge base and notes tree (Exploit_Notes/) intended to be browsed together with the toolkit.
- MGScripts — utility scripts used by the interactive bootstrap to expose helpers in a live REPL.

This project is designed to be used interactively: the root bootstrap loads helper modules and notes into a single Python REPL so operators can combine code and notes in the same session.

Quickstart
----------
1. Clone (preserve submodules) or update submodules if already cloned:

   git clone <repo-url> --recurse-submodules
   cd <repo-root>
   # or if already cloned:
   git submodule update --init --recursive

2. Create and activate a virtual environment, then install dependencies (the repository uses a top-level `requirements.md` which references `Documents/requirements.md`):

   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.md

3. Launch the interactive operator console (lightweight REPL):

   python3 bootstrap.py

Docker compose helper
---------------------
To run Docker Compose with the repository's `_env` file on Kali/Linux, use:

   docker compose --env-file _env -f docker-compose.yml up -d

On Windows/PowerShell, you can still use:

   .\compose.ps1 up -d

These apply:
- --env-file _env
- -f docker-compose.yml

   Documents-only REPL (lighter):

   python3 Documents/bootstrap.py

   Optional IPython-backed REPL (when IPython is installed):

   python3 bootstrap.py --shell ipython

Project structure (high-level)
------------------------------
- bootstrap.py              — root REPL bootstrap (combines MGScripts + Documents)
- ipython_startup.py        — helper to auto-load the REPL namespace into IPython
- requirements.md           — top-level requirements file (points to Documents/requirements.md)
- MGScripts/                — parent-repo helper scripts namespace and loader
  - bootstrap.py            — load_env(), add_script(), pinspect(), reload_all()
- Documents/                — submodule containing notes and SurzsEnviro toolkit
  - SurzsEnviro/            — the scripts-first Python toolkit
    - catchingpackets.py    — live packet capture / pcap analysis CLI
    - computerspeak.py      — shell wrapper and logging helpers
    - httpme.py             — HTTP utilities
    - metasploiting.py      — Metasploit RPC helpers
    - netrunning.py         — network scanning & helpers
    - packetcraft.py        — crafted packet generation helpers
    - shellwalking.py       — shell-history collection utilities
    - target_config.py      — runtime configuration & guardrails
    - whatprocess.py        — process/service helpers
    - SurzalsNotes/         — local notes/log output directory
  - Exploit_Notes/          — markdown knowledge base (notes, exploits, walkthroughs)

Usage highlights
----------------
- The code is "REPL-first": many helpers are intended to be imported into an interactive session and used directly.
- The bootstrap exposes helper shortcuts such as `speak()`, `reload_all()`, and `add_script()` into the REPL namespace.
- Notes live under `Documents/Exploit_Notes/` and are accessible through the REPL via `NOTES_ROOT`.

Useful smoke checks
-------------------
(from the repo root)

- Verify the packet-capture CLI helps output:

  python3 Documents/SurzsEnviro/catchingpackets.py --help

- Quick runtime namespace check:

  python3 - <<'PY'
from MGScripts.bootstrap import load_env
ns = load_env()
print('speak' in ns, 'reload_all' in ns, 'add_script' in ns)
PY

- Start the interactive console and experiment with helpers:

  python3 bootstrap.py

Tests
-----
A minimal pytest-based smoke test is present at tests/test_smoke.py (it asserts several repo smoke-check helpers return success).

Running tests locally (recommended)
-----------------------------------
1. Create and activate a Python virtual environment, then install dependencies:
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.md

2. Install pytest if not already installed:
   python3 -m pip install pytest

3. Run the smoke tests:
   pytest -q tests/test_smoke.py

To run all tests (if additional tests are added):
   pytest -q

Notes
-----
- The smoke tests call helper functions from smoke_check; ensure the repository root is the current working directory so imports from MGScripts and Documents resolve correctly.
- If requirements.md refers to external or system packages, install those as needed before running tests.

Development & conventions
-------------------------
- This repository is not packaged as a typical Python package; modules are intentionally "scripts-first" and the bootstrap loader manipulates sys.path to expose bare imports inside SurzsEnviro.
- Preserve the repo's import styles: package-qualified imports from the repo root and bare imports inside SurzsEnviro modules.
- Many modules mix return values with side-effect logging. Before refactoring, confirm callers do not rely on console/log side effects.
- There is no committed test suite or CI configuration. The repository includes `black`, `ruff`, and `pyright` in dependencies but no checked-in configs or commands to wire them together.
- See `Documents/.github/copilot-instructions.md` for additional developer guidance and recommended smoke checks.

Contributing
------------
If you'd like this README changed, or want a different indexing style (JSON index, generated module docs, or a full CODEBASE index), tell me which format you prefer and I can regenerate or add an index file.

License
-------
No LICENSE file is committed in this repository. Check with the repository owner before reusing code or notes.

Acknowledgements
-----------------
Generated and indexed automatically from repository structure and in-repo documentation. Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>


<Developer Notes>

