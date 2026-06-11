import code
import importlib.util
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

CHEATSHEET = """\
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

ROOT_NAMESPACE_KEYS = {
    "REPO_ROOT",
    "DOCUMENTS_ROOT",
    "documents_env",
    "mgscripts_env",
    "reload_documents",
    "reload_mgscripts",
    "reload_all",
    "CHEATSHEET",
}


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

    documents_bootstrap = DOCUMENTS_ROOT / "bootstrap.py"
    if not documents_bootstrap.exists():
        raise FileNotFoundError(
            f"Documents bootstrap not found at {documents_bootstrap}."
        )

    documents_spec = importlib.util.spec_from_file_location(
        "documents_bootstrap", documents_bootstrap
    )
    if documents_spec is None or documents_spec.loader is None:
        raise ImportError(f"Could not load module spec from {documents_bootstrap}")

    documents_module = importlib.util.module_from_spec(documents_spec)
    documents_spec.loader.exec_module(documents_module)
    build_documents_namespace = documents_module.build_namespace
    if not callable(build_documents_namespace):
        raise ImportError(
            f"Documents bootstrap at {documents_bootstrap} does not expose build_namespace()."
        )

    namespace = {
        "REPO_ROOT": REPO_ROOT,
        "DOCUMENTS_ROOT": DOCUMENTS_ROOT,
    }
    scoped_exports = {"documents": set(), "mgscripts": set()}

    def refresh_scope(scope_name, new_values):
        exported_keys = set(new_values)
        removable_keys = scoped_exports[scope_name] - exported_keys
        for key in removable_keys:
            if key not in ROOT_NAMESPACE_KEYS:
                namespace.pop(key, None)
        namespace.update(new_values)
        scoped_exports[scope_name] = exported_keys
        namespace[f"{scope_name}_env"] = new_values

    refresh_scope("documents", build_documents_namespace())
    refresh_scope("mgscripts", load_mgscripts_env())

    def reload_documents():
        reloader = namespace["documents_env"].get("reload_all")
        if callable(reloader):
            reloader()
        refresh_scope("documents", build_documents_namespace())

    def reload_mgscripts():
        reloader = namespace["mgscripts_env"].get("reload_all")
        if callable(reloader):
            reloader()
        refresh_scope("mgscripts", load_mgscripts_env())

    def reload_all():
        reload_documents()
        reload_mgscripts()

    namespace["reload_documents"] = reload_documents
    namespace["reload_mgscripts"] = reload_mgscripts
    namespace["reload_all"] = reload_all
    namespace["CHEATSHEET"] = CHEATSHEET
    return namespace

if __name__ == "__main__":
    namespace = build_namespace()
    readline.set_completer(module_aware_completer(namespace))
    readline.parse_and_bind("tab: complete")
    print(CHEATSHEET)
    code.interact(local=namespace) #yeah we need to stop thinking "cli" and start thinking "interactive console"