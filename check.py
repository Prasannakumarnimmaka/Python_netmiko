from netmiko import ConnectHandler

File_Name = "Devicedata.txt"

def device_Loging_data():
    global File_Name, device, file_name
    device = {
        "device_type" : "cisco_ios",
        "host" : ip,
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
        ip = ip.removesuffix("\n")
        if ip == True :
            print(f"Device reachable...")
            # device_Loging_data()
        elif ip == False:
            print("Device is not reachable")
            continue
        device_Loging_data()
        # Connecting Device
        print(f" Trying to Connect the Devices {ip}")
        connect = ConnectHandler(**device)
        connect.enable() # Enable mode
        connect.config_mode() # Configuration mode
        command_list = ["do show run","do show ip int br | ex unas"]
        # send command to device 
        command = connect.send_config_set(command_list)
        # command = connect.send_command("sh ip int br | ex unass \n")
        # sh_run = connect.send_command("sh run")
        print(command)
        # Print the file 
        with open (file_name,"w") as file:
            output = file.write(command)
            # sh_run = file.write(sh_run)
            print(f"Show ip int br | ex unass\n {output}\n")