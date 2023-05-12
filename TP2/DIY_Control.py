
from DIY_Fuzzy import fuzzyfication
from DIY_GraficarFP import GraficarFuncionPertenencia
from DIY_DesFuzzy import Desfuzzyficacion
import numpy as np



def ControlDifuso(posicion,velocidad):
    #dominos y solaopamiento
    D_posicion = [-np.pi/8,np.pi/8]
    D_velocidad = [-8,8]
    D_Fuerza = [-37,37]
    A_posicion = 0.5
    A_velocidad = 0.5

    posicionFuzzy = fuzzyfication(D_posicion,A_posicion,posicion)
    velocidadFuzzy = fuzzyfication(D_velocidad,A_velocidad,velocidad)

    #reglas
    #levantar F.txt y leer reglas
    reglas = open('DIY_F.txt','r')
    reglas = reglas.readlines()
    reglas = [i.strip('\n') for i in reglas]
    reglas = [i.split(' ') for i in reglas]

    #convinaciones que implican F=NG
    lables = ['NG','NP','Z','PP','PG']
    
    reglas_agrupadas = []

    for n in range(0,5):
        reglas_agrupadas.append([])
        for i in range(0,5):
            for j in range(0,5):
                if reglas[i][j] == lables[n]:
                    reglas_agrupadas[n].append([i,j])

    #inferencia
    FuerzaFuzzy = np.zeros(5)

    for n in range(0,5):
        for i in range(0,len(reglas_agrupadas[n])):
            FuerzaFuzzy[n] = max(FuerzaFuzzy[n],min(posicionFuzzy[reglas_agrupadas[n][i][0]],velocidadFuzzy[reglas_agrupadas[n][i][1]]))

    #print(FuerzaFuzzy)
    #defuzzyficacion

    Fuerza=Desfuzzyficacion(D_Fuerza,FuerzaFuzzy)
    #print(Fuerza)
    return Fuerza





    #definir dominio y alfa

#ControlDifuso(-np.pi/8,-1)

#GraficarFuncionPertenencia([-10,10], 0.3)
