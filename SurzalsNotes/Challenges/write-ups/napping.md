# Nmap Scan Findings — 192.168.56.103

## Target Overview

| Field | Value |
|---|---|
| **IP** | 192.168.56.103 |
| **OS Guess** | Ubuntu (Apache/2.4.41) |
| **Uptime** | ~28.9 days (since May 18, 2026) |
| **Open Ports** | 80/tcp (HTTP) |
| **Closed Ports** | 988 (reset) |
| **Filtered Ports** | 11 (no-response) |

## Nmap Scan Output

```
Nmap scan report for 192.168.56.103
Host is up (0.0054s latency).
Not shown: 988 closed tcp ports (reset), 11 filtered tcp ports (no-response)

PORT   STATE SERVICE    VERSION
80/tcp open  tcpwrapped
|_http-title: Login
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
```

## HTTP Enumeration Results

### Confirmed Endpoints (200 OK)

| Endpoint | Content-Type | Notes |
|---|---|---|
| `/` | text/html; charset=UTF-8 | Login form, PHP session cookie |
| `/index.php` | text/html; charset=UTF-8 | Same as root — login page |
| `/register.php` | text/html; charset=UTF-8 | Bootstrap sign-up form (username/password/confirm) |
| `/config.php` | text/html; charset=UTF-8 | **⚠️ Empty 200 response (0 bytes)** |

### Forbidden Endpoints (403)

| Endpoint | Notes |
|---|---|
| `/.htaccess` | Forbidden — Apache config file protected |
| `/server-status` | Apache status module enabled but restricted |

### Not Found (404)

| Category | Paths Tested |
|---|---|
| **Auth/Admin** | `login.php`, `admin`, `administrator`, `console`, `dashboard` |
| **CMS** | `wp-login.php` |
| **DB/Config** | `db.php`, `database.php`, `connection.php`, `.env` |
| **Info Disclosure** | `phpinfo.php`, `info.php`, `test.php`, `debug.php` |
| **Backups** | `backup.sql`, `dump.sql`, `source.php` |
| **Version Control** | `git/config`, `.git/config` |
| **Admin Panels** | `phpmyadmin`, `pma`, `mysql` |
| **API/Config** | `api.php`, `api/v1`, `info.json`, `version.json` |
| **Other** | `sitemap.xml`, `crossdomain.xml` |
| **Config Backups** | `config.php.bak`, `.orig`, `.old`, `.save`, `.swp`, `.dist`, `.example`, `.txt`, `.php~` |

## HTTP Headers Analysis

### Login Page (`/`) Response Headers

```http
HTTP/1.1 200 OK
Date: Wed, 17 Jun 2026 00:18:47 GMT
Server: Apache/2.4.41 (Ubuntu)
Set-Cookie: PHPSESSID=t3eemi8a43u3v2voko7k27r9qf; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Type: text/html; charset=UTF-8
```

### Registration Page (`/register.php`) Structure

- **Framework**: Bootstrap 4.5.2 (CDN)
- **Form Action**: `POST /register.php`
- **Fields**: username, password, confirm_password
- **No CAPTCHA** or rate limiting visible
- **Already have account link**: `index.php`

## Security Observations

### High Priority

1. **Empty config.php (200 OK)** — Returns zero bytes. Could indicate:
   - Misconfigured Apache serving PHP source code
   - Intentionally empty placeholder for DB credentials
   - Include-only file with no direct output

2. **PHPSESSID without HttpOnly** — Session cookie lacks HttpOnly flag, enabling potential XSS-based session hijacking

3. **Open Registration** — No CAPTCHA, no email verification visible, no rate limiting

### Medium Priority

4. **Apache 2.4.41 (Ubuntu)** — Released ~2019, potentially vulnerable to known CVEs
5. **server-status enabled** — Apache module present but restricted (403)
6. **.htaccess protected** — File exists but access denied (confirms .htaccess is present)

### Low Priority

7. **No security headers** — No X-Frame-Options, X-Content-Type-Options, CSP, or Strict-Transport-Security
8. **Cache-control set to no-cache** — Good practice for auth pages, but confirms PHP session handling

## Attack Surface Summary

```
192.168.56.103:80
├── GET  /              → Login form (PHPSESSID cookie)
├── POST /             → Authentication attempt
├── GET  /register.php → Open registration (no CAPTCHA)
├── POST /register.php → Account creation
├── GET  /config.php   → Empty response (suspicious)
├── GET  /.htaccess    → 403 Forbidden
└── GET  /server-status → 403 Forbidden
```

## Recommended Next Steps

1. **Test authentication flows** — SQL injection, brute force, default credentials
2. **Exploit registration** — Account creation for privilege escalation path
3. **Investigate config.php** — Try different HTTP methods (POST, PUT, DELETE) or include wrappers
4. **Session testing** — Attempt XSS to steal PHPSESSID (no HttpOnly)
5. **Directory brute-force** — Use ffuf/gobuster with larger wordlists for hidden paths

---
*Scan date: 2026-06-17*
*Scanner: Nmap 7.99 + manual HTTP enumeration*
