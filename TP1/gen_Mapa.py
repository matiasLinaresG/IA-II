# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:59:43 2023

@author: Tomas Mercado
"""

import pandas
import numpy as np


class Mapa:
    def __init__(self,n_estantes = 20):
        # Generacion automatica de la matriz
        # La celda unitaria es la que se puede repetir en todas direcciones, esta contiene 8 estantes
        celda_unitaria_mapa = np.array([[' ', ' ', ' ', ' '],
                                        [' ', '▀', '▀', ' '],
                                        [' ', '▀', '▀', ' '],
                                        [' ', '▀', '▀', ' '],
                                        [' ', '▀', '▀', ' '],
                                        [' ', ' ', ' ', ' ']], dtype="str")
        celda_unitaria_costo = np.array([[1, 1, 1, 1],
                                         [1, 99, 99, 1],
                                         [1, 99, 99, 1],
                                         [1, 99, 99, 1],
                                         [1, 99, 99, 1],
                                         [1, 1, 1, 1]])
        # Necesito 100 estantes
        # n_celdas = math.ceil(n_estantes/8)
        # Con magia obtengo que necesito una matriz de 4x4
    
        # Armo la matriz superponiendo las celdas unitarias
        self.mapa = np.tile(celda_unitaria_mapa, (4, 4))
        self.costo = np.tile(celda_unitaria_costo, (4, 4))
        # print(mapa)
        # print(costo)
        coso = pandas.DataFrame(data=self.mapa)
        coso.to_csv("mapa.csv",header=False)
        coso = pandas.DataFrame(data=self.costo)
        coso.to_csv("costo.csv",header=False)
        
        self.asignar_ids()
        

    def asignar_ids(self):
    
        lista_posEstantes = []
        it = np.nditer(self.mapa, flags=['multi_index'])
        a = 0
        for posicion in it:
            if posicion == '▀':
                # print("%s <%s>" % (posicion, it.multi_index), end=' ')
                i, j = it.multi_index
                lista_posEstantes.append((a, i, j))
                a += 1
        # print(lista_posEstantes)
    
        # Al Mati le gustan los Dataframes
        coso = pandas.DataFrame(data=lista_posEstantes, columns=["ID", "I", "J"])
        coso.to_csv("ID_estantes.csv")
        
        return True