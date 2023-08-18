'''Prototito personal, con posibilidad de implementar al proyecto original'''
import os #Importar sistema operativo y obtener una ruta de trabajo

"""Importar archivo .txt a la terminal"""
with open("ip_lista.txt") as file: #Apertura del archivo de texto
    dump = file.read() #Lectura del archivo
    dump = dump.splitlines() 
    print(dump)#Imprimir datos contenidos del archivo .txt a la terminal
    
"""Ping automatico de las direcciones IP"""
for ip in dump:
    os.system('cls')#Limpiar la pantalla por cada ping concluido 
    print('-'*40)
    print('ping => IP: ', ip)#Impresion de la direccion ip a pingear
    res=os.popen(f'ping -n 2 {ip}').read() #Ping y lectura a las direcciones IP importadas del archivo .txt 
    print('-'*40)

#Discriminacion de direcciones IP segun su respuesta al ping
    if(("Tiempo de espera agotado " or "Host de destino inaccesible")) in res: #Condición 1
        print(res) 
        f=open("output.txt", "a") #importar la impresion al documento output.txt
        f.write(str(ip) + ' -> Desconectado' + '\n' + '-'*40 + '\n') #Imprimir el resultado si cumple con la 'Condicíon 1'
        f.close()
    else: #De no cumplirse la 'Condición 1'
        print(res)
        f=open("output.txt", "a")
        f.write(str(ip) + ' -> Conectado' + '\n' + '-'*40 + '\n')
        f.close()

with open ("output.txt") as file:
    output = file.read()
    print(output)

