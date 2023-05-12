import numpy as np
def Desfuzzyficacion(Dominio, fuzzy):
    #dominio =[limite inferior, limite superior]
    #fuzzy = [NG,NP,Z,PP,PG]

    #calcula el valor nitido por media de centros
    L0 = (Dominio[1]-Dominio[0])/4
    centros=[Dominio[0],Dominio[0]+L0, Dominio[0]+2*L0, Dominio[1]-L0, Dominio[1]]
    valor_nitido = 0
    for i in range(5):
        valor_nitido += centros[i]*fuzzy[i]
    valor_nitido = valor_nitido/np.sum(fuzzy)
    return valor_nitido



    