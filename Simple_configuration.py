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
net_connect = ConnectHandler(**device)
net_connect.enable() # enter into enable mode---privileges mode
print(net_connect.find_prompt())
output = net_connect.send_command('show ip int brief')
print(output)
net_connect.disconnect()