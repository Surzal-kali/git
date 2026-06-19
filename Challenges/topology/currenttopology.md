# current network topology

Tailscale mesh network advertises routes to virtual machines (VMs) hooked into Host-only adapters to the individual nodes for maximum security. 

This has two rules to it

Any subnets advertised by all nodes cannot overlap. Because they'll be accessible on every node, they must be unique.

Payloads and packets sent to the advertised subnets are encrypted and sent directly to the node that advertises them. This means that the traffic is secure and does not pass through any intermediate nodes. But it makes it very finnicky when sending malicious payloads to the VMs, as the traffic is encrypted and sent directly to the node that advertises the subnet, so the same payload may work on one node but not on another, depending on the configuration of the network and the nodes.

Additional queries from surzal:

- How can i attach Offsec CTF vpns to the Tailscale Network? Sites like HacktheBox and TryHackMe provide VPNs to connect to their labs, but these VPNs are not designed to be integrated with Tailscale. However, you can use a workaround by setting up a VPN client on a machine that is part of your Tailscale network and then connecting to the CTF VPN from that machine. This way, the traffic from your Tailscale network will be routed through the VPN client, allowing you to access the CTF labs. (so no connecting it here with tailscale, but you can connect to the CTF VPN from a machine that is part of your Tailscale network.....) WAIT theres a work around for Forticlient VPN..maybe it works hear me out dex

I turned off magic DNS and made the IPs resolve numerically, so the FortiClient VPN and the Tailscale netowrk existed without conflicts. Technically woudn't the same logic work with openvpn and the like?

# Conclusion

The Tailscale mesh network topology provides a secure and efficient way to connect VMs using Host-only adapters. However, it requires careful consideration of subnet configurations and may present challenges when sending malicious payloads due to encryption and direct routing. While integrating Offsec CTF VPNs directly with Tailscale may not be possible, using a workaround by connecting to the CTF VPN from a machine within the Tailscale network can allow access to the labs without conflicts.

