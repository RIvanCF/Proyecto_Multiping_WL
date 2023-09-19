
from pythonping import ping 

with open("IP_addresses.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

def ping_host(dump):
    ping_result = ping(target = dump, count = 2, timeout = 1.2)

    return ping_result.rtt_max_ms 


for ip in dump: 
    if(ping_host(ip) >= 1200.0):
        print( "INACCESIBLE")
    else:
        print(ping_host(ip),'m/s')