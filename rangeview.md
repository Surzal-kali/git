# Nmap 7.99 scan

## Nmap command

```bash
    Nmap scan report for 192.168.56.102
    Host is up (0.0051s latency).
    Not shown: 986 closed tcp ports (reset), 13 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT   STATE SERVICE    VERSION
    80/tcp open  tcpwrapped
    |_http-title: Revive Cybertron
    |_http-favicon: Unknown favicon MD5: 7ACBCCAFA3EFCAB42272019300F67538
    |_http-server-header: Apache
    | http-methods: 
    |_  Supported Methods: HEAD GET POST OPTIONS
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).
    Uptime guess: 18.549 days (since Fri May 29 04:48:22 2026)
    TCP Sequence Prediction: Difficulty=258 (Good luck!)
    IP ID Sequence Generation: Randomized

    TRACEROUTE
    HOP RTT     ADDRESS
    1   5.13 ms 192.168.56.102

    Nmap scan report for 192.168.56.103
    Host is up (0.0054s latency).
    Not shown: 988 closed tcp ports (reset), 11 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
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
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).
    Uptime guess: 28.909 days (since Mon May 18 20:10:38 2026)
    TCP Sequence Prediction: Difficulty=259 (Good luck!)
    IP ID Sequence Generation: Randomized

    TRACEROUTE
    HOP RTT     ADDRESS
    1   5.45 ms 192.168.56.103

    Nmap scan report for 192.168.56.112
    Host is up (0.0047s latency).
    Not shown: 996 closed tcp ports (reset), 2 filtered tcp ports (no-response)
    Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
    PORT    STATE SERVICE        VERSION
    80/tcp  open  tcpwrapped
    |_http-title: Bad Request (400)
    |_http-server-header: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
    443/tcp open  ssl/tcpwrapped
    | tls-alpn: 
    |_  http/1.1
    |_http-server-header: Apache/2.4.51 (Fedora) OpenSSL/1.1.1l mod_wsgi/4.7.1 Python/3.9
    | http-methods: 
    |   Supported Methods: OPTIONS HEAD GET POST TRACE
    |_  Potentially risky methods: TRACE
    |_http-title: Test Page for the HTTP Server on Fedora
    |_ssl-date: TLS randomness does not represent time
    | ssl-cert: Subject: commonName=earth.local/stateOrProvinceName=Space
    | Subject Alternative Name: DNS:earth.local, DNS:terratest.earth.local
    | Issuer: commonName=earth.local/stateOrProvinceName=Space
    | Public Key type: rsa
    | Public Key bits: 4096
    | Signature Algorithm: sha256WithRSAEncryption
    | Not valid before: 2021-10-12T23:26:31
    | Not valid after:  2031-10-10T23:26:31
    | MD5:     4efa 65d2 1a9e 0718 4b54 41da 3712 f187
    | SHA-1:   04db 5b29 a33f 8076 f16b 8a1b 581d 6988 db25 7651
    |_SHA-256: e85f 5eac 6004 faef 0317 41fb 8f0c 8f3c ede4 56aa f485 41ce d5c4 822d 609c 04f6
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).
    Uptime guess: 31.545 days (since Sat May 16 04:54:38 2026)
    TCP Sequence Prediction: Difficulty=258 (Good luck!)
    IP ID Sequence Generation: Randomized

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.69 ms 192.168.56.112

    Nmap scan report for 192.168.56.113
    Host is up (0.0045s latency).
    Not shown: 999 closed tcp ports (reset)
    PORT     STATE SERVICE    VERSION
    8080/tcp open  tcpwrapped
    | http-methods: 
    |_  Supported Methods: GET HEAD OPTIONS
    | http-robots.txt: 1 disallowed entry 
    |_/
    |_http-title: Site doesn't have a title (text/html; charset=utf-8).
    Aggressive OS guesses: Aastra 57i VoIP phone (96%), Avaya P130 workgroup switch (96%), FreeBSD 4.7-STABLE (96%), Slingmedia Slingbox AV TV over IP gateway (95%), IBM AIX 5.3 (94%), Scientific Atlanta WebSTAR EPC2203 cable modem (93%), Ricoh Aficio MP C4501 printer (92%), Schweitzer Engineering SEL-2701 Ethernet processor (92%), Sony Ericsson P1i mobile phone (Symbian OS 9.1) (91%), Apple iPod touch audio player (iPhone OS 2.2) (91%)
    No exact OS matches for host (test conditions non-ideal).
    Uptime guess: 36.008 days (since Mon May 11 17:48:13 2026)
    TCP Sequence Prediction: Difficulty=263 (Good luck!)
    IP ID Sequence Generation: Randomized

    TRACEROUTE
    HOP RTT     ADDRESS
    1   4.54 ms 192.168.56.113

````
