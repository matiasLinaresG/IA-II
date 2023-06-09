import numpy as np


def dividir_conjunto_de_datos(x, t, porcentaje_entrenamiento):
# Calculamos la cantidad de ejemplos a usar para entrenamiento
    cantidad_entrenamiento = int(np.size(x, 0) * porcentaje_entrenamiento) # np.size(x, 0) es la cantidad de filas de x, np.size retorna el tamaño de la matriz

    # Mezclamos los datos
    indices = np.random.permutation(np.size(x, 0))
    x = x[indices]
    t = t[indices]

    # Dividimos los datos
    x_entrenamiento = x[0:cantidad_entrenamiento]
    t_entrenamiento = t[0:cantidad_entrenamiento]
    x_prueba = x[cantidad_entrenamiento:]
    t_prueba = t[cantidad_entrenamiento:]

    return x_entrenamiento, t_entrenamiento, x_prueba, t_prueba


# def dividir_conjunto_de_datos_regresion(x, porcentaje_entrenamiento):
# # Calculamos la cantidad de ejemplos a usar para entrenamiento
#     cantidad_entrenamiento = int(np.size(x, 0) * porcentaje_entrenamiento) # np.size(x, 0) es la cantidad de filas de x, np.size retorna el tamaño de la matriz

#     # Mezclamos los datos
#     indices = np.random.permutation(np.size(x, 0))
#     x = x[indices]
    
#     # Dividimos los datos
#     x_entrenamiento = x[0:cantidad_entrenamiento]
#     x_prueba = x[cantidad_entrenamiento:]

#     return x_entrenamiento, x_prueba