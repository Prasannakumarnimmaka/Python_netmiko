from netmiko import ConnectHandler

Device = {
    "device_type": "cisco_ios",
    "host":"192.168.10.130",
    "username":"admin",
    "password":"admin",
    "secret":"admin",
    "port":22
}
Net_connect = ConnectHandler(**Device)
print("Connect the device.....")