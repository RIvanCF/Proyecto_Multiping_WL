'''Prototipo personal, para implementar al proyecto original'''
import os #Importar sistema operativo y obtener una ruta de trabajo

"""Importar archivo .txt a la terminal"""
with open("ip_lista.txt") as file: #Apertura del archivo de texto
    dump = file.read() #Lectura del archivo
    dump = dump.splitlines() 
    print(dump)#Imprimir datos contenidos del archivo .txt a la terminal
    
"""Ping automatico de las direcciones IP"""
for ip in dump:
    os.system('cls')#Limpiar la pantalla por cada ping concluido 
    print('-'*30)
    print('ping => IP: ', ip)#Impresion de la direccion ip a pingear
    print('-'*30)
    res=os.popen(f'ping -n 2 {ip}').read() #Ping y lectura a las direcciones IP importadas del archivo .txt 
    

#Discriminacion de direcciones IP segun su respuesta al ping
    if(("Tiempo de espera agotado " or "Host de destino inaccesible")) in res: #Condición 1
        print(res) 
        f=open("output.txt", "a") #importar la impresion al documento output.txt
        f.write(str(ip) + '  Desconectado' + '\n' + '-'*30 + '\n') #Imprimir el resultado si cumple con la 'Condicíon 1'
        f.close()
    else: #De no cumplirse la 'Condición 1'
        print(res)
        f=open("output.txt", "a")
        f.write(str(ip) + '  Conectado' + '\n' + '-'*30 + '\n')
        f.close()

#Imprimir resultados al documento 'output.txt' 
with open ("output.txt") as file:
    output = file.read()
    print(output)

