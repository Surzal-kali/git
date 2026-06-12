# Map /app1 to a local service on port 8080
tailscale serve --bg --set-path /openterminal http://127.0.0.1:8000

# Map /app2 to a local service on port 8081
tailscale serve --bg --set-path /openweb http://127.0.0.1:8080

don't over think it poookie.