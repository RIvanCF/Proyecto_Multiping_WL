'''Prototito personal, con posibilidad de implementar al proyecto original'''
import os #Importar sistema operativo y obtener una ruta de trabajo

with open("ip_lista.txt") as file: #Apertura del archivo de texto
    dump = file.read() #Lectura 
    dump = dump.splitlines() 
    print(dump)
    
    for ip in dump:
        os.system('cls')
        print('ping => IP: ', ip)
        print('-'*60)
        os.system('ping -n 2 {}'.format(ip)) #Ping a las direcciones IP importadas del archivo .txt
        print('-'*60)
    