# Mercury Ideapad

## Challenge

Get the root flag from the Mercury virtual machine. 

## Solution

1. CVE-2021-3156 :D
Sudo before 1.9.5p2 contains an off-by-one error that can result in a heap-based buffer overflow, which allows privilege escalation to root via "sudoedit -s" and a command-line argument that ends with a single backslash character.

sudoedit -s
whoami\

root? 

### Dexter's Rebutal

While CVE-2021-3156 is a classic privilege escalation vector, several concerns arise:

**Technical Concerns:**
- The exploit requires `sudoedit` specifically, not just any sudo command. Does the target system have `sudoedit` configured in `/etc/sudoers`?
- Modern systems may have mitigations like SELinux or AppArmor that could prevent exploitation even if the vulnerability exists.
- The off-by-one overflow is subtle; does the exact payload work across different glibc versions?

**Questions:**
- Was this a coincidence that the VM was running an vulnerable sudo version, or was it intentionally left as a learning opportunity?
- How would you detect this in a production environment without scanning for CVEs?
- What's the minimal configuration needed to trigger this (e.g., does the user need specific sudoers entries)?

**Reasoning:**
The elegance of Baron Samedit lies in its simplicity, but relying on such well-known exploits feels like walking into a honeypot. In real engagements, I'd verify:
1. The exact sudo version (`sudo -V`)
2. Whether `sudoedit` is accessible to the user
3. Alternative paths (misconfigured SUID binaries, writable /etc/sudoers, etc.)

### Surza'sl Rebutal

This challenge teaches an important lesson: **patch management matters**. CVE-2021-3156 was disclosed in January 2021—leaving sudo unpatched for months is negligence.

Absolutely! This was a box from vulnhub, made in (most likely) pre 2021 rules. The actual point of the box was to show how to use tail sym links to read/write files as root, but the sudo exploit was a fun bonus. I thought i'd share it here since it was a fun challenge and a good reminder to patch your systems! Also, it was a good opportunity to practice using sudoedit, which is often overlooked in favor of more flashy exploits.