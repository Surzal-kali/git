# The CTF Write Up Protocol:

**Usage Protocol:** Complete immediately after lab/write-ups (will run these in the evenings during down town since it's how i relax). Maps hands-on work to official exam objectives. Forces 10-min targeted bridge only when coverage is ❌ or 🔄. Protects math/sleep > perfect coverage.

###  📥 Lab Metadata

| Field | Entry |
|-------|-------|
| **Lab/CTF** | `[e.g., THM: LinuxPrivesc, HTB: MachineName]` |
| **Date** | `YYYY-MM-DD` |
| **Primary Cert Focus** | `[Linux+ / Sec+ / Net+ / AZ-800+]` |
| **Tools/Techniques Used** | `[e.g., nmap, smbclient, sudoers edit, kerberos relay]` |

---

### 🔍 Action → Objective Mapping

| CTF Action / Technique | Official Exam Domain & Obj. #* | Coverage | 10-Min Bridge Task (Only if ❌/🔄) |
|------------------------|--------------------------------|----------|-----------------------------------|
| 'Enumerated HTTP and found a vulnerable file upload endpoint' | `Sec+: SY0-701: 3.4` | ✅ Covered | N/A |
| 'Deployed a private network and custom API endpoints for homelab infastrucutre (does that map to anything?)' | `AZ-800: M001` | 🔄 Reinforce | Research and document 3 real-world use cases of private networks in hybrid cloud environments.  :D|
| 'Used a custom-crafted polyglot file to bypass upload restrictions and achieve RCE' | `Sec+: SY0-701: 3.4` | ❌ Not Yet Touched | Research and summarize 3 modern file upload evasion techniques that leverage parser quirks or behavioral activation. |
| 'Cracked a password hash using John the Ripper' | `Sec+: SY0-701: 5.1` | ✅ Covered | N/A |
| 'Crafted custom SQLi payloads to extract data from a database' | `Sec+: SY0-701: 3.5` & `Net+: N10-009: 4.3` | ✅ Covered | N/A |
| 'Used Metasploit to exploit a known vulnerability in a service' | `Sec+: SY0-701: 3.4` | 🔄 Reinforce | Research and document 3 common Metasploit modules used for post-exploitation activities. |
| 'Mapped Exploits to CVEs and CVSS scores' | `Sec+: SY0-701: 3.4` | ✅ Covered | N/A |

(so alot of hands on, but not alot of actual schoolwork haha. I will be using this protocol to map my CTF work to the official exam objectives, and only doing the 10-minute bridge research when I haven't covered an objective yet. This way I can focus on the hands-on work while still ensuring I'm making progress towards the certifications.)

> *📌 Objective Format: `Exam Version Domain #.##`. Cross-reference your official blueprint when filling. Linux+ uses SK0-005/006 objectives; Sec+/Net+ use SY0-701/N10-009; AZ-800 uses Microsoft skill-mapped IDs.* (NOTE: they no longer do objectives numerically, more like categories. I will be using the module names for the College Courses at Central New Mexico CC, but you can use whatever schema as long as you stick to it)

---

### 📊 Weekly Triage Snapshot

| Cert | ✅ Covered | 🔄 Reinforce | ❌ Not Yet Touched | Bridge Priority (Next 7 Days) |
|------|-----------|--------------|-------------------|------------------------------|
| Linux+ | `X/XX` | `X/XX` | `X/XX` | `[High/Med/Low]` | Low
| Sec+ | `X/XX` | `X/XX` | `X/1XX` | `[High/Med/Low]` | Low
| Net+ | `X/XX` | `X/XX` | `X/1XX` | `[High/Med/Low]` | Medium
| AZ-800 | `X/XX` | `X/XX` | `X/1XX` | `[High/Med/Low]` | High


## Linux Modules:

| Module | Status |
|--------|--------|
| L001: System Management I | ✅ Covered |
| L002: System Management II | ✅ Covered |
| L003: Services and User Management I | In Progress |  
| L004: Services and User Management II | Not Yet Touched |
| L005: Security I | Not Yet Touched |
| L006: Security II | Not Yet Touched |
| L007: Automation, Orchestration, and Scripting  | Not Yet Touched |
| L008: Troubleshooting I | Not Yet Touched |
| L009: Troubleshooting II | Not Yet Touched |

## Network+ Modules:

| Module | Status |
|--------|--------|
| N001: Networking Concepts | In Progress (just got the textbook) |
| N002: Network Implmentation | Not Yet Touched |
| N003: Network Operations | Not Yet Touched |
| N004: Network Security | Not Yet Touched |
| N005: Network Troubleshooting and Tools | Not Yet Touched |


## Windows Server/AZ-800 Modules:

| Module | Status |
|--------|--------|
| M001: Windows Server Hybrid Infastructure | Not Yet Touched |
| M002: Discover Active Drirectory | Not Yet Touched |
| M003: Managing Active Directory | Not Yet Touched |
| M004: Configuring Group Policies | Not Yet Touched |
| M005: Configure Domains | Not Yet Touched |
| M006:  Windows Server Hybrid II? | Not Yet Touched |
| M007: Configure DNS | Not Yet Touched |
| M008: Manage IP Addressing | Not Yet Touched |
| M009: Implement Network Connectivity | Not Yet Touched |
| M010: Configure Advanced Storage Solutions | Not Yet Touched |
| M011: Implement Virtualization with Hyper-V and Azure | Not Yet Touched |

(cybersecurity is put on the back burner, since this is 3 certifications + Mathmatics. Christ)
(we'll supplement with active CTF work and hands-on experience)
