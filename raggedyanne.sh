[Unit]
Description=RAG Router Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple

# Use full paths for both python and script
ExecStart=/usr/bin/python3 /home/surzal/git/rag_router.py

# Ensure the working directory is correct for imports, relative paths, etc.
WorkingDirectory=/home/surzal/git

# Run as your user
User=surzal
Group=surzal

# Make Python logs appear immediately in journalctl
Environment=PYTHONUNBUFFERED=1

# Restart policy
Restart=on-failure
RestartSec=3

# Optional but recommended: define a clean PATH
Environment=PATH=/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=multi-user.target