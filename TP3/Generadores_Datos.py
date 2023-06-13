import numpy as np


def generar_datos_clasificacion(cantidad_ejemplos, cantidad_clases):
    FACTOR_ANGULO = 0.79
    AMPLITUD_ALEATORIEDAD = 0.1

    # Calculamos la cantidad de puntos por cada clase, asumiendo la misma cantidad para cada
    # una (clases balanceadas)
    n = int(cantidad_ejemplos / cantidad_clases)

    # Entradas: 2 columnas (x1 y x2)
    x = np.zeros((cantidad_ejemplos, 2))
    #x es 
    # Salida deseada ("target"): 1 columna que contendra la clase correspondiente (codificada como un entero)
    t = np.zeros(cantidad_ejemplos, dtype="uint8")  # 1 columna: la clase correspondiente (t -> "target")
    # t es
    randomgen = np.random.default_rng()

    # Por cada clase (que va de 0 a cantidad_clases)...
    for clase in range(cantidad_clases):
        # Tomando la ecuacion parametrica del circulo (x = r * cos(t), y = r * sin(t)), generamos
        # radios distribuidos uniformemente entre 0 y 1 para la clase actual, y agregamos un poco de
        # aleatoriedad
        radios = np.linspace(0, 1, n) + AMPLITUD_ALEATORIEDAD * randomgen.standard_normal(
            size=n)  # np.linspace(0, 1, n) es un vector de n elementos entre 0 y 1/ randomgen.standard_normal(size=n) es un vector de n elementos aleatorios con distribucion normal, valores entre -1 y 1

        # ... y angulos distribuidos tambien uniformemente, con un desfasaje por cada clase
        angulos = np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO,
                              n)  # np.linspace(clase * np.pi * FACTOR_ANGULO, (clase + 1) * np.pi * FACTOR_ANGULO, n) realiza una particion de n elementos entre clase * np.pi * FACTOR_ANGULO y (clase + 1) * np.pi * FACTOR_ANGULO, en valores: clase * np.pi * FACTOR_ANGULO, clase * np.pi * FACTOR_ANGULO + (1 * np.pi * FACTOR_ANGULO - clase * np.pi * FACTOR_ANGULO) / (n - 1), clase * np.pi * FACTOR_ANGULO + 2 * (1 * np.pi * FACTOR_ANGULO - clase * np.pi * FACTOR_ANGULO) / (n - 1), ..., (clase + 1) * np.pi * FACTOR_ANGULO

        # Generamos un rango con los subindices de cada punto de esta clase. Este rango se va
        # desplazando para cada clase: para la primera clase los indices estan en [0, n-1], para
        # la segunda clase estan en [n, (2 * n) - 1], etc.
        indices = range(clase * n, (clase + 1) * n)

        # Generamos las "entradas", los valores de las variables independientes. Las variables:
        # radios, angulos e indices tienen n elementos cada una, por lo que le estamos agregando
        # tambien n elementos a la variable x (que incorpora ambas entradas, x1 y x2)
        x1 = radios * np.sin(angulos)
        x2 = radios * np.cos(angulos)
        x[indices] = np.c_[x1, x2]
        #np.c es una funcion que concatena vectores, en este caso concatena x1 y x2, es decir, x[indices] = [x1, x2]
        # Guardamos el valor de la clase que le vamos a asociar a las entradas x1 y x2 que acabamos
        # de generar
        t[indices] = clase

        #t es un vector de 100 elementos, cada elemento es un entero entre 0 y 2, se relaciona con x, por ejemplo, x[0] tiene como salida deseada t[0] = 0, x[1] tiene como salida deseada t[1] = 0, ..., x[99] tiene como salida deseada t[99] = 2

    return x, t

def generar_datos_continuos(num_puntos, num_clases): #para clasificacion
    puntos = []
    etiquetas = []
    
    for i in range(num_clases):
        radio = np.random.uniform(0, 1)
        angulo = np.random.uniform(0, 2*np.pi)
        mean = [radio * np.cos(angulo), radio * np.sin(angulo)]
        cov = [[0.1, 0], [0, 0.1]]  # Covarianza para controlar la dispersión
        
        puntos_clase = np.random.multivariate_normal(mean, cov, num_puntos // num_clases)
        etiquetas_clase = np.full(num_puntos // num_clases, i)
        
        puntos.extend(puntos_clase)
        etiquetas.extend(etiquetas_clase)
    
    return np.array(puntos), np.array(etiquetas)



def generar_datos_regresion(num_puntos, rango_x): #con 2 entradas y 1 salida
    #x es un vector de 100 elementos, cada elemento es un vector de 2 elementos, cada elemento del vector es un numero real entre -1 y 1
    x = np.random.uniform(rango_x[0], rango_x[1], size=(num_puntos, 2))
    #t es un vector de 100 elementos, cada elemento es un numero real entre -1 y 1
    t = np.sin(x[:, 0]) + np.cos(x[:, 1])

    t = t.reshape(-1, 1)
    #se imprimen las dimensiones de las matrices
    print("x.shape: ", x.shape)
    print("t.shape: ", t.shape)
    
    return x, t

# Punto 4: 
# +Generador con sklearn:


def generar_datos_sklearn(cantidad_ejemplos, cantidad_clases):
    from sklearn.datasets import make_blobs
    
    # Genera manchas redondas bien separadas. A veces no todas las clases son linealmente separables.
    X, y = make_blobs(n_samples=cantidad_ejemplos,
                      n_features=2, centers=cantidad_clases)

    return X, y


# +Generador casero. En un circulo de radio aleatorio se ubican las m clases
    # cada una con n_datos/m ejemplos.
    
    # La ec parametrica del circulo es: (x = r * cos(t), y = r * sin(t))
    # t va a ser un numero aleatorio
    # Por ahora el centro es (0,0)

def generar_datos_caseros(cantidad_ejemplos=100, cantidad_clases=1):
    import numpy as np
    m = cantidad_clases

    n_datos = cantidad_ejemplos

    n = int(np.rint(n_datos/m))

    # cov = np.eye(2)  # Usamos la identidad como covarianza
    cov = np.array([[0.1,0],[0,0.1]])

    rng = np.random.default_rng()
    listaX = []  # Creo una lista de arrays que luego uno en un solo array
    listaT = []
    r = rng.random()
    # Genero una distribucion para cada clase
    for i in range(m):
        t = rng.random()*2*np.pi
        centro = np.rint([r*np.cos(t), r*np.sin(t)])
        # print("Centro: "+str(centro))

        # Genero los datos gausianos:
        # datos, clase = generarGaussiana(n, centro, cov, i)
        datos = np.array(rng.multivariate_normal(centro, cov, n))
        clase = np.full(datos.shape[0], i)
        # graficar_datos(datos, clase)

        listaX.append(datos)
        listaT.append(clase)

    Xsal = np.concatenate(listaX)
    tsal = np.concatenate(listaT)
    # graficar_datos(Xsal, tsal)
    return Xsal, tsal

# Herramienta para graficar la distribucion de puntos.

def graficar_datos(x, t):
    import matplotlib.pyplot as plt
    plt.scatter(x[:, 0], x[:, 1], marker="o", c=t, s=25, edgecolor="k")
    plt.show()
    return
