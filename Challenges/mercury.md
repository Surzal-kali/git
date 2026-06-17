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

## Remaining Open Questions

1. Can linuxmaster use `crontab -u webmaster` via the SGID binary? (SGID crontab group doesn't grant `-u` privilege)
2. Is there a MySQL user matching linuxmaster with socket auth? (ERROR 1045 says no)
3. Is there a writable file inside the Django app directory? (webmaster home is locked down)
4. Is there a cron job running as root that we can influence? (none found yet)
5. Is there another escalation path entirely? (SUID, capabilities, log injection, MySQL UDF?)

---

## Home-Range Scan Summary (192.168.56.114/24)

| Host | Ports | Risk | Notes |
|------|-------|------|-------|
| **192.168.56.112** | 22/tcp, 80/tcp | Medium | Apache 2.4.51 + mod_wsgi + TRACE enabled (XSS vector) |
| **192.168.56.113** ← MERCURY | 8080/tcp | CRITICAL ✅ | SQLi → credential dump → SSH access |
| **192.168.56.115** | 22/tcp, 80/tcp | High | `/install/`, `/backups/`, `/uploads/` dirs; CSRF on login form |

---

## Next Steps (Pending Direction)

- [ ] Investigate crontab SGID escalation path
- [ ] Investigate MySQL socket auth bypass
- [ ] Check for writable files in Django app directory
- [ ] Look for root-influenced cron jobs
- [ ] Explore other escalation vectors (capabilities, log injection, UDF)

after some deeper introspection, we have quite a few options. We could cheat, and do Dirty Pipe with `pkexec` (SUID), but that feels cheap. The SGID crontab is interesting, but it requires root to use `-u`, so it's not a direct escalation. The MySQL socket auth is a potential avenue if we can find a user matching linuxmaster, but the error suggests there isn't one. The locked-down home directory and lack of writable paths in `/etc` limit our options for file-based escalation. OH! speaking of the crontab and linuxmaster. the mysql isn't owned by linuxmaster.

linuxmaster@mercury:~$ cat /etc/systemd/system/djangotest.service
[Unit]
Description=Start django test server
After=mysql.service

[Service]
Type=simple
ExecStart=/usr/bin/django_testserver
User=webmaster
Group=webmaster

[Install]
WantedBy=multi-user.target
linuxmaster@mercury:~$ ls -la /etc/systemd/system/djangotest.service
-rw-r--r-- 1 root root 193 Sep  1  2020 /etc/systemd/system/djangotest.service
linuxmaster@mercury:~$ ls -la /etc/systemd/system/djangotest.service
-rw-r--r-- 1 root root 193 Sep  1  2020 /etc/systemd/system/djangotest.service

hol up

linuxmaster@mercury:/etc/systemd/system$ ls -la /usr/bin/django_testserver
-rwxr-xr-x 1 root root 85 Sep  1  2020 /usr/bin/django_testserver
linuxmaster@mercury:/etc/systemd/system$ file /usr/bin/django_testserver
/usr/bin/django_testserver: Bourne-Again shell script, ASCII text executable
linuxmaster@mercury:/etc/systemd/system$ strings /usr/bin/django_testserver | grep -i "pass\|secret\|root\|sudo\|"
#!/bin/bash
/usr/bin/python3 /home/webmaster/mercury_proj/manage.py runserver 0:8080
linuxmaster@mercury:/etc/systemd/system$ 

This is interesting. The `djangotest.service` runs as webmaster, but it's owned by root and not writable. However, the `django_testserver` script it executes is also owned by root and not writable. If we can find a way to modify that script or replace it with a symlink to a malicious script, we could potentially escalate to root when the service is restarted.