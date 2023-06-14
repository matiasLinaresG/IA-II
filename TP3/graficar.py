
import numpy as np
import matplotlib.pyplot as plt
def graficaresultado(F,XYZ,labels,titulo,fig):



    # Extrae los valores de X e Y de los pares en XY
    X = [x for x,_ ,_ in XYZ]
    Y = [y for _, y,_ in XYZ]
    Z = [z for _, _,z in XYZ]

    # Grafica los resultados
    
    ax = fig.add_subplot(111, projection='3d',label=titulo)
    surf=ax.scatter(X, Y, Z, c=F, cmap='viridis',label=titulo)

    # Configuración de los ejes y el título
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    ax.set_title(titulo)
    # Mostrar la escala de colores, name 'surface' is not defined
    fig.colorbar(surf, shrink=0.7, aspect=15)

    #marcar el punto de máxima acuaraccy con una estrella y mostrar el valor de los parámetros
    maximo = np.max(F)
    maximo_index = F.index(maximo)
    maximo_XYZ = XYZ[maximo_index]
    maximo_X = maximo_XYZ[0]
    maximo_Y = maximo_XYZ[1]
    maximo_Z = maximo_XYZ[2]
    ax.scatter(maximo_X, maximo_Y, maximo_Z, marker='*', s=100, c='r', label=titulo)
    texto='maximo: ' + str(round(maximo,6)) + '\n' + labels[0] + ': ' + str(round(maximo_X,5)) + '\n' + labels[1] + ': ' + str(round(maximo_Y,5)) + '\n' + labels[2] + ': ' + str(round(maximo_Z,5))
    #texto2_decimales = 'maximo: ' + str(maximo) + '\n' + labels[0] + ': ' + str(round(maximo_X,2)) + '\n' + labels[1] + ': ' + str(round(maximo_Y,2)) + '\n' + labels[2] + ': ' + str(round(maximo_Z,2))
    ax.text(maximo_X, maximo_Y, maximo_Z, texto, color='r')

   
