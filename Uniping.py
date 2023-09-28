'''Código personal a implementar al proyecto personal'''
from pythonping import ping

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
        'PAQUETES PERDIDOS': ping_result.packet_loss*100 
    }

for ip in dump:
    print('|','-'*30,' INFORMACIÓN DE LA DIRECCIÓN IP ',ip,'-'*30,'|','\n')
    print('\n',ping_host(ip),'\n')
    print('|','-'*30," EL PROGRAMA FINALIZÓ SU EJECUCIÓN ",'-'*30,'|','\n')
