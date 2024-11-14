from netmiko import ConnectHandler
from getpass import getpass

# device data
cisco_ios = {
    "device_type": "cisco_ios",
    "host":"192.168.10.1",
    "username":"admin",
    "password":getpass(),
    "secret":"admin",
    "port":22   # port no 22 int format only
}
cisco_ios1 = {
    "device_type": "cisco_ios",
    "host":"192.168.10.2",
    "username":"admin",
    "password":getpass(),
    "secret":"admin",
    "port":22   # port no 22 int format only
}
for device in (cisco_ios,cisco_ios1):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.enable()
    net_connect.disconnect()
