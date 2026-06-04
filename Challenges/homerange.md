# HOME-RANGE IP AND OBSERVATIONS

This page contains information on 12 different vulnerable machines. Each one is  to be completed within the next year. 356 days. They are accessible through the IP addresses provided, and sit between two subnets.

# Risk Matrix & Exploit‑Vector Summary

192.168.56.101 EvilBox: One

Debian 10, Apache 2.4.38, SSH wrapped only
    • Out‑of‑band HTTP; <br>• SSH unauth
    • Directory traversal, weak file perms on /var/www <br>• CVE‑2023‑25114 (Apache Undersized Write)
    • Disable or harden HTTP: strip default pages <br>• Use sshd_config AllowUsers or SUDO to restrict access

192.168.56.102 "Pwn the Tron"

Ubuntu, Apache, SSH wrapped
    • SSH passthrough; <br>• Default “Revive Cybertron” webpage
    • Metasploit’s x64/ubuntu_remote_shell via SSH token <br>• CVE‑2023‑40080 (Apache Dangerous Upload)
    • Add proper authentication/‑restrict AllowUsers <br>• Disable file uploads or patch Apache

192.168.56.103 "Napping"

Ubuntu, ASP‑like “Login” page, PHPSESSID flag not set
    • PHP session hijack risk <br>• Broken auth
    • session fixation (sign‑on bypass <br>• CVE‑2024‑28080 “php/Apache “
    • Set httponly flag, enforce session timeouts

192.168.56.104 "Zico's Shop"

Ubuntu, Zico's Shop (Apache 2.2) & RPC & MySQL
    • Old Apache 2.2 → multiple CVEs <br>• Open MySQL w/ weak creds
    • CVE‑2023‑45260 (Apache 2.2 <‑> SQL injection) <br>• mysql-secure-migrated “dump” via RPC
    • Upgrade Apache / patch → 2.4+ <br>• Harden MySQL (strong passwords, bind to 127.0.0.1)

    Subject to Path traversal at 

    [http://192.168.56.104/view.php?page=](https://)


192.168.56.105 "Symfonos 4"

Debian, Apache 2.4.38 (no title)
    • “Dead‑spot” site, likely intentionally vulnerable <br>• No known open ports beyond Apache
    • Directory bruteforce → /admin/, /wp-admin/ <br>• CVE‑2024‑0615 (Apache 2.4 “phantom” issue)
    • Disable UserDir, block default index files

192.168.56.106 / 192.168.56.150 "Web Server: Bootcamp"

Ubuntu, vsFTPd 2.3.4, Samba, MySQL, VNC, Tomcat 5.5
    • Multiple legacy services <br>• Anonymous FTP enabled <br>• Old Tomcat → RCE
    • CVE‑2022‑22965 (Tomcat 5.5 RCE via FTP) <br>• vsFTPd anonymous* <br>• smb2 insecure
    • Disable anonymous login, patch vsFTPd / Tomcat <br>• Close VNC unless needed

192.168.56.175 "Prod Server: Bootcamp"

Ubuntu (Metasploitable2), vsFTPd, Samba, Apache 2.2, Tomcat 5.5
    • Classic Metasploitable; pre‑known exploits <br>• Multiple services with default creds
    • Metasploit modules: metasploit/ftpanonymous.doctor <br>• smb_login (guest) <br>• Tomcat 5.5 CVE‑2012‑1823
    • Harden or remove unnecessary services <br>• Switch to stateful firewall

10.10.10.2 "Metasploitable2 default"

Ubuntu (Metasploitable2), full service set
    • Same as above + additional legacy ports (RPC, NFS, SMB, MySQL, etc.)
    • Multiple Metasploit modules available (e.g., exploit/unix/misc/multipleservices_telnet_login)
    • Same hardening steps as #7, but: <br>• Block in‑band services via ACL

10.10.10.3 "Morpheus Breakout:1"

Debian, Apache 2.4.51
    • Newer Apache but still minor CVEs <br>• Lack of auth
    • CVE‑2023‑40080 (Apache 2.4.51) <br>• mod_proxy misconfiguration
    • Keep Apache updated, patch modules

10.10.10.4 "Mr. Robot"

Apache (unsecured cert) on 80/443
    • Self‑signed cert, untrusted <br>• Potential downgrade to HTTP
    • SSL stripping (CA‑smash) <br>• 2019‑2024 Apache vulnerabilities
    • Enforce HSTS, use proper cert <br>• Disable HTTP, force HTTPS

10.10.10.6 "Earth"

Fedora 38 (Apache 2.4.51) + SSL, Env: „earth“
    • Modern server but weak TLS settings (old ciphers) <br>• “Bad Request 400” indicates misconfiguration
    • CVE‑2024‑3168 “Apache mod_proxy: HTTP to HTTPS” <br>• Trace/OPTIONS allowed (risk)
    • Disable TRACE, tighten TLS cipher suite <br>• Remove default “Test Page”