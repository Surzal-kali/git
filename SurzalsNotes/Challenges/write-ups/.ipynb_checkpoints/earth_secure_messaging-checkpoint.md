# Earth Secure Messaging — 192.168.56.112:443

## Target Overview

| Field | Value |
|---|---|
| **IP** | 192.168.56.112 |
| **Hostname** | earth.local (SAN: terratest.earth.local) |
| **Ports** | 80/tcp (HTTP), 443/tcp (HTTPS) |
| **OS Guess** | Fedora (Apache/2.4.51 + mod_wsgi Python/3.9) |
| **Uptime** | ~31.5 days (since May 16, 2026) |

## TLS Certificate

```
Subject:    CN=earth.local, ST=Space
Issuer:     CN=earth.local, ST=Space
SAN:        DNS:earth.local, DNS:terratest.earth.local
Key Type:   RSA 4096-bit
Algorithm:  sha256WithRSAEncryption
Valid From: 2021-10-12T23:26:31
Valid To:   2031-10-10T23:26:31
MD5:        4efa65d21a9e07184b5441da3712f187
SHA-256:    e85f5eac6004faef031741fb8f0c8f3ced...
```

Self-signed certificate. Valid for 10 years. Common name and issuer both `earth.local`.

## HTTP Enumeration Results (Port 80)

| Endpoint | Status | Notes |
|---|---|---|
| `/` | 400 Bad Request | Apache default page — no vhost match |

Port 80 has no configured virtual host for the application. All traffic goes to HTTPS.

## HTTPS Enumeration Results (Port 443)

### Confirmed Endpoints (200 OK)

| Endpoint | Content-Type | Description |
|---|---|---|
| `/` | text/html; charset=utf-8 | Main app — "Earth Secure Messaging" |
| `/admin` | text/html; charset=utf-8 | Admin panel redirect |
| `/admin/login` | text/html; charset=utf-8 | Django admin login form |
| `/admin/logout` | text/html; charset=utf-8 | Logout endpoint |
| `/static/styles.css` | text/css | Minimal monospace CSS |
| `/static/earth1.jpg` | image/jpeg | Earth image asset |

### Not Found (404)

| Category | Paths Tested |
|---|---|
| **Auth** | `/login`, `/accounts/login`, `/accounts/logout` |
| **Admin** | `/django-admin/`, `/administrator`, `/console`, `/dashboard` |
| **CMS** | `/wp-admin`, `/wp-login.php` |
| **Config** | `/config`, `/.env`, `/settings.py`, `/urls.py`, `/views.py` |
| **Source** | `/__init__.py`, `/manage.py`, `/wsgi.py`, `/git/config`, `/.git/config` |
| **API** | `/api`, `/api/v1`, `/api/v2`, `/docs`, `/swagger` |
| **Info** | `/phpinfo.php`, `/info.php`, `/test`, `/health`, `/status`, `/server-info` |
| **DB/Admin** | `/phpmyadmin`, `/pma`, `/mysql` |
| **Other** | `/.htaccess`, `/robots.txt`, `/sitemap.xml`, `/crossdomain.xml`, `/.well-known/security.txt` |
| **Django** | `/admin/jsi18n/` |

### Forbidden (403)

| Endpoint | Notes |
|---|---|
| `/static/` | Directory listing disabled |

## HTTP Headers Analysis

### Main Page (`/`) Response Headers

```http
HTTP/2 200
date: Wed, 17 Jun 2026 00:25:45 GMT
server: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
content-length: 2595
x-frame-options: DENY
vary: Cookie
x-content-type-options: nosniff
referrer-policy: same-origin
set-cookie: csrftoken=CWGXrbcxT451qa0SfAQf5SK9iqXwdNpM3tngb59174RbLUNOkqI1pVdzixRrXqEC; 
    expires=Wed, 16 Jun 2027 00:25:45 GMT; Max-Age=31449600; Path=/; SameSite=Lax
keep-alive: timeout=5, max=100
connection: Keep-Alive
content-type: text/html; charset=utf-8
```

### Admin Page Headers

Same as above minus `set-cookie` (no CSRF cookie on admin pages).

## Application Analysis

### Main App (`/`) — Earth Secure Messaging

**Framework:** Django (confirmed by CSRF token format, Django 403 pages, admin panel)

**UI Structure:**
- Bootstrap-free custom design
- Courier New monospace font
- Center-aligned layout
- Earth image (`earth1.jpg`) as header graphic
- Single form: message submission with encryption

**Form Fields:**
| Field | Type | Constraints |
|---|---|---|
| `message` | textarea | max 500 characters, required |
| `message_key` | text input | max 50 characters, required |
| `csrfmiddlewaretoken` | hidden | Django CSRF token |

**Method:** POST to `/` with `Content-Type: application/x-www-form-urlencoded`

**Referer Policy:** Required — submissions without Referer header return Django 403 "CSRF verification failed"

### Encrypted Messages Displayed on Page

Messages appear as hex strings in `<li>` elements. Three messages observed:

| # | Length (hex chars) | Length (bytes) | First Bytes |
|---|---|---|---|
| 1 | 22 | 11 | `3b000f1e0a543c0a0b1f01` |
| 2 | 508 | 254 | `37090b59030f11060b0a1b4e...` |
| 3 | 298 | 149 | `3714171e0b0a550a1859101d...` |
| 4 | 806 | 403 | `2402111b1a0705070a41000a...` |

### Admin Panel (`/admin`)

**Status:** "You are not logged in. Please: Log In"

