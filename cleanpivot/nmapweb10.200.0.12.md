nmap web server scan (proper this time with vuln)

<!-- 
┌──(kali㉿kali)-[~]

└─$ nmap 10.200.0.12 --script=vuln -oN webservervulnscan.txt

Starting Nmap 7.95 ( https://nmap.org ) at 2026-06-13 19:22 EDT

Nmap scan report for 10.200.0.12

Host is up (0.018s latency).

Not shown: 977 closed tcp ports (reset)

PORT     STATE    SERVICE

21/tcp   filtered ftp

22/tcp   open     ssh

23/tcp   open     telnet

25/tcp   open     smtp

| ssl-dh-params: 

|   VULNERABLE:

|   Anonymous Diffie-Hellman Key Exchange MitM Vulnerability

|     State: VULNERABLE

|       Transport Layer Security (TLS) services that use anonymous

|       Diffie-Hellman key exchange only provide protection against passive

|       eavesdropping, and are vulnerable to active man-in-the-middle attacks

|       which could completely compromise the confidentiality and integrity

|       of any data exchanged over the resulting session.

|     Check results:

|       ANONYMOUS DH GROUP 1

|             Cipher Suite: TLS_DH_anon_WITH_RC4_128_MD5

|             Modulus Type: Safe prime

|             Modulus Source: postfix builtin

|             Modulus Length: 1024

|             Generator Length: 8

|             Public Key Length: 1016

|     References:

|       https://www.ietf.org/rfc/rfc2246.txt

|   

|   Transport Layer Security (TLS) Protocol DHE_EXPORT Ciphers Downgrade MitM (Logjam)

|     State: VULNERABLE

|     IDs:  CVE:CVE-2015-4000  BID:74733

|       The Transport Layer Security (TLS) protocol contains a flaw that is

|       triggered when handling Diffie-Hellman key exchanges defined with

|       the DHE_EXPORT cipher. This may allow a man-in-the-middle attacker

|       to downgrade the security of a TLS session to 512-bit export-grade

|       cryptography, which is significantly weaker, allowing the attacker

|       to more easily break the encryption and monitor or tamper with

|       the encrypted stream.

|     Disclosure date: 2015-5-19

|     Check results:

|       EXPORT-GRADE DH GROUP 1

|             Cipher Suite: TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA

|             Modulus Type: Safe prime

|             Modulus Source: Unknown/Custom-generated

|             Modulus Length: 512

|             Generator Length: 8

|             Public Key Length: 512

|     References:

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4000

|       https://weakdh.org

|       https://www.securityfocus.com/bid/74733

|   

|   Diffie-Hellman Key Exchange Insufficient Group Strength

|     State: VULNERABLE

|       Transport Layer Security (TLS) services that use Diffie-Hellman groups

|       of insufficient strength, especially those using one of a few commonly

|       shared groups, may be susceptible to passive eavesdropping attacks.

|     Check results:

|       WEAK DH GROUP 1

|             Cipher Suite: TLS_DHE_RSA_WITH_DES_CBC_SHA

|             Modulus Type: Safe prime

|             Modulus Source: postfix builtin

|             Modulus Length: 1024

|             Generator Length: 8

|             Public Key Length: 1024

|     References:

|_      https://weakdh.org

| ssl-poodle: 

|   VULNERABLE:

|   SSL POODLE information leak

|     State: VULNERABLE

|     IDs:  CVE:CVE-2014-3566  BID:70574

|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other

|           products, uses nondeterministic CBC padding, which makes it easier

|           for man-in-the-middle attackers to obtain cleartext data via a

|           padding-oracle attack, aka the "POODLE" issue.

|     Disclosure date: 2014-10-14

|     Check results:

|       TLS_RSA_WITH_AES_128_CBC_SHA

|     References:

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566

|       https://www.imperialviolet.org/2014/10/14/poodle.html

|       https://www.securityfocus.com/bid/70574

|_      https://www.openssl.org/~bodo/ssl-poodle.pdf

| smtp-vuln-cve2010-4344: 

|_  The SMTP server is not Exim: NOT VULNERABLE

|_sslv2-drown: ERROR: Script execution failed (use -d to debug)

53/tcp   open     domain

80/tcp   open     http

|_http-csrf: Couldn't find any CSRF vulnerabilities.

|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.

| http-slowloris-check: 

|   VULNERABLE:

|   Slowloris DOS attack

|     State: LIKELY VULNERABLE

|     IDs:  CVE:CVE-2007-6750

|       Slowloris tries to keep many connections to the target web server open and hold

|       them open as long as possible.  It accomplishes this by opening connections to

|       the target web server and sending a partial request. By doing so, it starves

|       the http server's resources causing Denial Of Service.

|       

|     Disclosure date: 2009-09-17

|     References:

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750

|_      http://ha.ckers.org/slowloris/

|_http-dombased-xss: Couldn't find any DOM based XSS.

|_http-trace: TRACE is enabled

|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)

