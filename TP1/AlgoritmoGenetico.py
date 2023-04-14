from Funciones_Genetico import *
import numpy as np
import pandas as pd
import random
import time
import multiprocessing as mt


def calculate(func, args):
    result = func(*args)
    return result


def calculatestar(args):
    return calculate(*args)


if __name__ == '__main__':
    # Ajustes
    N_poblacionTotal = 12
    N_poblacionInter = 7
    iter_max = 11
    Poblacion_anterior = True


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

    Poblacion = []
    
    if Poblacion_anterior:
        # levantar la poblacion del archivo txt "poblacion"
        with open('poblacion.txt', 'r') as file:
            contenido = file.read()

        Poblacion = contenido.split('\n')
        for i in range(len(Poblacion)):
            Poblacion[i] = Poblacion[i].split(',')

        # print(Poblacion[1])
    else:
        for i in range(N_poblacionTotal):
            Poblacion.append(np.random.permutation(IdProductos).tolist())

    fijos = round(N_poblacionInter*0.4)
    nofijos = N_poblacionTotal-fijos

    if nofijos % 2 != 0:
        nofijos -= 1
        fijos += 1
    # Timestamp para el tiempo total de ejecucion
    t1 = time.time()
    
    for k in range(iter_max):
        print("ITERACION NUMERO: ", k)
    # CALIDAD. La idea es no calcular otra vez la calidad de los fijos
        if k == 0:
            # Pruebo hacerlo en un Pool
            t0 = time.time()
            with mt.Pool() as pool:
                tareas = [(Calidad_individual, (indiv, ordenes, IdEstantes))
                          for indiv in Poblacion]
                try:
                    CalidadP = pool.map(calculatestar, tareas)
                except mt.TimeoutError:
                    print("Se acabo el tiempo")
                    
            print("\tTarde en calcular: {:.2f}s".format(time.time()-t0))
            # t0 = time.time()
            # CalidadP2 = Calidad(Poblacion, ordenes, IdEstantes)
            # print("A la antigua tardaba en calcular todo: (s) "+str(time.time()-t0))
            
        else:
            t0 = time.time()
            with mt.Pool() as pool:
                tareas = [(Calidad_individual, (indiv, ordenes, IdEstantes))
                          for indiv in Poblacion[fijos:]]
                try:
                    CalidadNOfijos = pool.map(calculatestar, tareas)
                except mt.TimeoutError:
                    print("Se acabo el tiempo")
            CalidadP += CalidadNOfijos
            print("\tTarde en calcular: {:.2f}s".format(time.time()-t0))
            # t0 = time.time()
            # for c in CalidadP:
            #     print("\tCalidad ind(fijo)", c)
            # CalidadP = CalidadP+Calidad(Poblacion[fijos:], ordenes, IdEstantes)
            # print("A la antigua tardaba en calcular todo: (s) "+str(time.time()-t0))

    # SELECCION
        CalidadPInter, PoblacionInter = SelecionarPoblacion(
            Poblacion, CalidadP, N_poblacionInter)
    # CONVERGENCIA
        # if Convergencia(CalidadPInter,N_poblacionInter-5):
        #    break

        print("\tCalidad minimina individuo: ", min(CalidadP))
    # GENERACION DE UNA NUEVA POBLACION  <<========
        Poblacion = []
        CalidadP = []
    # FIJOS

        Poblacion = PoblacionInter[:fijos]
        CalidadP = CalidadPInter[:fijos]
    # CRUCE Y MUTACION
        for i in range(int(nofijos/2)):

            Padres = random.sample(PoblacionInter, 2)
            hijo1, hijo2 = Cruce(Padres[0], Padres[1])
            hijo1M = Mutacion(hijo1, 20)
            hijo2M = Mutacion(hijo2, 20)
            Poblacion.append(hijo1M)
            Poblacion.append(hijo2M)

        # guardar la poblacion  en un archivo csv usando
        with open('poblacion.txt', 'w') as file:
            for i in range(len(Poblacion)):
                for j in range(len(Poblacion[i])):
                    file.write(str(Poblacion[i][j]))
                    if j < len(Poblacion[i])-1:
                        file.write(",")
                if i < len(Poblacion)-1:
                    file.write("\n")
    
    print("==============RESPUESTA===============")
    solucion = Poblacion[list(CalidadP).index(min(CalidadP))]
    print("Tarde: {:.2f} minutos en hacer {} iteraciones".format((time.time()-t1)/60,k))
    # print("Número de iteraciones: "+str(k))
    print("Distancia mas corta: "+str(min(CalidadP)))
    # print("Solución: "+str(solucion))
    # print("Última poblacion intermedia: ")
    # for i in range(len(PoblacionInter)):
    #   print("   C="+str(CalidadP[Poblacion.index(PoblacionInter[i])])+', '+str(PoblacionInter[i]))
