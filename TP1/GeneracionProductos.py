import numpy as np
import random



N_ordenes=100
N_maxProductos=25

#Generar ordenes de la forma 
#orden 1
#p2
#p5
#p5

#orden 2
#p65


ordenes=[]
for i in range(N_ordenes):
    productos=[]

    N_productos=1000
    while N_productos<1 or N_productos>10:
            N_productos=round(np.random.geometric(0.2))
    for j in range(int(N_productos)):
        N=-1
        while N<0 or N in productos or N>N_maxProductos:
            #distribucion geometrica
            N = round(np.random.geometric(0.15))

            #N=int(np.random.normal(0, 5, 1))
        productos.append(N)
    ordenes.append(productos)


#Generar archivo de texto con las ordenes
with open('ordenes_mod.txt', 'w') as file:
    for i in range(len(ordenes)):
        file.write("orden "+str(i+1)+"\n")
        for j in range(len(ordenes[i])):
            file.write("p"+str(ordenes[i][j])+"\n")
        file.write("\n")


