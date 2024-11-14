# All pre-installed besides Netmiko.
from csv import reader
from datetime import date, datetime
from netmiko import ConnectHandler
from ping3 import ping, verbose_ping
import getpass
import os
#import sys

#sys.tracebacklimit = 0

# Checks if the folder exists, if not, it creates it.
if not os.path.exists('backup-config'):
    os.makedirs('backup-config')
# Current time and formats it to the Asia India time of Month, Day, and Year.
now = datetime.now()
dt_string = now.strftime("%m-%d-%Y_%H-%M")

# Gives us the information we need to connect.
def get_saved_config(ip, username, password):
    cisco_ios = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
        }

    # Creates the connection to the device.

    try:
        net_connect = ConnectHandler(**cisco_ios)
        net_connect.enable()
    except:
        return -1
    # Gets the running configuration.
    showintdes = net_connect.send_command("show int des")
    showinttrunk = net_connect.send_command("show int trunk")
    showvlan = net_connect.send_command("show vlan")
    showrun = net_connect.send_command("show run")
    shinv = net_connect.send_command("show inv")
    shplfm = net_connect.send_command("show platform")
    # Gets and splits the ip address for the  output file name.
    ip = ip.strip()
    # Creates the file name, which is the ip , and the date and time.
    fileName = ip + "_" + dt_string
    #fileName = ip
    # Creates the text file in the backup-config folder with the special name, and writes to it.
    backupFile = open("backup-config/" + fileName + ".txt", "w+")
    backupFile = open("backup-config/" + fileName + ".txt", "w+")
    backupFile.write(showintdes)
    backupFile.write("\n")
    backupFile.write(showinttrunk)
    backupFile.write("\n")
    backupFile.write(showvlan)
    backupFile.write("\n")
    backupFile.write(showrun)
    backupFile.write("\n")
    backupFile.write(shinv)
    backupFile.write("\n")
    backupFile.write(shplfm)
    backupFile.write("\n")

   # backupFile.write(showvlan)
    print("Outputted to " + fileName + ".txt!")

# Gets the CSV file name, and grabs the information from it.
with open('cisco_backup_hosts.csv') as csvfile:
        csv_reader = reader(csvfile)
        list_of_rows = list(csv_reader)
        rows = len(list_of_rows)
        while rows > 1:
            rows = rows -1
            ip = list_of_rows[rows][0]
            ip_ping = ping(ip)

            if ip_ping == None:
                fileName = "downDevices_" + dt_string + ".txt"
                downDeviceOutput = open("backup-config/" + fileName, "a")
                downDeviceOutput.write(str(ip) + "\n")
                print(str(ip) + " is down!")
            else:
                status = get_saved_config(list_of_rows[rows][0], list_of_rows[rows][1], list_of_rows[rows][2])
                if status == -1:
                    status = get_saved_config(list_of_rows[rows][0], list_of_rows[rows][3], list_of_rows[rows][4])
                    if status == -1:
                        fileName = "BothCredentials" + dt_string + ".txt"
                        BothCredentialsOutput = open("backup-config/" + fileName, "a")
                        BothCredentialsOutput.write(str(ip) + "\n")
                        print(str(ip) + " Both credentials are wrong!")
