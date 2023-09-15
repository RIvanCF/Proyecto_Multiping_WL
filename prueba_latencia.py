#!/usr/bin/python

import subprocess
from time import sleep
from math import sqrt

tLatencias = list()
tJitters = list()
latencia_promedio = 0
jitter_promedio = 0
conteo = 0

def desviacionEstandar(valores):
    n = len(valores)
    suma = sum(valores)
    media = suma/n
    suma_dif = sum([(valor-media)**2 for valor in valores])
    varianza = suma_dif/n
    desviacion = sqrt(varianza)
    return desviacion

def parsearElementos(p):
    global conteo
    for e in p:
        if("time" in e):
            e = e.split("=")
            if(len(e) > 1):
                conteo += 1
                tLatencias.append(float(e[1]))
    return

while True:
    if(conteo < 10):
        try:
            p = subprocess.check_output("ping  1 10.1.1.100", shell=True)
            p = p.split(" ")
            parsearElementos(p)
            print (conteo)
            sleep(1)
        except:
            print ("[>] Buscando, espere")
            sleep(2)
    else:
        break

print ("\nCalcular latencia promedio")
print (tLatencias)
latencia_promedio = sum(tLatencias)/len(tLatencias)
print ("Latencia promedio > %f"%(latencia_promedio))

print ("\nCalcular Jitter promedio")

for a, v in enumerate(tLatencias):
    try:
        tJitters.append(abs(tLatencias[a]-tLatencias[a+1]))
    except IndexError:
        pass
print (tJitters)
jitter_promedio = sum(tJitters)/len(tJitters)
print ("Jitter promedio > %f"%(jitter_promedio))

print ("\nCalcular desviacion estandar latencia")
desviacion_latencia = desviacionEstandar(tLatencias)
print ("Desviacion estandar latencia > %f"%(desviacion_latencia))

print ("\nCalcular desviacion estandar jitter")
desviacion_jitter = desviacionEstandar(tJitters)
print ("Desviacion estandar jitter > %f"%(desviacion_jitter))

with open("latencia.dat", "w") as oF:
    for a, lat in enumerate(tLatencias):
        oF.write("%d %f %f %f\n"%(a+1, lat, latencia_promedio, desviacion_latencia))

with open("jitter.dat", "w") as oF:
    for a, jit in enumerate(tJitters):
        oF.write("%d %f %f %f\n"%(a+1, jit, jitter_promedio, desviacion_jitter))

exit()
