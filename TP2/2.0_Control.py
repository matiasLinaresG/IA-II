import numpy as np
from DIY_Fuzzy import fuzzyfication
from DIY_DesFuzzy import Desfuzzyficacion

def ControlDifuso(posicion, velocidad):
    D_posicion = [-np.pi/8, np.pi/8]
    D_velocidad = [-6.5, 6.5]
    D_Fuerza = [-40, 40]
    A_posicion = 0.5
    A_velocidad = 0.5

    posicionFuzzy = fuzzyfication(D_posicion, A_posicion, posicion)
    velocidadFuzzy = fuzzyfication(D_velocidad, A_velocidad, velocidad)

    reglas = [
        ['Z', 'PP', 'PP', 'PG', 'PG'],
        ['NP', 'Z', 'PP', 'PP', 'PG'],
        ['NP', 'NP', 'Z', 'PP', 'PP'],
        ['NG', 'NP', 'NP', 'Z', 'PP'],
        ['NG', 'NG', 'NP', 'NP', 'Z']
    ]

    reglas_agrupadas = [[] for _ in range(5)]

    for n in range(5):
        for i, antecedente in enumerate(reglas):
            for j, consecuente in enumerate(antecedente):
                if consecuente == lables[n]:
                    reglas_agrupadas[n].append([i, j])

    FuerzaFuzzy = np.zeros(5)

    for n in range(5):
        for i in range(len(reglas_agrupadas[n])):
            FuerzaFuzzy[n] = max(FuerzaFuzzy[n], min(posicionFuzzy[reglas_agrupadas[n][i][0]], velocidadFuzzy[reglas_agrupadas[n][i][1]]))

    Fuerza = Desfuzzyficacion(D_Fuerza, FuerzaFuzzy)
    return Fuerza