| http-enum: 

|   /tikiwiki/: Tikiwiki

|   /test/: Test page

|   /phpinfo.php: Possible information file

|   /phpMyAdmin/: phpMyAdmin

|   /doc/: Potentially interesting directory w/ listing on 'apache/2.2.8 (ubuntu) dav/2'

|   /icons/: Potentially interesting folder w/ directory listing

|_  /index/: Potentially interesting folder

111/tcp  open     rpcbind

139/tcp  open     netbios-ssn

445/tcp  open     microsoft-ds

512/tcp  open     exec

513/tcp  open     login

514/tcp  open     shell

1099/tcp open     rmiregistry

| rmi-vuln-classloader: 

|   VULNERABLE:

|   RMI registry default configuration remote code execution vulnerability

|     State: VULNERABLE

|       Default configuration of RMI registry allows loading classes from remote URLs which can lead to remote code execution.

|       

|     References:

|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/misc/java_rmi_server.rb

1524/tcp open     ingreslock

2049/tcp open     nfs

2121/tcp open     ccproxy-ftp

3306/tcp open     mysql

|_ssl-ccs-injection: No reply from server (TIMEOUT)

5432/tcp open     postgresql

| ssl-dh-params: 

|   VULNERABLE:

|   Diffie-Hellman Key Exchange Insufficient Group Strength

|     State: VULNERABLE

|       Transport Layer Security (TLS) services that use Diffie-Hellman groups

|       of insufficient strength, especially those using one of a few commonly

|       shared groups, may be susceptible to passive eavesdropping attacks.

|     Check results:

|       WEAK DH GROUP 1

|             Cipher Suite: TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA

|             Modulus Type: Safe prime

|             Modulus Source: Unknown/Custom-generated

|             Modulus Length: 1024

|             Generator Length: 8

|             Public Key Length: 1024

|     References:

|_      https://weakdh.org

| ssl-poodle: 

|   VULNERABLE:

|   SSL POODLE information leak

|     State: VULNERABLE

|     IDs:  CVE:CVE-2014-3566  BID:70574

|           The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other

|           products, uses nondeterministic CBC padding, which makes it easier

|           for man-in-the-middle attackers to obtain cleartext data via a

|           padding-oracle attack, aka the "POODLE" issue.

|     Disclosure date: 2014-10-14

|     Check results:

|       TLS_RSA_WITH_AES_128_CBC_SHA

|     References:

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3566

|       https://www.imperialviolet.org/2014/10/14/poodle.html

|       https://www.securityfocus.com/bid/70574

|_      https://www.openssl.org/~bodo/ssl-poodle.pdf

| ssl-ccs-injection: 

|   VULNERABLE:

|   SSL/TLS MITM vulnerability (CCS Injection)

|     State: VULNERABLE

|     Risk factor: High

|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h

|       does not properly restrict processing of ChangeCipherSpec messages,

|       which allows man-in-the-middle attackers to trigger use of a zero

|       length master key in certain OpenSSL-to-OpenSSL communications, and

|       consequently hijack sessions or obtain sensitive information, via

|       a crafted TLS handshake, aka the "CCS Injection" vulnerability.

|           

|     References:

|       http://www.openssl.org/news/secadv_20140605.txt

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224

|_      http://www.cvedetails.com/cve/2014-0224

5900/tcp open     vnc

6000/tcp open     X11

6667/tcp open     irc

|_irc-unrealircd-backdoor: Looks like trojaned version of unrealircd. See http://seclists.org/fulldisclosure/2010/Jun/277

