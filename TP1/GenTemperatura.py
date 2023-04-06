#funcion que devuelve un listado de descenso de temperatura en un archivo .csv para ser recorrido en el programa de temple simulado
#se utiliza la funcion de descenso de temperatura temp_actual = temp_actual / math.log(2.722)
import math
import pandas as pd


def GenTemperatura():
    temp_inicial = 50
    final_temp = 1e-1
    temp_actual = temp_inicial
    lista_temp= []
    lista_iteraciones = []
    i=0
    while temp_actual > final_temp:
        temp_actual = temp_actual / math.log(2.722)
        lista_temp.append(temp_actual)
        lista_iteraciones.append(i)
        i=i+1
    df = pd.DataFrame({'Iteracion': lista_iteraciones, 'Temperatura': lista_temp})
    df.to_csv('Temperatura.csv', index=False)
    print("Archivo de temperatura generado")
    print(len(lista_temp))

GenTemperatura()


