
from DIY_Fuzzy import fuzzyfication
from DIY_GraficarFP import GraficarFuncionPertenencia
from DIY_DesFuzzy import Desfuzzyficacion
import numpy as np




def ControlDifuso(posicion,velocidad):

    #dominos y solaopamiento
    D_posicion = [-np.pi/2,np.pi/2]
    D_velocidad = [-6,6]
    D_Fuerza = [-80,80]
    A_posicion = 0.5
    A_velocidad = 0.5

    posicionFuzzy = fuzzyfication(D_posicion,A_posicion,posicion)
    velocidadFuzzy = fuzzyfication(D_velocidad,A_velocidad,velocidad)


    #reglas
    #levantar F.txt y leer reglas
    #reglas = open('DIY_F.txt','r')
    #reglas = reglas.readlines()
    #reglas = [i.strip('\n') for i in reglas]
    #reglas = [i.split(' ') for i in reglas]

    #reglas=[['Z','PP','PP','PG','PG'],
    #        ['NP','Z','PP','PP','PG'],
    #        ['NP','NP','Z','PP','PP'],
    #        ['NG','NP','NP','Z','PP'],
    #        ['NG','NG','NP','NP','Z']]
    
    reglas=[['NG','NG','NG','NP','Z'],
            ['NG','NG','NP','Z','PP'],
            ['NG','NP','Z','PP','PG'],
            ['NP','Z','PP','PG','PG'],
            ['Z','PP','PG','PG','PG']]



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
    #agregar nueva fila sin append

    # guardar posicion, velocidad, posicionFuzzy, velocidadFuzzy, FuerzaFuzzy, 
    # Fuerza en un archivo de llamado data.txt como una fila mas, si este no exixte crearlo
    guardar=0
    if guardar:
        with open('data.txt','a') as f:
            f.write('----------------------------------------\n')
        
            #posicion en gados, minutos y segundos
            grados = int(posicion*180/np.pi)
            minutos = int((posicion*180/np.pi-int(posicion*180/np.pi))*60)
            segundos = round((((posicion*180/np.pi-int(posicion*180/np.pi))*60)-int((posicion*180/np.pi-int(posicion*180/np.pi))*60))*60,6)

            f.write('posicion: '+str(grados)+'g '+str(minutos)+'m '+str(segundos)+'s  --> [')
            for i in range(0,5):
                f.write(str(round(posicionFuzzy[i],4))+' ')
            f.write(']\n')

            f.write('velocidad:  '+str(round(velocidad,6))+'--> [')
            for i in range(0,5):
                f.write(str(round(velocidadFuzzy[i],4))+' ')
            f.write(']\n')
                    
            #que los valores de FuerzaFuzzy esten  con 3 decimales
            f.write('FuerzaFuzzy: [')
            for i in range(0,5):
                f.write(str(round(FuerzaFuzzy[i],4))+' ')
            f.write('] -->'+str(Fuerza)+'\n')



    return Fuerza





    #definir dominio y alfa

#ControlDifuso(-np.pi/8,-1)

#GraficarFuncionPertenencia([-10,10], 0.3)
