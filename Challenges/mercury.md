# MERCURY — Exploitation Summary

## Target

- **IP:** `192.168.56.113`
- **Port 8080/tcp** — Python WSGI (WSGIServer/0.2 CPython/3.8.2)
- **App:** Django + MySQL ("Mercury Facts" — a fact-of-the-day web app)

## Entry Point

- `GET /mercuryfacts/{id}/` — RESTful endpoint returning raw DB results
- Response format: `Fact id: 1. (('Mercury does not have any moons or rings.',),)`
- Barebones HTML — intentionally minimal, no CSS/JS/frameworks

## Vulnerability: SQL Injection (UNION-based)

The `{id}` parameter is **not parameterized** — input goes directly into SQL.

### Proof of Concept

```
GET /mercuryfacts/1 UNION SELECT 1/
→ Returns 2 rows with 1 column each → base query selects 1 column
```

(theres more to this one for the root flag hehe)

webmaster@mercury:~/mercury_proj$ cat notes.txt
Project accounts (both restricted):
webmaster for web stuff - webmaster:bWVyY3VyeWlzdGhlc2l6ZW9mMC4wNTZFYXJ0aHMK
linuxmaster for linux stuff - password is mercurymeandiameteris4880km
webmaster@mercury:~/mercury_proj
(yes it is base64 lololol) its for "linuxmaster" and "mercuryistthesizeof0.056Earths" (webmaster) respectively

### Enumeration

- **DB Type:** MySQL (information_schema available)
- **Users table columns:** `id`, `username`, `password`

## Credentials Dumped

| # | Username    | Password                          |
|---|-------------|-----------------------------------|
| 1 | john        | johnny1987                        |
| 2 | laura       | lovemykids111                     |
| 3 | sam         | lovemybeer111                     |
| 4 | webmaster   | mercuryisthesizeof0.056Earths     |

## Todo List (from `/mercuryfacts/todo`)

- Add CSS
- Implement authentication (using users table) ← **not yet done**
- Use models in Django instead of direct MySQL call ← **root cause of SQLi**
- All the other stuff, so much!!!

## Key Takeaways

1. **Raw SQL queries + user input = SQL injection** — always use ORM/parameterized queries
2. **Hardcoded-style passwords** (johnny1987, lovemykids111) — weak password policy
3. **No authentication implemented** despite "todo" item — app is wide open
4. **robots.txt** returns 200 with `Disallow: /` — CTF misdirection

---

# HOME-RANGE RANGE SCAN SUMMARY

## Scan Details

- **Command:** `nmap --privileged --open -A --script=vuln 192.168.56.114/24`
- **Date:** Mon Jun 15 14:48:40 2026
- **Result:** 3 hosts up in the .11x subnet

---

## Host 1: 192.168.56.112

| Port | Service | Version |
|------|---------|---------|
| 22/tcp | open | tcpwrapped |
| 80/tcp | open | Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9 |

**Notes:**

- TRACE enabled (XSS vector)
- No exact OS match — likely hardened/custom
- **Potential vectors:** TRACE method abuse, Python WSGI enumeration

---

## Host 2: 192.168.56.113 ← MERCURY (EXPLOITED)

| Port | Service | Version |
|------|---------|---------|
| 8080/tcp | open | WSGIServer/0.2 CPython/3.8.2 |

**Notes:**

- Django + MySQL web app
- SQLi on `/mercuryfacts/{id}/` — **CRITICAL**
- Credentials dumped: john, laura, sam, webmaster
- No authentication implemented yet

---

## Host 3: 192.168.56.115

| Port | Service | Version |
|------|---------|---------|
| 22/tcp | open | tcpwrapped |
| 80/tcp | open | Apache/2.4.48 (Debian) |

**Interesting directories (directory listing enabled):**

- `/backups/` — **backup files!**
- `/install/` — **installer still present!**
- `/uploads/` — file upload directory
- `/batch/`, `/core/`, `/css/`, `/images/`, `/js/`, `/manual/`, `/template/`

**CSRF vulnerability found:**

- Form `loginform` → `index.php/login` (no CSRF token)

**Internal IP disclosure:** 127.0.0.1 leaked via http-internal-ip-disclosure script

**Potential vectors:**

1. `/install/` — run installer or find leftover install scripts
2. `/backups/` — download DB/code backups for creds
3. `/uploads/` — file upload → RCE
4. CSRF on login form — session hijack
5. Default CMS credentials (looks like a PHP-based CMS)

---

## Overall Risk Assessment

| Host | Risk Level | Primary Attack Vector |
|------|-----------|---------------------|
| .112 | Medium | TRACE method, WSGI enumeration |
| .113 | **CRITICAL** ✅ | SQLi → credential dump |
| .115 | High | Install dir, backups, CSRF, uploads |

## Recommended Next Targets

1. **192.168.56.115** — `/install/` and `/backups/` are low-hanging fruit
2. **192.168.56.112** — TRACE + WSGI enumeration
3. Revisit **.113** with dumped creds for SSH/login brute force

before i go out to smoke we have 3 possibilities for bypassing this

msf

sqlmap

direct integration from agent chat to browser but that requires a different MCP toolkit than Playwright. After multiple attempts, the workflow for the agent to use Playwright to interact with the web app and extract data is too cumbersome and error-prone, especially for complex SQLi payloads. The agent would need to handle encoding, session management, and parsing responses, which adds a lot of overhead compared to using a dedicated tool like sqlmap or Metasploit. Yeth.

i can delegate tasks? what. i can delegate tasks to other agents? what.

# Task Delegation to Specialized Agents

Given the complexity of the SQL injection exploitation and the need for reliable tools, we can delegate specific tasks to specialized agents that are designed for these purposes. Here's how we can break down the tasks: (i get it, don't use the same end point for different logic branches, but still, this is a CTF, we can be flexible with the workflow)

1. **Reconnaissance and Enumeration Agent**
   - Task: Perform detailed enumeration of the target web application, including parameter analysis, response parsing, and identifying potential injection points.
   - Tools: Custom scripts, Burp Suite, or other web enumeration tools.
wait what if we catagorize the agents by the OWASP Top 10 vulnerabilities? then we can have a SQLi agent, an XSS agent, an RCE agent, etc. that way we can delegate tasks based on the specific vulnerability we're targeting. That would allow us to have specialized agents that are optimized for each type of vulnerability, and we can easily delegate tasks to the appropriate agent based on the findings from our reconnaissance phase. For example, if we identify a potential SQL injection point, we can delegate the exploitation task to the SQLi agent, which can then use tools like sqlmap or Metasploit to automate the exploitation process. This would streamline our workflow and increase our chances of successfully exploiting the vulnerability.

all agents should have baked in they need to report attempts and results back to the main agent, so we can keep track of what has been tried and what the outcomes were. This way, we can avoid redundant attempts and also have a clear record of our actions for analysis and reporting purposes. Each specialized agent can have its own reporting mechanism that feeds into a centralized logging system, allowing us to monitor progress and make informed decisions on next steps based on the results received from each agent.
