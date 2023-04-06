
import numpy as np
import pandas as pd

def heuristica(x,y,fin0,fin1): #se calcula la distancia de manhattan
      return abs(x-fin0)+abs(y-fin1)
def A_estrella (mapa_i, costo ,Comienzo, Fin):
    mapa=np.copy(mapa_i) #crea el mapa de la solucion

    vacio=' '
    comienzo='☆'
    fin='★'

    N_filas=len(mapa) #numero de filas
    N_col=len(mapa[0]) #numero de columnas
    mapa[Comienzo[0]][Comienzo[1]]=comienzo #posicion inicial
    mapa[Fin[0]][Fin[1]]=fin #posicion final

    #mostrar mapa
    #print(pd.DataFrame(mapa))
    #pausa=input("Presione enter para continuar")

    Mapa_path=np.copy(mapa) #crea el mapa de la solucion

    #Orden para analizar los vecinos
    vecinos=[[1,0],[0,1],[-1,0],[0,-1]] #derecha, abajo, izquierda, arriba

    nodoActual=list(Comienzo) #posicion actual

    Abiertos=[] #lista de nodos abiertos
    Cerrados=[] #lista de nodos cerrados
    Abiertosf=[] #lista de nodos abiertos con su f
    Abiertos_nodoActual=[] #lista de nodos abiertos con su nodo actual
    Solucion=[] #lista de nodos solucion
    Cerrados_anterior=[] #lista de nodos cerrados con su nodo anterior

    primera=0 #variable para saber si es la primera iteracion

    while True:
      #Es esta la posicion final?
      if mapa[nodoActual[0]][nodoActual[1]]==fin: # si es la posicion final
        I=Abiertos.index(nodoActual) #busco el indice del nodo actual en la lista de nodos abiertos
        Cerrados_anterior.append(Abiertos_nodoActual[I]) #agrego el nodo actual a la lista de nodos cerrados con su nodo anterior
        Cerrados.append(nodoActual) #agrego el nodo actual a la lista de nodos cerrados
        break

      #Que posibilidades de movimiento tengo?
      #Que hijos tengo en el nodo actual
      hijos=[] #lista de hijos del nodo actual
      for vecino in vecinos: #recorro los vecinos
        xy_v= list(np.array(nodoActual)+np.array(vecino)) #posicion del vecino
        if not(0<=xy_v[0]<N_filas) or not(0<=xy_v[1]<N_col): #si el vecino esta fuera del mapa
          continue #no lo agrego a la lista de hijos
        if (mapa[xy_v[0]][xy_v[1]]==vacio or mapa[xy_v[0]][xy_v[1]]==fin) and not([xy_v[0],xy_v[1]] in Cerrados): #si el vecino es vacio y no esta en la lista de cerrados
          hijos.append(xy_v) #agrego el vecino a la lista de hijos
          #Que f=heuristica+costo tiene el hijo?
          f=heuristica(xy_v[0],xy_v[1],Fin[0],Fin[1])+costo[xy_v[0]][xy_v[1]] #f=heuristica+costo
          #En caso de que no este se agrega el hijo a la lista de abiertos
          if not(xy_v in Abiertos): #si el vecino no esta en la lista de abiertos
            Abiertos.append(xy_v) #agrego el vecino a la lista de abiertos
            Abiertosf.append(f) #agrego el f del vecino a la lista de f de los nodos abiertos
            Abiertos_nodoActual.append(nodoActual) #agrego el nodo actual a la lista de nodos abiertos con su nodo actual

      #Se agrega a la lista de cerrados el nodo actual
      Cerrados.append(nodoActual) #agrego el nodo actual a la lista de nodos cerrados

      if primera==0: #si es la primera iteracion
        primera=1 #cambio el valor de la variable
        Cerrados_anterior.append([None,None]) #agrego un elemento a la lista de nodos cerrados con su nodo anterior
      else: #si no es la primera iteracion
        I=Abiertos.index(nodoActual) #busco el indice del nodo actual en la lista de nodos abiertos
        Cerrados_anterior.append(Abiertos_nodoActual[I]) #agrego el nodo actual a la lista de nodos cerrados con su nodo anterior


      #Se elimina al nodo actual de la lista de Abiertos
      if nodoActual in Abiertos: #si el nodo actual esta en la lista de nodos abiertos
        I=Abiertos.index(nodoActual) #busco el indice del nodo actual en la lista de nodos abiertos
        Abiertos.remove(nodoActual) #elimino el nodo actual de la lista de nodos abiertos
        Abiertosf.pop(I) #elimino el f del nodo actual de la lista de f de los nodos abiertos
        Abiertos_nodoActual.pop(I) #elimino el nodo actual de la lista de nodos abiertos con su nodo actual

      #Se elije como proximo nodo a visitar el nodo que tenga menor f
      i_min=np.argmin(Abiertosf) #busco el indice del nodo con menor f
      nodoActual=list(Abiertos[i_min]) #el nodo actual es el nodo con menor f

    Solucion.append(Fin) #agrego el nodo final a la lista de nodos solucion


    #mostrar mapa
    #print(pd.DataFrame(mapa))
    

    Comienzo=list(Comienzo)
    Solucion[-1]=list(Solucion[-1])

    #print(Solucion[-1]!=Comienzo)
    #print(Solucion[-1], type(Solucion[-1]))
    #print(Comienzo, type(Comienzo))

    while (Solucion[-1] != Comienzo):
    #while Solucion[-1]!=Comienzo: #mientras el ultimo elemento de la lista de nodos solucion no sea el nodo inicial
      I=Cerrados.index(Solucion[-1]) #busco el indice del ultimo elemento de la lista de nodos solucion en la lista de nodos cerrados
      Solucion.append(list(Cerrados_anterior[I])) #agrego el nodo anterior al ultimo elemento de la lista de nodos solucion



    #Descomentar para mostrar los elementos analizados
    #for pixel in Cerrados:
    #  Mapa_path [pixel[0]][pixel[1]]='*'

    for pixel in Solucion: #recorro la lista de nodos solucion
      Mapa_path [pixel[0]][pixel[1]]='X' #agrego el nodo solucion al mapa de la solucion

    #mostrar mapa
    #print(pd.DataFrame(Mapa_path))
    return len(Solucion) -1

def v_iguales(v1, v2):
    return all(x == y for x, y in zip(v1, v2))