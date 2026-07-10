# Vulhub Structure Overview 📋

1. Directory Hierarchy

vulhub/
├── <software>/              # 150+ software directories (lowercase: "drupal", "nginx", etc.)
│   ├── CVE-XXXX-XXXXX/      # CVE vulnerabilities (UPPERCASE)
│   │   ├── docker-compose.yml
│   │   ├── README.md
│   │   ├── README.zh-cn.md  (Chinese docs)
│   │   ├── [N].png          (screenshots, numbered)
│   │   └── [src/]           (optional: exploit/config files)
│   └── <vuln-name>/         # Non-CVE vulns (lowercase: "heartbleed", "ssti")
│       └── [same structure]
│
├── base/                    # Base Docker images (153 dirs)
│   └── <software>/
│       └── <version>/
│           └── Dockerfile
│
└── environments.toml        # **Master registry** (82KB, TOML format)

2. environments.toml Registry

This is your index goldmine. Each entry:

[[environment]]
name = "Human-readable vuln name"
cve = ["CVE-2024-39907"]  # Array (can be multiple)
app = "Application name"
path = "software/CVE-ID"  # Relative path to compose dir
dockerfile = {"image:tag" = "path/to/base/Dockerfile"}
tags = ["RCE", "SQL Injection", "Database", ...]  # Searchable categories

3. Key Observations for VulnForge

┌────────────────────┬─────────────────────────────────────────────────────────────┐
│ Aspect             │ Details                                                     │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Total Environments │ ~1000+ (quick count: 150+ software × avg 5-10 vulns each)   │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Naming Convention  │ Software lowercase, CVEs uppercase, non-CVEs lowercase      │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Compose File       │ Minimal — just services with image, ports, optional volumes │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Standardization    │ ✅ Consistent structure — easy to parse programmatically    │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Base Images        │ Reusable from base/ (maps image → Dockerfile path)          │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Tags               │ Predefined vocabulary for filtering/randomization           │
├────────────────────┼─────────────────────────────────────────────────────────────┤
│ Line Endings       │ Must be LF (not CRLF)                                       │
└────────────────────┴─────────────────────────────────────────────────────────────┘

4. Pseudo-Random Selection Strategy

Since tags are categorized (RCE, SSRF, SQL Injection, etc.), you can:

• Random by difficulty: Group environments by tag count or Docker image size
• Random by type: Pick a random tag, then a random vulnerability
• Resource-aware: Pull image size from  docker-compose.yml  or pre-compute a manifest