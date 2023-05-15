def fuzzyfication(dominio, alfa, x):
    particiones = {}
    num_particiones = 5
    ancho = (dominio[1] - dominio[0]) / (num_particiones - 1)

    centro = [dominio[0] + i * ancho for i in range(num_particiones)]

    particiones['NG'] = particion_hombro(centro[0], alfa * ancho, -1, x)
    particiones['NP'] = particion(centro[1], ancho, 0, x)
    particiones['Z'] = particion(centro[2], ancho, 0, x)
    particiones['PP'] = particion(centro[3], ancho, 0, x)
    particiones['PG'] = particion_hombro(centro[4], alfa * ancho, 1, x)

    return particiones


def particion(centro, ancho, lado, x):
    ancho_medio = ancho / 2

    if lado == -1:
        if x <= centro:
            return 1
        elif centro < x <= centro + ancho_medio:
            return (centro + ancho_medio - x) / ancho_medio
        else:
            return 0
    elif lado == 1:
        if x <= centro - ancho_medio:
            return 0
        elif centro - ancho_medio < x <= centro:
            return (x - centro + ancho_medio) / ancho_medio
        else:
            return 1
    else:
        if x <= centro - ancho_medio:
            return 0
        elif centro - ancho_medio < x <= centro:
            return (x - centro + ancho_medio) / ancho_medio
        elif centro < x <= centro + ancho_medio:
            return (centro + ancho_medio - x) / ancho_medio
        else:
            return 0


def particion_hombro(centro, ancho, lado, x):
    ancho_medio = ancho / 2

    if lado == -1:
        if x <= centro:
            return 1
        elif centro < x <= centro + ancho_medio:
            return (centro + ancho_medio - x) / ancho_medio
        else:
            return 0
    elif lado == 1:
        if x <= centro - ancho_medio:
            return 0
        elif centro - ancho_medio < x <= centro:
            return (x - centro + ancho_medio) / ancho_medio
        else:
            return 1
    else:
        return 0
