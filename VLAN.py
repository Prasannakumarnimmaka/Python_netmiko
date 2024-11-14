from netmiko import ConnectHandler
from datetime import datetime, date
from ping3 import ping,verbose_ping

now= datetime.now()
def Get_device_Credintials():
    global device, filename
    device = {
        "device_type" : "cisco_ios",
        "host" : ip,
        "username" : "admin",
        "password" : "admin",
        "secret" : "admin",
        "port" : 22
    }

    filename = "Conf_Backup"+ ip +".txt"
    

#_main_#
with open("C:/Users/nimma/OneDrive/Desktop/Python/Devicedata.txt","r") as f:
    for ip in f:
        ip = ip.removesuffix("\n")
        print(ip)
        ip = str(ip)
        ip_ping = ping(ip)
        if ip_ping:
            print(f"Connecting the devive{ip}{ip_ping:.4f} seconds")
            Get_device_Credintials()
            connect = ConnectHandler(**device)
            connect.enable() # Enter the Enable mode
            connect.config_mode() # Enable the config mode
            vlan_cmd = ["vlan 10"," name Prasanna"]
            vlan_config = connect.send_config_set(vlan_cmd)
            Trunk_conf_cmd = ["int range e0/0-1","switchport trunk encapsulation dot1q","switchport mode trunk","no sh"]
            Trunk_conf = connect.send_config_set(Trunk_conf_cmd)
            Access_Config = ["int range e0/2-3","switchport mode access","switchport access vlan 10"]
            Aceess_config_cmd = connect.send_config_set(Access_Config)
            send_cmd = connect.send_command("do wr me")
            show_vlan = connect.send_command("show vlan brief")
            print(f"show vlan brief :{show_vlan}")
            show_trunk = connect.send_command("show interface trunk")
            print(f"show trunk:{show_trunk}")
            show_run = connect.send_command("show run")
            print(f"show run: {show_run}")
            with open (filename,"w") as file:
                output = file.write(show_run)
                print(f"show run :{output}")

    print(" Job Successfull")
connect.disconnect()


