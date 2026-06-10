import subprocess

def launch_repl_framework():
    # Step 1: Verify Working Directory
    current_dir = subprocess.run("cd /config/workspace && pwd", shell=True, capture_output=True).stdout.decode('utf-8').strip()
    
    if current_dir != "/config/workspace":
        raise Exception(f"Current directory is {current_dir}, expected /config/workspace")
    
    # Step 2: Launch 'bootstrap.py' with Correct User Credentials
    subprocess.run("su - user && cd /config/workspace && python3 bootstrap.py", shell=True, capture_output=True)
    
    print("REPL framework launched successfully.")

if __name__ == "__main__":
    launch_repl_framework()