
def fuzzyfication(Dominio, alfa, x):
    # devuelve el valor de la funcion de pertenencia a cada particion en la posicion x
    # Dominio es una lista con el valor minimo y maximo del dominio
    # alfa es el porcentaje de solapamiento entre particiones
    # x es el valor nitido
    #el numero de particiones es 5 (NG, NP, Z, PP, PG)

    # calculo del ancho de las particiones cinsiderando la superposicion alfa
    L0= (Dominio[1]-Dominio[0])/4
    L = L0/(1-alfa)

    centro = [Dominio[0], Dominio[0]+L0, Dominio[0]+2*L0, Dominio[1]-L0, Dominio[1]]
    # calculo del valor de la funcion de pertenencia en cada particion utilizando la funcion particion y particion_hombro
    
    NG = particion_hombro(centro[0],L,-1,x)
    NP = particion(centro[1],L,0,x)
    Z = particion(centro[2],L,0,x)
    PP = particion(centro[3],L,0,x)
    PG = particion_hombro(centro[4],L,1,x)

    return [NG, NP, Z, PP, PG]


   

def particion(centro,L,lado, x):
    # devuelve el valor de la particion en la posicion
    # centro es el valor del centro de la particion
    # L es el ancho de la particion
    # x es el valor nitido

    L = L/2

    if lado == -1:
        if x <= centro:
            return 1
        elif x > centro and x <= centro+L:
            return (centro+L-x)/L
        else:
            return 0
    elif lado == 1:
        if x <= centro-L:
            return 0
        elif x > centro-L and x <= centro:
            return (x-centro+L)/L
        else:
            return 1
    
    else: 
        if x <= centro-L:
            return 0
        elif x > centro-L and x <= centro:
            return (x-centro+L)/L
        elif x > centro and x <= centro+L:
            return (centro+L-x)/L
        else:
            return 0
    
def particion_hombro(centro,L,lado,x):
    # devuelve el valor de la particion en la posicion
    # centro es el valor del centro de la particion
    # L es el ancho de la particion
    # lado es el lado de la particion (-1 izquierda, 1 derecha)
    # x es el valor nitido

    L = L/2
    if lado == -1:
        if x <= centro:
            return 1
        elif x > centro and x <= centro+L:
            return (centro+L-x)/L
        else:
            return 0
    elif lado == 1:
        if x <= centro-L:
            return 0
        elif x > centro-L and x <= centro:
            return (x-centro+L)/L
        else:
            return 1
    else:
        return 0