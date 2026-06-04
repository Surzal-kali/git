## SSH (Port 22)
Vulnerability: Default credentials
Creds: msfadmin:msfadmin  
Module:

auxiliary/scanner/ssh/ssh_login

## Samba (Ports 139/445)
1. trans2open RCE (CVE‑2003‑0201)
Module:

exploit/linux/samba/trans2open

2. usermap_script RCE (CVE‑2007‑2447)
Module:

exploit/multi/samba/usermap_script

## vsFTPd 2.3.4 Backdoor (Port 21)
Vulnerability: Backdoor triggered by :)  
Module:

exploit/unix/ftp/vsftpd_234_backdoor

## Apache / Web Apps (Port 80)
1. PHP CGI Argument Injection (CVE‑2012‑1823)
Module:

exploit/multi/http/php_cgi_arg_injection

2. Mutillidae (Multiple RCEs)
Common modules used:

exploit/multi/http/php_eval

exploit/unix/webapp/php_include

exploit/multi/http/lfi_exec

3. DVWA (Multiple vulns)
No dedicated MSF modules — manual exploitation:

SQLi

XSS

File upload → webshell

4. TWiki RCE (CVE‑2005‑1991)
Module:

exploit/unix/webapp/twiki_history

## Tomcat 5.5 (Port 8180)
Vulnerability: Manager app WAR upload
Default creds: tomcat:tomcat  
Module:

exploit/multi/http/tomcat_mgr_upload

## MySQL (Port 3306)
Vulnerabilities:

Weak creds (root: empty password)

UDF-based RCE

Modules:

auxiliary/scanner/mysql/mysql_login

exploit/linux/mysql/mysql_udf_payload

## PostgreSQL (Port 5432)
Vulnerability: Weak creds + command execution
Module:

auxiliary/scanner/postgres/postgres_login

exploit/multi/postgres/postgres_copy_from_program

## NFS (Port 2049)
Vulnerability: no_root_squash → root via SSH key
Module:

No direct exploit module
Technique:

Mount export

Drop authorized_keys

SSH as root

## VNC (Port 5900)
Vulnerability: Weak password
Module:

auxiliary/scanner/vnc/vnc_login

## Telnet (Port 23)
Vulnerability: Weak credentials
Module:

auxiliary/scanner/telnet/telnet_login

## UnrealIRCd (Port 6667)
Vulnerability: Backdoored version (CVE‑2010‑2075)
Module:

exploit/unix/irc/unreal_ircd_3281_backdoor

## Bind DNS (Port 53)
Vulnerability: DoS only (no RCE)
Module:

auxiliary/dos/dns/bind_tsig

## RPC / rlogin / rsh (Ports 512–514)
Vulnerability: Trust relationships → remote shell
Modules:

auxiliary/scanner/rservices/rsh_login

