import code
import readline
import rlcompleter
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DOCUMENTS_ROOT = REPO_ROOT / "Documents"

for candidate in (REPO_ROOT, DOCUMENTS_ROOT):
    candidate_str = str(candidate)
    if candidate_str not in sys.path:
        sys.path.insert(0, candidate_str)

from MGScripts.bootstrap import load_env as load_mgscripts_env

CHEATSHEET = """
===========================
 MainGit Interactive Console
===========================

MGScripts (Parent Repo)
-----------------------------------

List everything loaded:
    dir()

Reload both the parent scripts and Documents toolkit:
    reload_all()
    reload_mgscripts()
    reload_documents()

Inspect functions and modules:
    help(module_name)
    help(function_name)
    dir(module_name)
    pinspect(module_name)

Persist helper code into the current working tree:
    add_script("name.py", callable_or_source)

-----------------------------------

Documents Toolkit + Notes
-----------------------------------

SurzsEnviro helpers are loaded directly into the session:
    speak("note to self")
    ec("pwd")

Browse the markdown knowledge base:
    notes_list()
    notes_search("keyword")
    notes_open("relative/path.md")
"""


def module_aware_completer(namespace):
    try:
        from jedi import Interpreter

        jedi_available = True
    except ImportError:
        jedi_available = False
        print("Note: Install 'jedi' for better autocompletion (pip install jedi)")

    fallback_completer = rlcompleter.Completer(namespace)

    def fallback_complete(text, state):
        if "." in text:
            module_name, _, attr_prefix = text.rpartition(".")
            module = namespace.get(module_name)
            if module:
                attrs = [attr for attr in dir(module) if attr.startswith(attr_prefix)]
                if state < len(attrs):
                    return f"{module_name}.{attrs[state]}"
                return None
        return fallback_completer.complete(text, state)

    if not jedi_available:
        return fallback_complete

    def jedi_complete(text, state):
        if state == 0:
            try:
                interpreter = Interpreter(text, [namespace, namespace])
                completions = interpreter.complete()
                jedi_complete.matches = []
                for completion in completions:
                    name = completion.name
                    if "." in text:
                        base, _ = text.rsplit(".", 1)
                        full = f"{base}.{name}"
                    else:
                        full = name
                    if full.startswith(text):
                        jedi_complete.matches.append(full)

                fallback_matches = []
                for index in range(100):
                    fallback = fallback_complete(text, index)
                    if fallback is None:
                        break
                    if fallback not in jedi_complete.matches:
                        fallback_matches.append(fallback)
                jedi_complete.matches.extend(fallback_matches)
            except Exception:
                jedi_complete.matches = []
                for index in range(100):
                    fallback = fallback_complete(text, index)
                    if fallback is None:
                        break
                    jedi_complete.matches.append(fallback)

        if state < len(jedi_complete.matches):
            return jedi_complete.matches[state]
        return None

    return jedi_complete


def build_namespace():
    if not DOCUMENTS_ROOT.exists():
        raise FileNotFoundError(
            f"Documents submodule not found at {DOCUMENTS_ROOT}. Run 'git submodule update --init --recursive'."
        )

    from Exploit_Notes.bootstrap import load_notes
    from SurzsEnviro.bootstrap import load_env as load_documents_env

    documents_namespace = load_documents_env()
    mgscripts_namespace = load_mgscripts_env()
    notes_namespace = load_notes()

    namespace = {
        "REPO_ROOT": REPO_ROOT,
        "DOCUMENTS_ROOT": DOCUMENTS_ROOT,
        "documents_env": documents_namespace,
        "mgscripts_env": mgscripts_namespace,
    }
    namespace.update(documents_namespace)
    namespace.update(mgscripts_namespace)
    namespace.update(notes_namespace)

    def reload_documents():
        reloader = documents_namespace.get("reload_all")
        if callable(reloader):
            reloader()

    def reload_mgscripts():
        reloader = mgscripts_namespace.get("reload_all")
        if callable(reloader):
            reloader()

    def reload_all():
        reload_documents()
        reload_mgscripts()
        reindex = namespace.get("notes_reindex")
        if callable(reindex):
            reindex()

    namespace["reload_documents"] = reload_documents
    namespace["reload_mgscripts"] = reload_mgscripts
    namespace["reload_all"] = reload_all
    namespace["CHEATSHEET"] = CHEATSHEET
    return namespace


def launch_repl(namespace):
    try:
        from IPython import start_ipython
    except ImportError:
        readline.parse_and_bind("tab: complete")
        readline.set_completer(module_aware_completer(namespace))
        code.interact(local=namespace, banner=CHEATSHEET)
        return

    print(CHEATSHEET)
    start_ipython(argv=[], user_ns=namespace, display_banner=False)


def main():
    launch_repl(build_namespace())


if __name__ == "__main__":
    main()
