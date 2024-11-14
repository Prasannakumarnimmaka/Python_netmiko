from netmiko import ConnectHandler
# device credential data provide 
device = {
    "device_type": "cisco_ios",
    "host":"192.168.1.130",
    "username":"vayu",
    "password":"vayu",
    "secret":"vayu",
    "port":22   # port no 22 int format only
}
print("Device connection started......")
conn_device = ConnectHandler(**device)
print("Enter into the enbale mode")
conn_device.enable()
comm_set = ("int e0/1","no sh","ip add 100.0.0.1 255.255.255.0","duplex full")
send_cmd = conn_device.send_config_set(comm_set)
print(send_cmd)
send_cmd = conn_device.send_command("sh ip int br | ex unas")
# save output as in text file
with open("runnning.txt","w") as f:
    output = f.write(send_cmd)
print(output)
print("Disconneted the device")
conn_device.disconnect()

