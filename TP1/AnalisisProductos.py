import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open('ordenes_mod.txt', 'r') as file:
    contenido = file.read()

ordenes = contenido.split('\n\n')


#quitar el primer elemento de las listas de ordenes
for i in range(len(ordenes)):
    #borrar el primer elemento
    ordenes[i] = ordenes[i].split('\n')
    ordenes[i].pop(0)

for i in range(len(ordenes)):
    if ordenes[i] == []:
        ordenes.pop(i)   

print(ordenes)       
#guardar en un archivo de texto las ordenes
with open('ordenes_ordenadas.txt', 'w') as file:
    for i in range(len(ordenes)):
        for j in range(len(ordenes[i])):
            file.write(ordenes[i][j])
            if j < len(ordenes[i])-1:
                file.write(",")
        file.write("\n")

#guardar en un csv on pandas los id de los productos ordenados y sin repetir
productos = []
for i in range(len(ordenes)):
    for j in range(len(ordenes[i])):
        if ordenes[i][j] not in productos:
            productos.append(ordenes[i][j])

productos.sort()

df = pd.DataFrame(productos, columns=['id'])
df.to_csv('productos.csv', index=False)


#pausa = input("Presione una tecla para continuar...")

#contar cuantas veces se repite cada producto en las ordenes
productos = []
for i in range(len(ordenes)):
    for j in range(len(ordenes[i])):
        if ordenes[i][j] not in productos:
            productos.append(ordenes[i][j])
            
for i in range(len(productos)):
    productos[i] = [productos[i], 0]

for i in range(len(ordenes)):
    for j in range(len(ordenes[i])):
        for k in range(len(productos)):
            if ordenes[i][j] == productos[k][0]:
                productos[k][1] += 1


#graficar en un diagrama de barras la cantidad de veces que se repite cada producto
#grafica en la misma ventana la catidad de produntos por orden
#ordenar de mayor a menor


productos.sort(key=lambda x: x[1], reverse=True)
#quitar la p
for i in range(len(productos)):

    productos[i][0] = int(productos[i][0][1:])


#graficar en una ventana
plt.figure(1)
plt.subplot(211)
plt.bar([i[0] for i in productos], [i[1] for i in productos])
plt.title("Cantidad de productos por orden")
plt.xlabel("Productos")
plt.ylabel("Cantidad de veces que se repite")

#graficar en otra ventana
plt.subplot(212)
plt.bar([i for i in range(len(ordenes))], [len(i) for i in ordenes])
plt.title("Cantidad de productos por orden")
plt.xlabel("Ordenes")
plt.ylabel("Cantidad de productos")
plt.show()


#x = np.arange(len(productos))
#plt.bar(x, [i[1] for i in productos])
#plt.xticks(x, [i[0] for i in productos])
#plt.show()



#print(productos)