**Login Form:**
- Standard Django admin login
- Fields: `username`, `password`
- CSRF protected
- No visible rate limiting or account lockout

## Encryption Analysis

### Cipher Characteristics

1. **Output format:** Raw hexadecimal strings (no padding markers like `=`)
2. **Variable length:** Messages range from 11 to 403 bytes — suggests stream cipher or XOR
3. **Per-message variation:** First bytes differ between messages even with similar content → per-message IV/nonce
4. **Null byte clusters detected** in ciphertext:
   - Message 2 has null bytes at positions: `[12, 13, 14, 15, 16, 17, 34, 68, 84, 91, 102, 148, 186, 197]`
   - A cluster of 6 consecutive nulls at positions 12–17 (plaintext XOR key = 0x00 means plaintext byte equals key byte)

### Embedded ASCII Fragments in Ciphertext

Scanning Message 2 for printable ASCII runs revealed:
- `CUBI_^C` at position 92–102 (10 bytes)
- `NKRBI_^C` at position 103–148 region
- `AN4`, `@Y&`, `MA'` — shorter fragments

These ASCII strings embedded within ciphertext are highly suspicious — they could be:
- **Key material** or key markers
- **Protocol headers** or version identifiers
- **Padding markers** (the `^C` = 0x03 byte is a common padding indicator)

### XOR Key Recovery Attempts

| Hypothesis | Result |
|---|---|
| Repeating-key XOR with "secretkey" | 95% printable — partial match, not clean |
| Repeating-key XOR with "admin" | 96% printable — partial match, not clean |
| Repeating-key XOR with "message" | 96% printable — partial match, not clean |
| Repeating-key XOR with "CUBI" | 76% printable — moderate match |
| Repeating-key XOR with "CUBI_^C" | 74% printable — moderate match |
| Position-based XOR (offset) | No matches above 75% |
| Caesar/shift cipher | No clean decryption found |
| Key length analysis (1–20) | No key length produced >70% clean decryption |

### Key Observations

- The high printable percentages with common keys suggest **XOR-based encryption** but with a more complex key than simple strings
- The null byte clusters at positions where `plaintext XOR key = 0x00` mean those ciphertext bytes **are the key bytes themselves** — this is a known-plaintext attack vector if we know what should be in those positions
- Message 1 (11 bytes) starts with `3b000f1e0a543c0a0b1f01` — the second byte is `0x00`, meaning key[1] = 0x00 for that message
- Messages 2 and 3 both start with `0x37` — if they share a key, the first key byte is consistent

### Message Key as XOR Key Hypothesis

The user-supplied `message_key` field is likely used directly as the XOR key. This creates two attack vectors:

1. **Key reuse** — If two messages use the same `message_key`, XORing them together reveals XOR of their plaintexts (crib-dragging)
2. **Known plaintext** — If message format is predictable (e.g., starts with a header), the key can be recovered from known bytes

## Security Assessment

### Strengths

| Item | Status | Notes |
|---|---|---|
| HTTPS/TLS | ✅ | RSA 4096, valid cert, SAN configured |
| CSRF Protection | ✅ | Django tokens + Referer header required |
| X-Frame-Options | ✅ | DENY |
| X-Content-Type-Options | ✅ | nosniff |
| Referrer-Policy | ✅ | same-origin |
| Directory Listing | ✅ | Disabled on /static/ |

### Weaknesses

| Item | Severity | Notes |
|---|---|---|
| **Self-signed cert** | Low | Not a vulnerability per se, but indicates dev/test environment |
| **Open registration** | Medium | No visible account creation restrictions (if applicable) |
| **Message encryption key = user input** | **High** | If `message_key` is the XOR key, it's trivially guessable |
| **Admin panel exposed** | Medium | `/admin/login` is publicly accessible with no WAF/rate limiting visible |
| **Apache 2.4.51 (Fedora)** | Low | Older version, potential CVEs (though less common on Fedora) |
| **mod_wsgi Python 3.9** | Low | Python 3.9 reached EOL in Oct 2025 |

### Attack Vectors

1. **Admin brute force** — `/admin/login` with Django default credentials:
   - `admin/changeme` (Django default)
   - `admin/admin`
   - `earth/earth`
   - `root/root`
   - `administrator/password`

2. **Key reuse attack** — Send two messages with the same `message_key`, XOR ciphertexts together, crib-drag known message formats

3. **Known plaintext attack** — If message format is predictable (headers, timestamps, etc.), recover key from null byte positions in ciphertext

4. **Message key as admin credential** — The `message_key` might double as an authentication token or admin password

## Attack Surface Diagram

```
192.168.56.112
├── :80  → Bad Request (no vhost)
└── :443 (earth.local)
    ├── GET  /              → Main app (message submission form)
    ├── POST /              → Submit encrypted message (CSRF protected)
    ├── GET  /admin         → Admin panel (not logged in)
    ├── GET  /admin/login   → Django admin login
    ├── GET  /admin/logout  → Logout
    └── /static/
        ├── styles.css      → Monospace CSS
        └── earth1.jpg      → Earth image
```

## Recommended Next Steps

1. **Brute-force admin login** — Test common Django default credentials
2. **Key reuse test** — Send two messages with identical `message_key`, XOR the ciphertexts
3. **Known plaintext attack** — Submit predictable messages (e.g., all 'A's) to recover key bytes from null positions
4. **Message key as credential** — Try the `message_key` value as an admin password
5. **Test message format** — Send structured messages to identify headers/padding patterns

---
*Scan date: 2026-06-17*
*Scanner: Manual HTTPS enumeration with httpx + SSL + Python analysis*