8009/tcp open     ajp13

8180/tcp open     unknown

| http-cookie-flags: 

|   /admin/: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/index.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/login.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/account.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin_login.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/home.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin-login.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/adminLogin.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/controlpanel.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/cp.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/index.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/login.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/home.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/controlpanel.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin-login.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/cp.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/account.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/admin_login.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/adminLogin.jsp: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/includes/FCKeditor/editor/filemanager/upload/test.html: 

|     JSESSIONID: 

|       httponly flag not set

|   /admin/jscript/upload.html: 

|     JSESSIONID: 

|_      httponly flag not set

| http-slowloris-check: 

|   VULNERABLE:

|   Slowloris DOS attack

|     State: LIKELY VULNERABLE

|     IDs:  CVE:CVE-2007-6750

|       Slowloris tries to keep many connections to the target web server open and hold

|       them open as long as possible.  It accomplishes this by opening connections to

|       the target web server and sending a partial request. By doing so, it starves

|       the http server's resources causing Denial Of Service.

|       

|     Disclosure date: 2009-09-17

|     References:

|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750

|_      http://ha.ckers.org/slowloris/

| http-enum: 

|   /admin/: Possible admin folder

|   /admin/index.html: Possible admin folder

|   /admin/login.html: Possible admin folder

|   /admin/admin.html: Possible admin folder

|   /admin/account.html: Possible admin folder

|   /admin/admin_login.html: Possible admin folder

|   /admin/home.html: Possible admin folder

|   /admin/admin-login.html: Possible admin folder

|   /admin/adminLogin.html: Possible admin folder

|   /admin/controlpanel.html: Possible admin folder

|   /admin/cp.html: Possible admin folder

|   /admin/index.jsp: Possible admin folder

|   /admin/login.jsp: Possible admin folder

|   /admin/admin.jsp: Possible admin folder

|   /admin/home.jsp: Possible admin folder

|   /admin/controlpanel.jsp: Possible admin folder

|   /admin/admin-login.jsp: Possible admin folder

|   /admin/cp.jsp: Possible admin folder

|   /admin/account.jsp: Possible admin folder

|   /admin/admin_login.jsp: Possible admin folder

|   /admin/adminLogin.jsp: Possible admin folder

|   /manager/html/upload: Apache Tomcat (401 Unauthorized)

|   /manager/html: Apache Tomcat (401 Unauthorized)

|   /admin/view/javascript/fckeditor/editor/filemanager/connectors/test.html: OpenCart/FCKeditor File upload

|   /admin/includes/FCKeditor/editor/filemanager/upload/test.html: ASP Simple Blog / FCKeditor File Upload

|   /admin/jscript/upload.html: Lizard Cart/Remote File upload

|_  /webdav/: Potentially interesting folder

Host script results:

|_smb-vuln-ms10-054: false

|_smb-vuln-regsvc-dos: ERROR: Script execution failed (use -d to debug)

|_smb-vuln-ms10-061: false

Nmap done: 1 IP address (1 host up) scanned in 324.68 seconds
-->

POST EXPLOITATION cat etc/shadow:


<!--  -->

quick for hashcat omg i forgot !!!!

cat /etc/shadow -> hashest.txt 

hashcat -m 1800 hashest.txt /usr/share/wordlists/rockyou.txt --forceversion 

-> no such file or directory

WAT

hashcat -m 1800 hashest.txt /usr/share/wordlists/rockyou.txt --forceversion 0.57
 == invalid argument specified "forcevarsion"

(extracting rock you to desktop)

hashcat -m 1800 hashest.txt /home/kali/Desktop/rockyou.txt --forceversion 0.57

can has paste shadow? runtime isn't letting me (not sure if its meterpreter or hashcat or virtualbox)

SCREW IT WE'RE ROOT THIS IS WASTE OF TIME

we have backdoor is okie. but the network packet logic is as follows: 

Untrusted → [NETWORK VISIBLE] → Backdoor Host → [NETWORK + LOCAL FORENSIC] → Trusted Network. So therefore to provide proper remediation we have to remove the backdoor and then do a full forensic analysis of the backdoor host to determine if there are any other indicators of compromise. (note do that.)