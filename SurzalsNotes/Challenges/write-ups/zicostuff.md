# Vulnhub Summary
Level: Intermediate

Goal: Get root and read the flag file

Description:

Zico is trying to build his website but is having some trouble in choosing what CMS to use. After some tries on a few popular ones, he decided to build his own. Was that a good idea?

Hint: Enumerate, enumerate, and enumerate!

## Nmap 7.99 scan initiated Mon Jun 22 20:21:36 2026 as: /usr/lib/nmap/nmap --privileged --open -sC -sV -O -oN zicostuff.txt 192.168.1.102

Nmap scan report for 192.168.1.102
Host is up (0.00074s latency).
Not shown: 997 closed tcp ports (reset)
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
| 1024 68:60:de:c2:2b:c6:16:d8:5b:88:be:e3:cc:a1:25:75 (DSA)
| 2048 50:db:75:ba:11:2f:43:c9:ab:14:40:6d:7f:a1:ee:e3 (RSA)
|_ 256 11:5d:55:29:8a:77:d8:08:b4:00:9b:a3:61:93:fe:e5 (ECDSA)
80/tcp open http Apache httpd 2.2.22 ((Ubuntu))
|\_http-server-header: Apache/2.2.22 (Ubuntu)
|\_http-title: Zico's Shop
111/tcp open rpcbind 2-4 (RPC #100000)
| rpcinfo:
| program version port/proto service
| 100000 2,3,4 111/tcp rpcbind
| 100000 2,3,4 111/udp rpcbind
| 100000 3,4 111/tcp6 rpcbind
| 100000 3,4 111/udp6 rpcbind
| 100024 1 40496/udp6 status
| 100024 1 47021/tcp6 status
| 100024 1 51633/udp status
|_ 100024 1 59668/tcp status
Aggressive OS guesses: 3Com Baseline Switch 2924-SFP or Cisco ESW-520 switch or Allied Telesis AT-8000 series switch (86%), Allied Telesis AT-8000S; Dell PowerConnect 2824, 3448, 5316M, or 5324; Linksys SFE2000P, SRW2024, SRW2048, or SRW224G4; or TP-LINK TL-SL3428 switch (86%), Aruba, Cisco, or Netgear switch (Linux 3.10 or 4.4) (86%), Linksys SRW2008MP switch (86%), Google Fuchsia (86%), Cisco SG 300-10, Dell PowerConnect 2748, Linksys SLM2024, SLM2048, or SLM224P, or Netgear FS728TP or GS724TP switch (86%), Linksys SRW2000-series or Allied Telesyn AT-8000S switch (86%), Cisco SRW2008-K9 switch (85%), OpenBSD 5.5 (85%)
No exact OS matches for host (test conditions non-ideal).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

# Nmap done at Mon Jun 22 20:21:51 2026 -- 1 IP address (1 host up) scanned in 15.25 seconds

Summary of Findings

     1. Nmap Scan:
        - The initial Nmap scan revealed several open ports:
          - SSH (Port 22): Running OpenSSH 5.9p1 on Ubuntu.
          - HTTP (Port 80): Apache httpd 2.2.22 running on Ubuntu.
          - RPCBIND (Port 111): Active and running.

     2. Path Traversal Testing:
        - We tested path traversal vulnerabilities to access sensitive files:
          - /etc/passwd was successfully accessed via http://192.168.1.102/view.php?page=../../../../etc/passwd.
          - Attempts to access /etc/shadow and .bash_history did not yield results.

     3. Directory Listing:
        - We used FFUf with a custom wordlist to identify potential directories and files.
        - Directories like /var/www, /home/zico, /etc, and .git were identified as potentially accessible.

     4. File Upload Attempt:
        - Attempted to upload eatthis.sh to /var/www/html/uploads using:
     1      curl -T /home/surzal/git/Challenges/payloads/eatthis.sh
       http://192.168.1.102/view.php?page=../../../../var/www/html/uploads/
        - The upload did not produce visible output.

     5. Verification of Upload:
        - Checked if the file was uploaded by attempting to access it:
     1      curl http://192.168.1.102/view.php?page=../../../../var/www/html/uploads/eatthis.sh
        - No visible output, implying either success or restriction.

     - Verification:
       - Verify if the file upload was successful by checking if eatthis.sh is executable. (it was not)

     - Further Queries:
       - You mentioned querying OpenCVE for any known vulnerabilities related to path traversal attacks on Apache and
         PHP configurations. Once you have that information, we can proceed with next steps accordingly.
alright so we have a few things we can do

     6. Directory Listing - /img/:
        - Confirmed directory listing enabled at http://192.168.1.102/img/
        - Files visible: (to be documented after review)
        - Potential for identifying image upload patterns, CMS structure, or sensitive files

#### APACHE2/CONFIG

ServerAdmin webmaster@localhost DocumentRoot /var/www Options FollowSymLinks AllowOverride None Options Indexes FollowSymLinks MultiViews AllowOverride None Order allow,deny allow from all ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/ AllowOverride None Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch Order allow,deny Allow from all ErrorLog ${APACHE_LOG_DIR}/error.log # Possible values include: debug, info, notice, warn, error, crit, # alert, emerg. LogLevel warn CustomLog ${APACHE_LOG_DIR}/access.log combined Alias /doc/ "/usr/share/doc/" Options Indexes MultiViews FollowSymLinks AllowOverride None Order deny,allow Deny from all Allow from 127.0.0.0/255.0.0.0 ::1/128 