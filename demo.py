from netmiko import ConnectHandler
device_list= {
    'device_type':'cisco_ios',
    'ip':'192.168.10.130',
    'username':'admin',
    'password':'admin',
    'secret':'cisco'
}
a=device_list.split(':')
print(a)
#connection= ConnectHandler(**device_list)
#connection.enable()
#command_list='command.txt'
#command_l=connection.send_config_from_file(command_list)
#print(command_l)
#connection.disconnect
