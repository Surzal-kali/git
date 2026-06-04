# Exploit Chains Shared by Metasploitable Challenge VMs

## FTP -vsFTPd 2.3.4 (Backdoor, CVE-2011-2523)

(exploit/unix/ftp/vsftpd_234_backdoor)

## SSH - OpenSSH 4.7p1 (CVE-2010-4478)

SSH user enumeration via timing attack (auxiliary/scanner/ssh/ssh_enumusers_timing)

SSH brute force (auxiliary/scanner/ssh/ssh_login)

SSH key acceptance abuse
(auxiliary/scanner/ssh/ssh/identify_pubkeys)

## SMTP - Postfix /MSF2 SMTP Stack (VRFY/ETRN user enumeration)

VRFY user enumeration (auxiliary/scanner/smtp/smtp_unix)

SMPT v detection (auxiliary/scanner/smtp/smtp_version)

## DNS - Blind 9.4.2 (CVE-2008-0122)

TKEY DoS (auxiliary/dos/dns/bind_tkey)

TSIG Badtime DoS (auxiliary/dos/dns/bind_tsig_badtime)

TSIG Dos (auxiliary/dos/dns/bind_tsig)

## SMB - Samba 3.0.20 (trans2open, CVE-2007-2447)

Samba Trans2open RCE (exploit/linux/samba/trans2open)

Samba username map script RCE (exploit/multi/samba/usermap_script)

Samba pipe memory corruption (exploit/linux/samba/lsa_transnames_heap)

## NFS - No Root Squash (CVE-2009-2692)

NFS mount scanner (auxiliary/scanner/nfs/nfsmount)

NFS v scanner (auxiliary/scanner/nfs/nfsstat)

exploit is mount -> write -> escalate

## MySQL - 5.0.51a (CVE-2006-5759)

MySQL login brute force (auxiliary/scanner/mysql/mysql_login)

MySQL hash dump (auxiliary/scanner/mysql/mysql_hashdump)

MySQL UDF RCE (exploit/linux/mysql/mysql_udf_payload)

MySQL file write (exploit/linux/mysql/mysql_yassl_getname)

## Tomcat - 5.5 Manager Upload

Tomcat WAR upload RCE (exploit/multi/http/tomcat_mgr_upload)

Tomcat PUT method RCE (exploit/multi/http/tomcat_put)

Tomcat AJP Ghostcat (auxiliary/scanner/http/ajp_request)

Ghostcat is scanner only, not RCE

