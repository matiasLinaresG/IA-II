from Funciones_Genetico import *
import numpy as np
import pandas as pd
import random


N_poblacionTotal=12
N_poblacionInter=7
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
#CALIDAD. La idea es no calcular otra vez la calidad de los fijos
    if k==0:
        CalidadP=Calidad(Poblacion,ordenes,IdEstantes)
    else:
        for c in CalidadP:
           print("\tCalidad ind(fijo)",c)
        CalidadP=CalidadP+Calidad(Poblacion[fijos:],ordenes,IdEstantes)
        


#SELECCION
    CalidadPInter,PoblacionInter=SelecionarPoblacion(Poblacion,CalidadP,N_poblacionInter)
#CONVERGENCIA
    #if Convergencia(CalidadPInter,N_poblacionInter-5):
    #    break

    print("Calidad minimina individuo: ",min(CalidadP))
#GENERACION DE UNA NUEVA POBLACION  <<========
    Poblacion=[]
    CalidadP=[]
#FIJOS

    Poblacion=PoblacionInter[:fijos]
    CalidadP=CalidadPInter[:fijos]
#CRUCE Y MUTACION    
    for i in range(int(nofijos/2)):
    
        Padres=random.sample(PoblacionInter,2)
        hijo1,hijo2=Cruce(Padres[0],Padres[1])
        hijo1M=Mutacion(hijo1,6)
        hijo2M=Mutacion(hijo2,6)
        Poblacion.append(hijo1M)
        Poblacion.append(hijo2M)

    #guardar la poblacion  en un archivo csv usando
    with open('poblacion.txt', 'w') as file:
        for i in range(len(Poblacion)):
            file.write(str(Poblacion[i]))
            file.write('\n')








print("==============RESPUESTA===============")
solucion=Poblacion[list(CalidadP).index(min(CalidadP))]

print("Número de iteraciones: "+str(k))
print("Distancia mas corta: "+str(min(CalidadP)))
print("Solución: "+str(solucion))
print("Última poblacion intermedia: ")
for i in range(len(PoblacionInter)):
  print("   C="+str(CalidadP[Poblacion.index(PoblacionInter[i])])+', '+str(PoblacionInter[i]))
