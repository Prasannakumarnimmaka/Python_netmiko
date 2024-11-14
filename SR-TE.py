from netmiko import ConnectHandler

# Define the device details for Router A
router_a = {
    "device_type": "cisco_xr",
    "ip": "192.168.29.70",              # Router A IP
    "username": "admin",
    "password": "admin",
}

# Define the SR-TE configuration commands for Router A
sr_te_commands = [
    "mpls traffic-eng",
    "policy my-srte-policy",
    "color 10",                          # Optional: Define traffic class/color
    "end-point ipv4 3.3.3.3",            # Destination IP (Router C’s Loopback)
    "candidate-paths",
    "preference 100",
    "explicit-path name path-via-b",   # Name of the explicit path
    "index 10 next-hop 2.2.2.2",       # Intermediate Router B’s Loopback IP
    "index 20 next-hop 3.3.3.3",       # Final Router C’s Loopback IP
    "mpls traffic-eng",
    "explicit-path name path-via-b",
    "index 10 next-hop 2.2.2.2",         # Intermediate hop
    "index 20 next-hop 3.3.3.3",         # Final destination
]

# Define the MPLS TE interface configuration commands for Router A
interface_commands = [
    "interface GigabitEthernet0/0/0/0",  # Use the correct interface name
    "mpls traffic-eng tunnels",         # Enable MPLS TE on the interface
]

# Connect to Router A
try:
    connection = ConnectHandler(**router_a)
    print("Connected to Router A")

    # Enter global configuration mode
    connection.enable()
    connection.config_mode()

    # Configure SR-TE policy
    print("Configuring SR-TE policy on Router A...")
    output = connection.send_config_set(sr_te_commands)
    print(output)

    # Enable MPLS TE on the specified interface
    print("Enabling MPLS TE on the interface...")
    output = connection.send_config_set(interface_commands)
    print(output)

    # Save the configuration
    print("Saving configuration...")
    output = connection.save_config()
    print(output)

    print("Configuration complete.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the device
    connection.disconnect()
    print("Disconnected from Router A")