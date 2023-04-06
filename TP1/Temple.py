from matplotlib import pyplot as plt

import math
import pandas as pd
import random

#importamos libreria con distribucion de boltzmann


def temple_simulado(ListaEstantes):
    #mezclamos la lista de trayectorias
    #print (Trayectorias)
    #random.shuffle(Trayectorias)

    Trayectorias = ListaEstantes


    #abrimos distancias.csv y lo guardamos en un diccionario
    Distancias = pd.read_csv("distancias.csv", index_col=0)
    #print(Distancias)
    Distancias = Distancias.to_dict()
    #print(Distancias)

    #abrimos temperatura.csv y lo guardamos en un diccionario
    Temperatura = pd.read_csv("Temperatura.csv", index_col=0)
    Temperatura = Temperatura.to_dict()
    # print(Temperatura)

    # temp_inicial = 50
    # final_temp = 1e-1
    # alpha = 0.2
    # temp_actual = temp_inicial

    temp_inicial = Temperatura["Temperatura"][0]

    temp_actual = temp_inicial


    solution = []
    costo_anterior = 200000
    lista = Trayectorias

    #agregamos lista la bahia de carga de id "carga" al inicio y al final de la lista
    lista.insert(0, 1001)
    lista.append(1001)
    lista_costos = []
    lista_temp= []
    lista_iteraciones = []

    for j in range(len(Temperatura["Temperatura"])):
        costo_actual = 0

        #eligo un indice de la lista al azar
        indice = random.randint(1, len(lista) - 2)
        #eligo un segundo indice de la lista al azar que no sea el mismo que el anterior
        indice2 = indice+1
        if indice2 > len(lista) - 2:
            indice2 = indice - 1

        #intercambio los elementos de las posiciones elegidas
        lista[indice], lista[indice2] = lista[indice2], lista[indice]


        # #aleatorizar lista
        # random.shuffle(lista)
        # print("lista", lista)
        # #lista.append(lista[0])
        # #copio la lista para poder compararla con la lista anterior

        for i in range(len(lista) - 1):
            # print(" ")
            # print(i)

            ComienzoParcial = lista[i]
            # print(Comienzo)
            FinParcial = lista[i + 1]
            # print(Fin)

            #usamos el costo actual y la distancia asociada al dataframe para calcular el costo de la solucion desde el dataframe

            #obtenemos el id de la combinacion de nodos
            ID_distancia = str(ComienzoParcial) + '-' + str(FinParcial)
            #print(ID_distancia)
            #si i es mayor que j, entonces el id es j-i o fin parcial es carga
            if ComienzoParcial > FinParcial:
                ID_distancia = str(FinParcial) + '-' + str(ComienzoParcial)
                # print("modificamos: ",ID_distancia)
            #obtenemos el costo de la combinacion de nodos utilizando el diccionario

            costo_2puntos = Distancias['distancia'][ID_distancia]
            #print(costo_2puntos)

            #""""""Notas de consulta"""""""""
            #costo_2puntos = Distancias.loc[Distancias['id'] == ID_distancia, 'distancia'].iloc[0] #iloc[0] es para obtener el valor de la celda y no el dataframe entero con el valor de la celda y el nombre de la columna
            #usar profiler
            #""""""""""""""""""""""""""""""""

            #sumamos el costo de la combinacion de nodos al costo total de la solucion
            costo_actual = costo_actual + costo_2puntos


            #print(" ")
            # print("costo anterior",costo_anterior)
            # print("costo actual", costo_actual)

        cost_diff = costo_anterior - costo_actual
        # print("costo diff")
        # print(cost_diff)
        # print(" ")
        # if the new solution is better, accept it
        if cost_diff > 0:
            # print("tomo solucion\n")
            #solucion es una copia de los valores de la lista hasta el momento
            solution = lista.copy()

            costo_anterior= costo_actual
            # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            #obtenemos 1 numero aleatorio entre de la distribucion de probabilidad de boltzman entre 0 y 1 y lo guardamos en a
            #a = boltzmann.rvs(0.5, loc=0, N=1)
            a = random.uniform(0, 1)
            b=math.exp(cost_diff / temp_actual)
            # print("a ",a)
            # print("b ",b)
            if a < b:
                # print("porque siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii tomo solucion")
                solution = lista.copy()
                costo_anterior = costo_actual

        # decrement the temperature
        #temp_actual -= alpha
        #temp_actual/=1.05
        # el comando temp_actual = lista_temp.pop(0) falla dejando el plot vacio, entonces lo hago asi
        #temp_actual = temp_actual / math.log(2.722)
        temp_actual = Temperatura["Temperatura"][j]
        #print("temp actual", temp_actual)


        # print("\nLA SOLUCION PARCIAL ES:")
        # print(solution)
        # print("\n\n")

        #guardamos costos en una lista para plotear luego
        lista_costos.append(costo_anterior)
        lista_temp.append(temp_actual)
        lista_iteraciones.append(len(lista_costos))


    print("\n\n\nLA SOLUCION ES:")
    print(solution)

    print("\n\n\nEl costo de la solucion es:")
    print(costo_anterior)
    #plotear costo anterior vs temperatura
    plt.scatter(lista_iteraciones,lista_costos)
    #plt.xlabel('Temperatura')
    #plt.ylabel('Costo')
    plt.show()


    return costo_anterior

# main
if __name__ == '__main__':
    ListaEstantes = [3, 30, 9, 10, 51, 12, 63, 14, 45, 16, 27, 18, 19, 20, 80, 23, 75]
    temple_simulado(ListaEstantes)







