
## What We KNOW (Verified)

| Fact | Source |
|---|---|
| **DB creds:** `qdpmadmin` / `UcVQCMQk2STVeS6J` | `/core/config/databases.yml` |
| **Database:** `qdpm`, host `localhost` | Same file |
| **Admin email in config:** `admin@localhost.com` | `configuration` table, id=1 |
| **Admin password hash:** `$P$EWiAHFbjf82GNfe8cVyX6pPtrpyEFd1` | `configuration` table, id=2 |
| **Hash format:** phpass `$P$` (MD5-based, 8192 rounds) | Hash prefix |
| **Users table:** EMPTY — zero rows | MySQL query |
| **john couldn't crack it** | rockyou.txt failed |
| **Login form fields:** `login[email]`, `login[password]`, `remember_me=1`, `http_referer` | Burp capture |
| **No CSRF token** on login form | Burp capture |
| **Session cookie:** `qdPM8=<sid>` | Response header |

## What We DON'T KNOW (Assumptions)

| Assumption | Risk |
|---|---|
| qdPM checks `configuration` table for admin creds vs `users` table | Could be either, or both |
| phpass hash in config matches what login verification expects | Maybe it's stored differently than expected |
| Inserting a user into `users` table will work | Table is empty — maybe users are created on first login? |
| The hash uses standard phpass MD5 implementation | Could be custom salt/rounds |

## The Core Problem

We have the **hash** but can't crack it, and we don't know if qdPM's auth checks:
1. The `configuration` table (id=2) for admin password
2. The `users` table for user credentials
3. Both tables
4. Something else entirely (LDAP? hardcoded?)

## Next Steps (Options)

**A.** Use CSRF on the **password reset** endpoint to set a known password
**B.** Check if qdPM has a **default install script** that creates users with known creds
**C.** Look at the **qdPM source code** in `/core/` to find the exact auth verification logic
**D.** Try the **ZAP API** (you just installed it) for automated CSRF exploitation

Which path feels right? 🎯

THE FACTS BB. Dexter always coming in clear and ready at a moments notice to lay out the facts and keep us on track. I appreciate that.