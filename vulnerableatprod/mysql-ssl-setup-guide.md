cat# MySQL SSL Authentication - Kali Setup Guide

## Target: Metasploitable2 VM (MySQL with SSL)

### Prerequisites

```bash
# Install MySQL client on Kali
sudo apt update && sudo apt install -y mysql-client
```

### Step 1: Place Keys in a Directory

Create a dedicated directory for the keys:

```bash
mkdir -p ~/.mysql-ssl-keys
cd ~/.mysql-ssl-keys

# Copy your keys here (from copypastebb.txt or wherever they're stored)
# You need these 3 files on the CLIENT side:
#   ca.pem       - CA certificate (trust anchor)
#   client-cert.pem  - Your client certificate
#   client-key.pem   - Your client private key
```

### Step 2: Verify Key Pair Matches

The client cert and key must be a matching pair:

```bash
# Check modulus of both - they should match
openssl x509 -noout -modulus -in client-cert.pem | openssl md5
openssl rsa -noout -modulus -in client-key.pem | openssl md5
# Both outputs should be IDENTICAL
```

### Step 3: Connect via MySQL CLI

```bash
mysql --ssl-ca=~/.mysql-ssl-keys/ca.pem \
      --ssl-cert=~/.mysql-ssl-keys/client-cert.pem \
      --ssl-key=~/.mysql-ssl-keys/client-key.pem \
      -h 192.168.0.24 \
      -u root \
      -p
```

Or create a config file (`~/.my.cnf`) so you don't type it every time:

```ini
[client]
host = 192.168.0.24
user = root
ssl-ca = /home/kali/.mysql-ssl-keys/ca.pem
ssl-cert = /home/kali/.mysql-ssl-keys/client-cert.pem
ssl-key = /home/kali/.mysql-ssl-keys/client-key.pem
```

Then just run:
```bash
mysql -u root -p
```

### Step 4: Verify SSL Connection

Once connected in MySQL, run:

```sql
SHOW STATUS LIKE 'Ssl_cipher';
```

If it returns a cipher name (not empty), you're connected over SSL.

---

## Alternative: Connect via Metasploit

```bash
msfconsole

# Use the mysql_login module with SSL
use auxiliary/scanner/mysql/mysql_login
set RHOSTS 192.168.0.24
set SSL true
set SSL_CA_FILE /home/kali/.mysql-ssl-keys/ca.pem
set SSL_CERT_FILE /home/kali/.mysql-ssl-keys/client-cert.pem
set SSL_KEY_FILE /home/kali/.mysql-ssl-keys/client-key.pem
set USER_AS_ROOT true
run
[-] 192.168.0.24:3306     - 192.168.0.24:3306 - Unsupported target version of MySQL detected. Skipping.
[*] 192.168.0.24:3306     - Scanned 1 of 1 hosts (100% complete)
[*] 192.168.0.24:3306     - Bruteforce completed, 1 credential was successful.
[*] 192.168.0.24:3306     - You can open an MySQL session with these credentials and CreateSession set to true
[*] Auxiliary module execution completed
`
openssl s_client -connect 192.168.0.24:3306 -CAfile /home/kali/.mysql-ssl-keys/ca.pem

== > If you see "SSL connection error", the server may not require SSL. Try without the SSL options to confirm.
```

without ssl
``` bash
    use auxiliary/scanner/mysql/mysql_login
    set RHOSTS 192.168.0.24
    set USER_AS_ROOT true
    run
```
<!-- its the version of mysql that is the problem. it is too old and not supported by metasploit. so i have to use the mysql client instead.. man i'm learning alot of new stuff today. -->
---

## Alternative: Connect via Python

```python
import mysql.connector

conn = mysql.connector.connect(
    host="192.168.0.24",
    user="root",
    ssl_ca="/home/kali/.mysql-ssl-keys/ca.pem",
    ssl_cert="/home/kali/.mysql-ssl-keys/client-cert.pem",
    ssl_key="/home/kali/.mysql-ssl-keys/client-key.pem"
)
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
print(cursor.fetchone())
```

Install: `pip install mysql-connector-python`

---

## What Each Key Does

| File | Purpose | Needed on Client? |
|------|---------|-------------------|
| `ca.pem` | CA certificate - proves server identity | YES |
| `client-cert.pem` | Your client identity certificate | YES |
| `client-key.pem` | Your private key (proves you own the cert) | YES |
| `server-cert.pem` | Server's certificate | NO (you get this from server) |
| `server-key.pem` | Server's private key | NO - NEVER share this |
| `*-req.pem` | Certificate requests | NO - intermediate files |

---

## Troubleshooting

```bash
# Test SSL connectivity manually
openssl s_client -connect 192.168.0.24:3306 -CAfile /home/kali/.mysql-ssl-keys/ca.pem

# Check if MySQL is listening on the target
nmap -p 3306 192.168.0.24

# Verify MySQL requires SSL (if configured to do so)
mysql -h 192.168.0.24 -u root --skip-ssl   # try without SSL first
```

If connection fails with "SSL connection error", the server may not require SSL — try without the `--ssl-*` flags. If it says "Access denied", you may need credentials in addition to the certs.

they really made this one hard. nothing is dated to the version needed for exploitation. metasploit doesn't support this version 