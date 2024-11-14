from netmiko import ConnectHandler
from datetime import datetime, date
from ping3 import ping,verbose_ping

now= datetime.now()
def Get_device_Credintials():
    global device
    device = {
        "device_type" : "cisco_ios",
        "host" : ip,
        "username" : "admin",
        "password" : "admin",
        "secret" : "admin",
        "port" : 22
    }

    
    

#_main_#
with open("C:/Users/nimma/OneDrive/Desktop/Python/Devicedata.txt","r") as f:
    for ip in f:
        ip = ip.removesuffix("\n")
        print(ip)
        ip = str(ip)
        ip_ping = ping(ip)
        if ip_ping:
            print(f"Connecting the devive{ip}{ip_ping:.4f} seconds")
            filename = "Conf_Backup_" + ip +"_"+ str(now) +".txt"
            print(filename)
            Get_device_Credintials()
            connect = ConnectHandler(**device)
            connect.enable() # Enter the Enable mode
            connect.config_mode() # Enable the config mode
            command_set = ("int e0/1","no shut","exit")
            send_command_set = connect.send_config_set(command_set)
            for i in range(2,4):
                hsrp_Config = ["int e0/1.10","encapsulation dot1q 10",f"ip add 192.168.20.{i} 255.255.255.0","standby 1 ip 192.168.20.254",]
            send_hsrp_Config = connect.send_config_set(hsrp_Config)
            print(send_hsrp_Config)
            send_cmd = connect.send_command("do wr me\n")
            send_cmd = connect.send_command("show ip int br | ex unass")
            send_cmd1 = connect.send_command("show standby brief")
            print(f"send ip int br | ex unass:{send_cmd}")
            print(f"show ip standby:{send_cmd1}")
        else:
            print(f"Device unreachable: {ip}")
    
print("Job Successfull")

        

        



