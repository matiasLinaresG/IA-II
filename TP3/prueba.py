import numpy as np
import matplotlib.pyplot as plt

def graficaresultado(F,XYZ,labels):



    # Extrae los valores de X e Y de los pares en XY
    X = [x for x,_ ,_ in XYZ]
    Y = [y for _, y,_ in XYZ]
    Z = [z for _, _,z in XYZ]

    # Grafica los resultados
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf=ax.scatter(X, Y, Z, c=F, cmap='viridis')

    # Configuración de los ejes y el título
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    ax.set_title('Acuaraccy')
    # Mostrar la escala de colores, name 'surface' is not defined
    fig.colorbar(surf, shrink=0.7, aspect=15)

    #marcar el punto de máxima acuaraccy con una estrella y mostrar el valor de los parámetros
    maximo = np.max(F)
    maximo_index = F.index(maximo)
    maximo_XYZ = XYZ[maximo_index]
    maximo_X = maximo_XYZ[0]
    maximo_Y = maximo_XYZ[1]
    maximo_Z = maximo_XYZ[2]
    ax.scatter(maximo_X, maximo_Y, maximo_Z, marker='*', s=100, c='r')
    texto='maximo: ' + str(round(maximo,3)) + '\n' + labels[0] + ': ' + str(round(maximo_X,3)) + '\n' + labels[1] + ': ' + str(round(maximo_Y,3)) + '\n' + labels[2] + ': ' + str(round(maximo_Z,3))
    #texto2_decimales = 'maximo: ' + str(maximo) + '\n' + labels[0] + ': ' + str(round(maximo_X,2)) + '\n' + labels[1] + ': ' + str(round(maximo_Y,2)) + '\n' + labels[2] + ': ' + str(round(maximo_Z,2))
    ax.text(maximo_X, maximo_Y, maximo_Z, texto, color='r')
    

    plt.show()

def funcion(x, y , z):
    # Define aquí tu función F que depende de X e Y
    return x**2 + y**2 - z**2

# Pares de elementos X e Y
XYZ = [(np.random.uniform(0, 10), np.random.uniform(0, 10), np.random.uniform(0, 10)) for i in range(500)]

# Calcula los valores de F para cada par de elementos en XY
F = [funcion(x, y, z) for x, y,z in XYZ]

# Grafica los resultados
graficaresultado(F, XYZ, ['X', 'Y','Z'])