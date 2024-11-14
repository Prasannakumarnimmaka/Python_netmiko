from ping3 import ping, verbose_ping

# Simple ping to a host
ip = "192.168.10.132"
response_time = ping(ip)
if response_time:
    print(f"Ping successful! Response time: {response_time:.4f} seconds")
else:
    print("Ping failed!")