from netmiko import ConnectHandler
from datetime import date, datetime



now = datetime.now()
print(now)
def get_data (ip = 'i'):
    with open('C:/Users/nimma/OneDrive/Desktop/Python/Devicedata.txt','r+') as f:
        file = f.readlines()
        print(file)
        for i in file:
            device = {
                'device_type' : 'invalid',
                'host' : i,
                'username' : 'admin',
                'password' : 'admin',
                'secret' : 'admin',
                'port' : 22 ,
                'buffer' : 10
                }

            try:
                get_data()
                connect = ConnectHandler(**device)
                print(connect)
                
            except:
                print("the error occured in {i}")

