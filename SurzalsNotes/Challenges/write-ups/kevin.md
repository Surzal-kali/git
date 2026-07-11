# Nmap 7.99 scan initiated Fri Jul 10 12:13:51 2026 as: /usr/lib/nmap/nmap --privileged -sC -sV --script=vuln -oN kevin.md 192.168.219.45
Nmap scan report for 192.168.219.45
Host is up (0.069s latency).
Not shown: 989 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
80/tcp    open  http         GoAhead WebServer
|_http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
| http-enum: 
|   /cgi-bin/mj_wwwusr: Majordomo2 Mailing List
|   /cgi-bin/vcs: Mitel Audio and Web Conferencing (AWC)
|   /cgi-bin/ffileman.cgi?: Ffileman Web File Manager
|   /cgi-bin/ck/mimencode: ContentKeeper Web Appliance
|   /cgi-bin/masterCGI?: Alcatel-Lucent OmniPCX Enterprise
|   /cgi-bin/awstats.pl: AWStats
|   /cgi-bin/image/shikaku2.png: TeraStation PRO RAID 0/1/5 Network Attached Storage
|   /cgi-bin2/: Potentially interesting folder
|_  /cgi-bin/: Potentially interesting folder
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-sql-injection: ERROR: Script execution failed (use -d to debug)
|_http-server-header: GoAhead-Webs
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=192.168.219.45
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://192.168.219.45:80/index.asp
|     Form id: 
|     Form action: /goform/formLogin
|     
|     Path: http://192.168.219.45:80/index.asp?Message=Invalid user name or password.
|     Form id: 
|_    Form action: /goform/formLogin
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
|_ssl-ccs-injection: No reply from server (TIMEOUT)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: KEVIN; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Jul 10 12:21:02 2026 -- 1 IP address (1 host up) scanned in 431.83 seconds

Now, this guy is very obvious either login_form or file_upload. both sit under windows/http/hp<variant>

C'est la vie, I will have to look into if WSL blocks reverse shells or not D: 