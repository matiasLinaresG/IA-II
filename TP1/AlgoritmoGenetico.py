from Funciones_Genetico import *
import numpy as np
import pandas as pd
import random


N_poblacionTotal=10
N_poblacionInter=5
iter_max=1000

IdEstantes=pd.read_csv('ID_estantes.csv')
IdEstantes=IdEstantes["ID"].values.tolist()

IdProductos=pd.read_csv('productos.csv')
IdProductos=IdProductos["id"].values.tolist()

#leer el archivo order1.txt y guardar su informacoin en una lista de listas. esta separado po 'n y ,
with open('ordenes_ordenadas.txt', 'r') as file:
    contenido = file.read()

ordenes = contenido.split('\n')
for i in range(len(ordenes)):
    ordenes[i]=ordenes[i].split(',')


#igualar la canditad de productos y la cantidad de estantes rellendo prucuntos  con "vacio"
for i in range(len(IdEstantes)-len(IdProductos)):
  IdProductos.append("vacio")


Poblacion=[]

for i in range(N_poblacionTotal):
  Poblacion.append(np.random.permutation(IdProductos).tolist()) 

fijos=round(N_poblacionInter*0.4)
nofijos=N_poblacionTotal-fijos

if nofijos%2!=0:
    nofijos+=1
    fijos-=1



for k in range(iter_max):
    print("ITERACION NUMERO: ",k)

    if k==0:
        CalidadP=Calidad(Poblacion,ordenes,IdEstantes)
    else:
        CalidadP.append(Calidad(Poblacion[fijos+1:],ordenes,IdEstantes))

    CalidadPInter,PoblacionInter=SelecionarPoblacion(Poblacion,CalidadP,N_poblacionInter)

    #if Convergencia(CalidadPInter,N_poblacionInter-5):
    #    break

    print("Calidad minimina individuo: ",min(CalidadP))

    Poblacion=[]
    CalidadP=[]


    for i in range(fijos):
        Poblacion.append(PoblacionInter[i])
        CalidadP.append(CalidadPInter[i])
    
    for i in range(int(nofijos/2)):
    
        Padres=random.sample(PoblacionInter,2)
        hijo1,hijo2=Cruce(Padres[0],Padres[1])
        hijo1M=Mutacion(hijo1,10)
        hijo2M=Mutacion(hijo2,10)
        Poblacion.append(hijo1M)
        Poblacion.append(hijo2M)

        # print("     --------------------------------------------")
        # print("     "+str(Padres[0])+"-->"+str(hijo1)+"-->"+str(hijo1M))
        # print("     "+str(Padres[1])+"-->"+str(hijo2)+"-->"+str(hijo2M))




print("==============RESPUESTA===============")
solucion=Poblacion[list(CalidadP).index(min(CalidadP))]

print("Número de iteraciones: "+str(k))
print("Distancia mas corta: "+str(min(CalidadP)))
print("Solución: "+str(solucion))
print("Última poblacion intermedia: ")
for i in range(len(PoblacionInter)):
  print("   C="+str(CalidadP[Poblacion.index(PoblacionInter[i])])+', '+str(PoblacionInter[i]))
