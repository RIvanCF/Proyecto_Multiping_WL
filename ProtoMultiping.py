'''Prototipo personal, para implementar al proyecto original'''
import os #Importar sistema operativo y obtener una ruta de trabajo
import time
"""Importar archivo .txt a la terminal"""
with open("IP_addresses.txt") as file: #Apertura del archivo de textox
    dump = file.read() #Lectura del archivo
    dump = dump.splitlines() 
    print(dump)#Imprimir datos contenidos del archivo .txt a la terminal
    
"""Ping automatico de las direcciones IP"""
for ip in dump:
    '''os.system('cls')'''#Limpiar la pantalla por cada ping concluido 
    print('-'*40 + '\n')
    print('ping => IP: ', ip)#Impresion de la direccion ip a pingear
    res=os.popen(f'ping -n 2 {ip}').read() #Ping y lectura a las direcciones IP importadas del archivo .txt 


#Discriminacion de direcciones IP segun su respuesta al ping
    if(("Tiempo de espera agotado " or "Host de destino inaccesible")) in res: #Condición 1
        print(res)
        f=open("output.txt", "a") #importar la impresion al documento output.txt
        f.write(str(ip) + '  Desconectado' + '\n') #Imprimir el resultado si cumple con la 'Condicíon 1'
        f.close()
    else: #De no cumplirse la 'Condición 1'
        print(res)
        f=open("output.txt", "a")
        f.write(str(ip) + '  Conectado' + '\n')
        f.close()

#Imprimir resultados al documento 'output.txt' 
with open ("output.txt") as file:
    output = file.read()
    print(output)

    time.sleep(60)

with open("output.txt", "w") as file:
    pass
