# Nmap 7.99 scan

## Nmap command

```bash
    Nmap scan report for 192.168.56.102
    Host is up (0.0037s latency).
    Not shown: 999 closed tcp ports (reset)
    PORT   STATE SERVICE    VERSION
    80/tcp open  tcpwrapped
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-server-header: Apache
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).

    TRACEROUTE
    HOP RTT     ADDRESS
    1   3.74 ms 192.168.56.102

    Nmap scan report for 192.168.56.103
    Host is up (0.0041s latency).
    Not shown: 997 closed tcp ports (reset), 1 filtered tcp port (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE    VERSION
    22/tcp open  tcpwrapped
    80/tcp open  tcpwrapped
    | http-csrf: 
    | Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.56.103
    |   Found the following possible CSRF vulnerabilities: 
    |     
    |     Path: http://192.168.56.103:80/
    |     Form id: 
    |     Form action: /index.php
    |     
    |     Path: http://192.168.56.103:80/register.php
    |     Form id: 
    |_    Form action: /register.php
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-server-header: Apache/2.4.41 (Ubuntu)
    | http-cookie-flags: 
    |   /: 
    |     PHPSESSID: 
    |_      httponly flag not set
    |_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.11 ms 192.168.56.103

    Nmap scan report for 192.168.56.112
    Host is up (0.0045s latency).
    Not shown: 990 closed tcp ports (reset), 9 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE    VERSION
    80/tcp open  tcpwrapped
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-trace: TRACE is enabled
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_http-server-header: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.51 ms 192.168.56.112

    Nmap scan report for 192.168.56.114
    Host is up (0.0042s latency).
    Not shown: 985 closed tcp ports (reset), 12 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT    STATE SERVICE    VERSION
    22/tcp  open  tcpwrapped
    135/tcp open  tcpwrapped
    445/tcp open  tcpwrapped
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).

    Host script results:
    |_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: EOF
    |_smb-vuln-ms10-054: false
    |_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: EOF

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.17 ms 192.168.56.114

    Nmap scan report for 192.168.56.115
    Host is up (0.0044s latency).
    Not shown: 996 closed tcp ports (reset), 1 filtered tcp port (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT     STATE SERVICE    VERSION
    22/tcp   open  tcpwrapped
    80/tcp   open  tcpwrapped
    |_http-server-header: Apache/2.4.48 (Debian)
    | http-enum: 
    |   /backups/: Backup folder w/ directory listing
    |   /robots.txt: Robots file
    |   /batch/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |   /core/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |   /css/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |   /images/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |   /install/: Potentially interesting folder
    |   /js/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |   /manual/: Potentially interesting folder
    |   /template/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |_  /uploads/: Potentially interesting directory w/ listing on 'apache/2.4.48 (debian)'
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    | http-internal-ip-disclosure: 
    |_  Internal IP Leaked: 127.0.0.1
    | http-csrf: 
    | Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.56.115
    |   Found the following possible CSRF vulnerabilities: 
    |     
    |     Path: http://192.168.56.115:80/
    |     Form id: loginform
    |     Form action: http://192.168.56.115/index.php/login
    |     
    |     Path: http://192.168.56.115:80/index.php/login/restorePassword
    |     Form id: restorepassword
    |     Form action: /index.php/login/restorePassword
    |     
    |     Path: http://192.168.56.115:80/index.php/login
    |     Form id: loginform
    |_    Form action: http://192.168.56.115/index.php/login
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    3306/tcp open  tcpwrapped
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.42 ms 192.168.56.115

    OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    # Nmap done at Wed Jun 17 17:22:58 2026 -- 256 IP addresses (255 hosts up) scanned in 283.75 seconds

````
