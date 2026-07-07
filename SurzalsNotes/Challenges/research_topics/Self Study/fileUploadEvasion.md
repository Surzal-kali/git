# File Upload Evasion Techniques

📁 File Upload Evasion: Quick Research Placeholder
Core Objective: Bypass validation controls to deploy executable/triggerable artifacts that achieve RCE, data exfiltration, or persistent access.

🔹 Validation Layers & Common Bypass Vectors
LAYER
TYPICAL CONTROL
BYPASS TECHNIQUE
Filename/Extension
Blocklist/Allowlist
Double extensions (shell.php.jpg, file.asp.aspx), case variation, trailing whitespace/dots (test.php. , .php.), Unicode/IDN homograph characters
Content-Type/MIME
Header validation
Spoof Content-Type: image/png for PHP webshells; rely on server misconfig rather than header trust
Magic Bytes/Fingerprints
File signature scan
Embed valid image headers (\xFF\xD8\xFF / \x89PNG) over malicious code; use polyglot structures
Size/Structure
Max file size, ZIP archive checks
Chunked uploads, race conditions during temp→live move, archive password bypasses, malformed but parser-tolerant archives


🔄 Modern/Advanced Techniques (2024–2026)
Triggerless / Conditional Activation: Files remain inert until specific requests trigger execution (e.g., custom HTTP header, cookie, or query param). Evades static analysis, DAST, and AI-based scanners.
Parser & Runtime Exploitation: Leverage server stack quirks (IIS . truncation, Apache # comment injection, Nginx PHP-FPM boundary handling, CMS template engines) to reinterpret benign uploads as code.
Obfuscated Payloads: Polyglot images (GIF/PNG + JS/PHP), base64/zlib compressed webshells in EXIF/metadata, steganographic triggers, or DOM/CSP bypass chaining.
WAF/EDR Evasion via Encoding: UTF-7/UTF-8 mixed encoding, fragmented tags (<? $code ?> across boundaries), hex/octal escapes, or conditional compilation to break regex-based filters.
📝 Research Placeholders & Angles
✅ Legacy tricks (null bytes %00, basic MIME spoofing) are largely mitigated in modern runtimes; focus on parser normalization bugs and runtime interpretation gaps.
🔍 Modern evasion relies on behavioral activation timing and multi-stage parsing, not just static signature bypass.
🧪 Test against: CMS-specific upload handlers (WordPress, Drupal, Shopify), cloud storage CDNs, API-based multipart endpoints, and enterprise WAF/Cloud WAF rule sets.
🛡️ Defenses to research: Strict allowlists + content negotiation validation, MIME/type double-checking, dedicated file analysis engines, server-side sandbox execution, and runtime behavior monitoring.
Suggested Manual Research Keywords: conditional webshell, polyglot file upload, WAF multipart evasion, CMS parser file interpretation bugs, triggerless RCE payload, cloud CDN upload validation bypass

# File Upload Evasion: qdPM Case Study (the tale against the spreadsheet)

For this box we prepared multiple payloads of various resolution sizes, all php (based on the application framework). However, it seems this application is designed with an honest to god spreadsheet, nothing fancy.

TODO: Try out the new payloads on an actual vulnerable machine. See if it in fact works!

