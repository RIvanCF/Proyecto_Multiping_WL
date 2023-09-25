'''Prototipo personal, para implementar al proyecto original'''
import os #Importar sistema operativo y obtener una ruta de trabajo
import time
from pythonping import ping #Biblioteca que permitira calcular la letencia de cada direccion IP
"""Importar archivo .txt a la terminal"""


with open("IP_addresses.txt") as file: #Apertura del archivo de textox
    dump = file.read() #Lectura del archivo
    dump = dump.splitlines() 
    print(dump)#Imprimir datos contenidos del archivo .txt a la terminal

def ping_host(dump):
    ping_result = ping(target = dump, count = 2, timeout = 1.2) #Parametros 

    return ping_result.rtt_max_ms
 
"""Ping automatico de las direcciones IP"""
for ip in dump:
    '''os.system('cls')'''#Limpiar la pantalla por cada ping concluido 
    if(ip <= "0"):
        print("|------      El programa finalizó su ejecución      ------|" + "\n"*2)
        break
    else:
        print('-'*40 + '\n')
        print('ping => IP: ', ip)#Impresion de la direccion ip a pingear
        res=os.popen(f'ping -n 1 -w 1200 {ip}').read() #Ping y lectura a las direcciones IP importadas del archivo .txt
    
#Discriminacion de direcciones IP segun su respuesta al ping
        if("Tiempo de espera agotado " or "inaccesible." or ping_host(ip) >= 1200.0) in res: #Condición 1
            print(res)
            f=open("output.txt", "a") #importar la impresion al documento output.txt
            f.write(str(ip) + ' [ERROR]' + ' DOWN' + '\n' ) #Imprimir el resultado si cumple con la 'Condicíon 1'
            f.close()

        else: #De no cumplirse la 'Condición 1'
                print(res)
                f=open("output.txt", "a")
                f.write(str(ip)  + ' [OK] ' + str(ping_host(ip)) + '\n') #Se imprime la IP, estado de conexión, velocidad de respuesta Máxima 
                f.close()
    
#Imprimir resultados al documento 'output.txt' 
with open ("output.txt") as file:
        output = file.read()
        print(output)

        time.sleep(5) #Tiempo de visualización antes de borrarse el contenido 

with open("output.txt", "w") as file: 
        pass
    