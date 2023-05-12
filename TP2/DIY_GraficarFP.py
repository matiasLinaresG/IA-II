from DIY_Fuzzy import fuzzyfication 
import numpy as np
import matplotlib.pyplot as plt


def GraficarFuncionPertenencia(Dominio, alfa):

    posiciones = np.linspace(Dominio[0],Dominio[1],1000)

    #calcular funcion de pertenencia para cada particion
    NG = []
    NP = []
    Z = []
    PP = []
    PG = []

    for i in posiciones:
        NG.append(fuzzyfication(Dominio,alfa,i)[0])
        NP.append(fuzzyfication(Dominio,alfa,i)[1])
        Z.append(fuzzyfication(Dominio,alfa,i)[2])
        PP.append(fuzzyfication(Dominio,alfa,i)[3])
        PG.append(fuzzyfication(Dominio,alfa,i)[4])

    #graficar funcion de pertenencia

    plt.plot(posiciones,NG, label = 'NG')
    plt.plot(posiciones,NP, label = 'NP')
    plt.plot(posiciones,Z, label = 'Z')
    plt.plot(posiciones,PP, label = 'PP')
    plt.plot(posiciones,PG, label = 'PG')

    plt.legend()
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Funciones de pertenencia')

    plt.show()