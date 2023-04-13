from Funciones_Genetico import Calidad_individual
from more_itertools import sort_together
import numpy as np
import pandas as pd

with open('poblacion.txt', 'r') as file:
    contenido = file.read()
    Poblacion = contenido.split('\n')
    for i in range(len(Poblacion)):
        Poblacion[i] = Poblacion[i].split(',')

IdEstantes = pd.read_csv('ID_estantes.csv')
IdEstantes = IdEstantes["ID"].values.tolist()

IdProductos = pd.read_csv('productos.csv')
IdProductos = IdProductos["id"].values.tolist()

# leer el archivo order1.txt y guardar su informacoin en una lista de listas. esta separado po 'n y ,
with open('ordenes_ordenadas.txt', 'r') as file:
    contenido = file.read()
ordenes = contenido.split('\n')
for i in range(len(ordenes)):
    ordenes[i] = ordenes[i].split(',')

# igualar la canditad de productos y la cantidad de estantes rellendo prucuntos  con "vacio"
for i in range(len(IdEstantes)-len(IdProductos)):
    IdProductos.append("vacio")

IdAlmacen=pd.read_csv('ID_estantes.csv')


calidad = []
for individuo in Poblacion:
    calidad.append(Calidad_individual(individuo, ordenes, IdEstantes))

mapa=pd.read_csv('mapa.csv')
mapa=mapa.values.tolist()
#agregar una fila 0 de ' ' al mapa
mapa.insert(0, [' ']*len(mapa[0]))


#ordenar la poblacion de mayor a menor calidad
CalidadOrd, PoblacionOrdenada = list(sort_together([calidad, Poblacion]))

for producto in Poblacion[0]:
    if producto=="vacio":
        continue
    #de producto a estante
    index_estante=IdProductos.index(producto)
    #de estante a coordenada
    #valor de la columna "I" donde la columna "ID" sea igual a IDestante
    I=IdAlmacen["I"][index_estante]
    J=IdAlmacen["J"][index_estante]
    mapa[I][J]=producto
    

#mostrar mapa 

print(pd.DataFrame(mapa))