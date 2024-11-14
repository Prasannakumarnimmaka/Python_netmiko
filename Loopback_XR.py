from netmiko import ConnectHandler
from getpass import getpass



devices = {
    "device_type" : "cisco_xr",
    "host" : "192.168.29.70",
    "username" : "admin",
    "password" : "admin",
    "secret" : "admin",
    "port" : 22 # optional use
}
# Define Loopback Configuration
# # loopback = ["int Loopback0",
#             "ipv4 address 1.1.1.1/32",
#             "description TEST PURPOSE",
#             "commit",
#             "end"]
isis_conf = ["router isis 10",
"is-type level-2-only",
"net 0000.0000.0000.0001.00",
"interface Loopback0",
"interface GigabitEthernet 0/0/0/0"
]
# Connect to Router
try:
    connection = ConnectHandler(**devices)
    print("Connected to Devices")

    # Enter global configuration mode
    connection.enable()
    connection.config_mode()

    # Configure Loopback 0
    print("Configuring isis on Router A...")
    output = connection.send_config_set(isis_conf,terminator=r"RP/0/RP0/CPU0:.*#")
    print(output)
    commit_diff = connection.send_command("show commit change diff")
    print(commit_diff)
    commit = connection.send_command("commit")
    print(commit)
    connection.exit_config_mode()
    
    # show interface ip details

    isis_Conf = connection.send_command("show run router isis")
    print(isis_Conf)


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
