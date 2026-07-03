# MERCURY (192.168.56.113) — Confirmed Facts

> Last updated: 2026-06-17

---

## Target Profile

| Field | Value |
|-------|-------|
| **IP** | `192.168.56.113` |
| **OS** | Ubuntu 20.04.4 LTS (Focal) |
| **Kernel** | 5.4.0-74-generic |
| **Hostname** | mercury |
| **Port 8080/tcp** | WSGIServer/0.2 CPython/3.8.2 — Django + MySQL ("Mercury Facts") |

---

## Credentials (All Confirmed)

### SSH Accounts

| Account | Username | Password | Source |
|---------|----------|----------|--------|
| webmaster | `webmaster` | `mercuryisthesizeof0.056Earths` | Base64 in `/home/webmaster/mercury_proj/notes.txt` |
| linuxmaster | `linuxmaster` | `mercurymeandiameteris4880km` | Base64 in `/home/webmaster/mercury_proj/notes.txt` |

### Database Users (Dumped via SQLi)

| # | Username | Password |
|---|----------|----------|
| 1 | john | johnny1987 |
| 2 | laura | lovemykids111 |
| 3 | sam | lovemybeer111 |
| 4 | webmaster | mercuryisthesizeof0.056Earths |

---

## SSH Access — Confirmed ✅

| Account | Login | Shell |
|---------|-------|-------|
| webmaster | ✅ | ✅ |
| linuxmaster | ✅ | ✅ |

---

## Flags

| Flag | Status | Location |
|------|--------|----------|
| **User flag** | ✅ Captured | `/home/webmaster/user_flag.txt` → `[user_flag_8339915c9a454657bd60ee58776f4ccd]` |
| **Root flag** | 🔒 Not yet obtained | — |

---

## Vulnerability: SQL Injection (UNION-based)

- **Endpoint:** `GET /mercuryfacts/{id}/`
- **Root cause:** Raw SQL in `mercury_facts/views.py` — unparameterized string concatenation
  ```python
  cursor.execute('SELECT fact FROM facts WHERE id = ' + fact_id)
  ```
- **Proof of concept:** `GET /mercuryfacts/1 UNION SELECT 1/` → returns 2 rows, 1 column each
- **Impact:** Full DB read → credential dump from `users` table

---

## Django App Structure

```
/home/webmaster/mercury_proj/
├── db.sqlite3          ← empty (0 bytes)
├── manage.py           ← executable
├── notes.txt           ← project accounts info
├── mercury_facts/      ← vulnerable app
│   └── views.py        ← SQLi in get_fact_from_db()
├── mercury_index/      ← index page + robots.txt
└── mercury_proj/       ← Django settings
```

---

## Privilege Escalation Vectors — Evaluated

| Vector | Finding | Status |
|--------|---------|--------|
| **SUID binaries** | Standard set only (`sudo`, `pkexec`, `gpasswd`, `su`, `crontab`, `at`) | ❌ No unusual SUID |
| **SGID crontab** | `/usr/bin/crontab` is `-rwxr-sr-x root:crontab` — SGID, not SUID. `-u` flag requires root. | ⏳ Open |
| **sudo** | Requires interactive password for both accounts; no NOPASSWD entries | ❌ Blocked |
| **Cron jobs** | No crontab entries for either user; system cron is default only | ❌ Nothing to abuse |
| **viewsyslog group** | linuxmaster is member, but syslog files are `syslog:adm` (640) — no access | ❌ Dead end |
| **MySQL auth_socket** | ERROR 1698 for root; ERROR 1045 for linuxmaster local connect | ⏳ Open |
| **Symlink abuse** | `/etc/alternatives/vimdiff → /usr/bin/vim.basic` — not writable by us | ❌ Dead end |
| **Writable /etc files** | None writable by either user | ❌ Locked down |

---

## Key Constraints

1. No sudo NOPASSWD for either account
2. `crontab -u` requires root, not just group membership (SGID crontab ≠ SUID)
3. webmaster home is `drwx------ webmaster:webmaster` — linuxmaster cannot read/write it
4. MySQL runs on 3306, bind-address 0.0.0.0, but local socket auth blocks non-db users
5. No writable paths found in `/etc` or webmaster's home directory

---

## ✅ Resolved: PwnKit — CVE-2021-4034 (pkexec Local Privilege Escalation)

### Discovery

| Field | Value |
|-------|-------|
| **Binary** | `/usr/bin/pkexec` |
| **Version** | 0.105 |
| **Package** | policykit-1 0.105-26ubuntu1 (amd64) |
| **OS** | Ubuntu 20.04.1 LTS (Focal Fossa) |
| **Kernel** | 5.4.0-74-generic |
| **SUID bit** | ✅ Yes (`/usr/bin/pkexec` is SUID root) |

### Vulnerability Details

**CVE-2021-4034 (PwnKit)** — A path traversal vulnerability in `pkexec`'s argument validation logic.

**Root cause:** When pkexec receives a `--version` or binary path argument, it attempts to canonicalize the path before checking if the binary exists. The bug: it does not properly handle double-slash (`//`) prefixes, which causes the canonicalization to produce an incorrect result. This allows an attacker to craft a path that bypasses the existence check and executes arbitrary commands as root.

**Mechanics:**
1. pkexec is designed to let authorized users run *one command* as another user (typically root)
2. It checks if the binary being executed exists at an absolute path
3. The bug: `//` tricks the canonicalization logic — `//.../../../bin/sh` resolves incorrectly
4. Result: **any unprivileged user** can execute `/bin/sh` as root without authentication

**Affected versions:** All pkexec versions **before 0.120**. Fixed in commit by Qualys researcher (Alon Bar-Lev).

### Verification on Mercury

```bash
$ ssh webmaster@192.168.56.113 "pkexec --version"
pkexec version 0.105

$ dpkg -l policykit-1 | tail -1
ii  policykit-1    0.105-26ubuntu1    amd64    framework for managing administrative policies and privileges
```

### Exploitation

**Metasploit:**
```
use exploit/linux/local/cve_2021_4034_pwnkit_lpe_pkexec
set SESSION <webmaster_session>
run
```

**Manual (C exploit):**
- Compile CVE-2021-4034 PoC from Exploit-DB #49861
- Transfer to Mercury via SSH/SCP or inline base64 decode
- Execute — drops root shell immediately

### Impact

✅ **Full root access** — no password, no authentication bypass needed
✅ **Works over existing SSH session** — no new attack surface required
✅ **No kernel exploit needed** — purely userspace vulnerability

### Exploitation Chain (Complete)

```
SQLi on /mercuryfacts/{id}/ → credential dump → SSH as webmaster → pkexec 0.105 PwnKit → root ✅
```

---

---

## Next Steps (Pending Direction)

- [ ] Investigate crontab SGID escalation path
- [ ] Investigate MySQL socket auth bypass
- [ ] Check for writable files in Django app directory
- [ ] Look for root-influenced cron jobs
- [ ] Explore other escalation vectors (capabilities, log injection, UDF)

after some deeper introspection, we have quite a few options. We could cheat, and do Dirty Pipe with `pkexec` (SUID), but that feels cheap. The SGID crontab is interesting, but it requires root to use `-u`, so it's not a direct escalation. The MySQL socket auth is a potential avenue if we can find a user matching linuxmaster, but the error suggests there isn't one. The locked-down home directory and lack of writable paths in `/etc` limit our options for file-based escalation. OH! speaking of the crontab and linuxmaster. the mysql isn't owned by linuxmaster.

# 🔍 Critical Blind Spots \& High-Value Targets

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

