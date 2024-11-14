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
print("Trying to Connecet the Device.......")
connect = ConnectHandler(**devices)
print("Device Connection Succusfully \n Enter into the Enable mode")
connect.enable()
print("Create LoopBACK interface and Sending OSPF Configuration")
cmd_set_list = ["int lo10","ip add 10.10.10.10 255.255.255.255","commit"]
connect_cmd = connect.send_config_set(cmd_set_list)
print(f"show executed commands{connect_cmd}")
connect_cmd = connect.send_command("show run | sec ospf")
print(f"do show run | sec ospf {connect_cmd}")
connect_cmd = connect.send_command(" show ip int br | ex unass")
print(f"do show ip int brief | ex unass {connect_cmd}")
ospf_cmd = connect.send_command(" show ip route ospf")
print(f"do show ip route ospf{ospf_cmd}")
send_cmd = connect.send_command("sh run ")
# save file in test
# with open("runnning.txt","w") as f:
#     output = f.write(send_cmd)
# # print(send_cmd)
connect.disconnect()
print("Connection disconnected \n Try again ")
