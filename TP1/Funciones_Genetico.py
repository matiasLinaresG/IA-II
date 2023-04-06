import numpy as np
import random
from more_itertools import sort_together
from Temple import temple_simulado


def DeProductosAEstantes(orden,IdEstantes,configuracion):
  orden_E=[]
  for producto in orden:
    orden_E.append(IdEstantes[configuracion.index(producto)])
  return orden_E


def Calidad(Poblacion_P,Ordenes_P,IdEstantes):

  Calidad = []
  for configuracion in Poblacion_P:
    print('1 individuo')

    calidadOrden = 0
    for orden in Ordenes_P:
      orden_E=DeProductosAEstantes(orden,IdEstantes,configuracion)
      calidadOrden += temple_simulado(orden_E)/len(orden_E)
    Calidad.append(calidadOrden)
    print ("calidad individuo: ",calidadOrden)
  return Calidad
       

def Cruce(padre1, padre2):
    hijo1 = []
    hijo2 = []
    Partida=padre1[0]
    Entrega=padre1[-1]

    padre1=padre1[1:-1]
    padre2=padre2[1:-1]

    punto_cruce = random.randint(1, len(padre1)-1)
    
    hijo1.extend(padre1[:punto_cruce])
    for gen in padre2:
        if list(gen) not in list(hijo1):
            hijo1.append(list(gen))

    
    hijo2.extend(padre2[:punto_cruce])
    for gen in padre1:
        if list(gen) not in list(hijo2):
            hijo2.append(list(gen))

    hijo1.insert(0,Partida)
    hijo1.append(Entrega)
    hijo2.insert(0,Partida)
    hijo2.append(Entrega)
    
    return hijo1, hijo2

def Mutacion(Individuo,cantidad):
  Copia=list(np.copy(Individuo))

  Partida=Copia[0]
  Entrega=Copia[-1]
  Copia=Copia[1:-1]

  for i in range(cantidad):
    #selecionar 2 puntos al azar
    punto1=np.random.randint(0,len(Copia))
    punto2=np.random.randint(0,len(Copia))
    #intercambiar
    Copia[punto1],Copia[punto2]=Copia[punto2],Copia[punto1]

  Copia.insert(0,Partida)
  Copia.append(Entrega)

  return list(Copia)

def Convergencia(calidades,N):
  #ordenar las calidades de menor a mayor
  calidades=list(calidades)
  #contar la canticade de elementos que son iguales
  Iguales=calidades.count(calidades[0])
  return Iguales>=N

def SelecionarPoblacion(Poblacion,calidad,Cantidad):
  CalidadOrd,PoblacionOrdenada = list(sort_together([calidad, Poblacion]))

  
  return(CalidadOrd[:Cantidad],list(PoblacionOrdenada[:Cantidad]))