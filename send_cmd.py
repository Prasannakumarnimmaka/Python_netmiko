from netmiko import ConnectHandler
from ping3 import ping, verbose_ping
File_Name = "Devicedata.txt"

def device_Loging_data():
    global File_Name, device, file_name
    device = {
        "device_type" : "cisco_ios",
        "host" : ip,'899999998;[,]'
        "username" : "admin",
        "password" : "admin",
        "secret" :"admin",
        "port" : 22  #Optional data
    }
    file_name = "Config_backup " + ip +  ".txt"
    # print(file_name)
#_main_#

with open ("C:/Users/nimma/OneDrive/Desktop/Python/Devicedata.txt","r") as f:
    for ip in f:
        ip = (ip.removesuffix("\n"))
        ping = ping(ip)
        if ping == True :
            print(f"Device reachable...")
            # device_Loging_data()
        elif ping == False:
            print("Device is not reachable")
            continue
        device_Loging_data()
        # Connecting Device
        print(f" Trying to Connect the Devices {ip}")
        connect = ConnectHandler(**device)
        connect.enable() # Enable mode
        connect.config_mode() # Configuration mode
        for n in range(1,2):
            command = [f"int lo{n}",f"ip add 1.1.1.{n} 255.255.255.255", "no sh"]
            send_cmd = connect.send_config_set(command)
            print(send_cmd)
        command = connect.send_command("do wr \n")
        command = connect.send_command ("Show ip int br | ex unass")
        print(command)
        