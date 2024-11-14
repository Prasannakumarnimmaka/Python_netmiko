from netmiko import ConnectHandler
from getpass import getpass

# device data
device = {
    "device_type": "cisco_ios",
    "host":"192.168.10.130",
    "username":"admin",
    "password":getpass(),
    "secret":"admin",
    "port":22   # port no 22 int format only
}
command = "showe ip int brief"
with ConnectHandler(**device) as net_connent:
    output = net_connent.send_command(command)
print(output)