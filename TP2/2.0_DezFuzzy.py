import numpy as np
def Desfuzzyficacion(Dominio, fuzzy):
    # calcula el valor nitido por media de centros
    L0 = (Dominio[1]-Dominio[0])/4
    centros = np.linspace(Dominio[0] + L0, Dominio[1] - L0, 5)
    valor_nitido = np.sum(fuzzy * centros) / np.sum(fuzzy)
    return valor_nitido
