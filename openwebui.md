docker run -d \
  --name open-webui \
  --network host \
  --ipc host \
  --pid host \
  -p 8080:8080 \
  -v ~/open-webui/data:/app/backend/data \
  -v ~/open-webui/cache:/app/backend/data/cache \
  -v ~/open-webui/models:/app/backend/data/models \
  -v ~/open-webui/tmp:/tmp \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENV=prod \
  ghcr.io/open-webui/open-webui:latest

# Access the web interface at http://localhost:8080 (or the tailscale ip for meeee)

docker run -it \
  --cap-add=SYS_ADMIN \
  --cap-add=SYS_PTRACE \
  --cap-add=NET_ADMIN \
  --security-opt apparmor=unconfined \
  --security-opt seccomp=unconfined \
  --net host \
  -v /home/user/.local/share/open-terminal:/home/user/.local/share/open-terminal \
  -v /home/user/.config/open-terminal:/home/user/.config/open-terminal \
  -v /tmp:/tmp \
  ghcr.io/open-webui/open-terminal:latest

  # Access the terminal interface at http://localhost:8080/terminal (or the tailscale ip for meeee)

  also 

  mkdir -p ~/.local/share/open-terminal ~/.config/open-terminal

before running the terminal container to ensure the necessary directories exist for data persistence.