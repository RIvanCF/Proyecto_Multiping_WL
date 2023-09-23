'''Código personal a implementar al proyecto personal'''
import os 
from pythonping import ping
import time

with open("IP_addresses.txt") as file: 
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

def ping_host(dump):
    ping_result = ping(target = dump, count = 100, timeout=1.5, verbose=True)

    return {
        'IP': dump,
        'LATENCIA MINIMA': ping_result.rtt_min_ms,
        'LATENCIA MÁXIMA': ping_result.rtt_max_ms,
        'PAQUETES PERDIDOS': ping_result.packet_loss,
    }

for ip in dump:
    f=open("output.txt", "a")
    f.write(str(ping_host(ip)))
    f.close()

with open ("output.txt") as file:
    output = file.read()
    print(output)

    time.sleep(10)

with open("output.txt", "w") as file: 
    pass 