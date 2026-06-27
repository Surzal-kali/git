📋 Current Facts (Zico Shop / 192.168.1.102)
🔍 Recon & Enumeration
Target IP: 192.168.1.102 [1]
OS Fingerprint: Ubuntu Linux, Apache 2.2.22 (PHP/MySQL stack), OpenSSH 5.9p1 → strongly suggests MySQL ≤ 5.x era
Services open: SSH 22, HTTP 80, RPCBIND 111 [1]
Vulnerability found: Path traversal on /view.php?page= allowing arbitrary file read (null-byte truncated)
🗂️ What We've Read / Tried
FILE/PATH
RESULT
/etc/passwd
Confirmed user zico (UID 1000) [2]
Apache config (000-default.conf)
Yielded useful info about virtual hosts/dirs — you have the snippet but said it doesn't need pasting right now
/var/www/config.php
Dead end — no creds exposed [6]
~/.bash_history (zico)
Dead end — empty or scrubbed [6]


🕵️ Directory Bruteforcing
Ran dirb big.txt against the web server
Found /dbadmin/ → redirects to test-dbadmin.php which exposes a MySQL admin/test page
🔑 Credential Discovery
You pulled this table from that DB test page:

NAME
HASH
ID
root
653F4B285089453FE00E2AAFAC573414
1
zico
96781A607F4E9F5F423AC01F0DAB0EBD
2

(Surzals Notes)
WE GOT IT. The zico password is zico2215@ and the root password is 34kroot34 neither works for ssh but i'll try other avenues :D