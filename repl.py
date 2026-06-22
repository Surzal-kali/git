import subprocess
import sys
import os

def launch_repl_framework():
    # Verify working directory
    workspace_dir = "/config/workspace"
    if not os.path.isdir(workspace_dir):
        raise FileNotFoundError(f"Workspace directory not found: {workspace_dir}")
    
    # Launch bootstrap.py directly with current Python executable
    try:
        subprocess.run([sys.executable, os.path.join(workspace_dir, "bootstrap.py")], check=True)
        print("REPL framework launched successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error launching REPL: {e}", file=sys.stderr)
        raise
    except FileNotFoundError:
        print(f"Python executable or bootstrap.py not found", file=sys.stderr)
        raise
#testing testing one two three? 
if __name__ == "__main__":
    launch_repl_framework()