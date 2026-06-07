import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
repo_root_str = str(REPO_ROOT)
if repo_root_str not in sys.path:
    sys.path.insert(0, repo_root_str)

from bootstrap import build_namespace

shell = get_ipython()
if shell is None:
    raise RuntimeError("ipython_startup.py must be loaded by IPython.")

shell.push(build_namespace
