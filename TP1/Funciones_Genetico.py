import numpy as np
import random
from more_itertools import sort_together
from Temple2 import temple_simulado
import time


def DeProductosAEstantes(orden,IdEstantes,configuracion):
  orden_E=[]
  for producto in orden:
    orden_E.append(IdEstantes[configuracion.index(producto)])
  return orden_E

    

def Calidad(Poblacion_P,Ordenes_P,IdEstantes):

  Calidad = []
  for configuracion in Poblacion_P:

    calidadOrden = 0

    for orden in Ordenes_P:
      orden_E=DeProductosAEstantes(orden,IdEstantes,configuracion)
      calidadOrden += temple_simulado(orden_E)/len(orden_E)
    Calidad.append(calidadOrden)
    print ("\tcalidad individuo: ",calidadOrden)
  return list(Calidad)
       

def Cruce(padre1, padre2):
    hijo1 = []
    hijo2 = []
    #cantidad de elementos igual a "vac" en padre1
    N_vac = padre1.count('vacio')

    punto_cruce = random.randint(1, len(padre1)-1)
    
    hijo1.extend(padre1[:punto_cruce])
    for gen in padre2:
      if (gen not in list(hijo1)) or (gen=='vacio' and hijo1.count('vacio')<N_vac):
        hijo1.append(gen)

    hijo2.extend(padre2[:punto_cruce])
    for gen in padre1:
      if (gen not in list(hijo2)) or (gen=='vacio' and hijo2.count('vacio')<N_vac):
        hijo2.append(gen)

    #if len(hijo1) != len(padre1):
    #  print(hijo1.count('vacio'))
    #  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #  pausa=input("pausa")
    
    return hijo1, hijo2

def Mutacion(Individuo,cantidad):
  Copia=Individuo.copy()


  for i in range(cantidad):
    #selecionar 2 puntos al azar
    punto1=np.random.randint(0,len(Copia))
    punto2=np.random.randint(0,len(Copia))
    #intercambiar
    Copia[punto1],Copia[punto2]=Copia[punto2],Copia[punto1]


  return list(Copia)

def Convergencia(calidades,N):
  #ordenar las calidades de menor a mayor
  calidades=list(calidades)
  #contar la canticade de elementos que son iguales
  Iguales=calidades.count(calidades[0])
  return Iguales>=N

def SelecionarPoblacion(Poblacion,calidad,Cantidad):
  CalidadOrd,PoblacionOrdenada = list(sort_together([calidad, Poblacion]))

  
  return(list(CalidadOrd[:Cantidad]),list(PoblacionOrdenada[:Cantidad]))