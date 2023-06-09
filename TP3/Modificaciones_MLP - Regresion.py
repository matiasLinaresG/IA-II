import numpy as np
import matplotlib.pyplot as plt
import Generadores_Datos as gd
import Divisores as div

# Generador basado en ejemplo del curso CS231 de Stanford:
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)




def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):  # n_entrada = 2, n_capa_2 = 25, n_capa_3 = 3
    # Inicializamos los pesos de la red con valores aleatorios con distribucion normal
    # (media = 0, desvio estandar = 0.1)

    randomgen = np.random.default_rng()  # np.random.default_rng() es un generador de numeros aleatorios

    w1 = 0.1 * randomgen.standard_normal((n_entrada,
                                          n_capa_2))  # np.random.standard_normal((n_entrada, n_capa_2)) es una matriz de n_entrada filas y n_capa_2 columnas con valores aleatorios con distribucion normal, media = 0, desvio estandar = 1
    b1 = 0.1 * randomgen.standard_normal((1,
                                          n_capa_2))  # np.random.standard_normal((1, n_capa_2)) es una matriz de 1 fila y n_capa_2 columnas con valores aleatorios con distribucion normal, media = 0, desvio estandar = 1

    w2 = 0.1 * randomgen.standard_normal((n_capa_2,
                                          n_capa_3))  # ramdomgen.standard_normal((n_capa_2, n_capa_3)) es una matriz de n_capa_2 filas y n_capa_3 columnas con valores aleatorios con distribucion normal, media = 0, desvio estandar = 1
    b2 = 0.1 * randomgen.standard_normal((1,
                                          n_capa_3))  # np.random.standard_normal((1,n_capa_3)) es una matriz de 1 fila y n_capa_3 columnas con valores aleatorios con distribucion normal, media = 0, desvio estandar = 1

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]  # x.dot es un producto matricial, dot es de la libreria numpy, se usa para multiplicar matrices

    # Funcion de activacion lineal para la capa oculta (h -> "hidden")

    h = z  # h es la salida de la capa oculta, es decir, la entrada de la capa de salida


    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)

    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores


# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, xtest, ttest, pesos, learning_rate, epochs):  # train es una funcion que recibe 5 parametros, x, t, pesos, learning_rate y epochs, realiza el entrenamiento de la red neuronal con los datos de entrada x y la salida correcta t, los pesos de la red se encuentran en el diccionario pesos, el learning_rate es la tasa de aprendizaje y epochs es la cantidad de iteraciones que se realizan para entrenar la red
    # Cantidad de filas (i.e. cantidad de ejemplos)
    
    numero_clases = 3
    numero_ejemplos = 300

    lista_loss = []
    lista_lossval = []
    lista_precision_prueba = []

    #relaizamos una copia de x y t para no modificar los datos originales
    xcopy = x.copy()
    tcopy = t.copy()
    #xnew, tnew = generar_datos_clasificacion(numero_ejemplos, numero_clases)
    #xnew2, tnew2 = generar_datos_clasificacion(numero_ejemplos, numero_clases)
    x_precision=xtest
    t_precision=ttest
    _, _, x_val, t_val = div.dividir_conjunto_de_datos(xcopy,tcopy, 0.7)
#   x_barrido, t_barrido, x_pruebaval, t_pruebaval = dividir_conjunto_de_datos(x, t, 0.9)
    best_loss = float("inf")
    best_accuracy = 0
    patience = 0
    validation_frequency=100


    for i in range(epochs):
        m = x.shape[0]  # cantidad de ejemplos
        
        # LOSS
        y,h,z,loss =  calcular_loss(x, t, pesos)
        _,_,_,lossval = calcular_loss(x_val, t_val, pesos)
        #guardo los valores de loss en una lista para graficarlos
        lista_loss.append(loss)
        lista_lossval.append(lossval)
        ##################################################################################Calculo de Precision#########################################################################################

        # # e. calculo accuracy con val de train
        # predicciones = clasificar(x, pesos)
        # precision = np.mean(predicciones == t)

        # e. calculo accuracy con datos de precision
        predicciones_precision = clasificar(x_precision, pesos)
        precision_prueba = np.mean(predicciones_precision == t_precision)

        

        #guardamos la precision prueba en una lista para graficarla
        lista_precision_prueba.append(precision_prueba)

        # f.se agrega parada temprana, con un conjunto distinto al de entrenamiento (validacion), se verifica el valor de loss o de accuracy cada N epochs (donde N es un parámetro de configuración) utilizando el conjunto de validación, y se detiene el entrenamiento en caso de que estos valores hayan empeorado (se incluye una tolerancia para evitar cortar el entrenamiento por alguna oscilación propia del proceso de entrenamiento).
        if i % validation_frequency == 0:
            
            print(f"Epoch {i}: loss = {loss}, loss val = {lossval}, precision prueba= {precision_prueba}")
            # print(best_loss - loss)
           
            if lossval < best_loss:
                best_loss = lossval
                best_accuracy = precision_prueba
                patience = 0
            else:
                patience += 1
                print(f"patience-> {patience}")
                if patience > 2:
                    print(f"Early stopping (patience > 2) in epoch {i}")
                    break
            

 ##################################################################################Calculo de Precision#########################################################################################

        # Paso 4: Actualizar los pesos utilizando el algoritmo de backpropagation

        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = 2 * (p - t)  # Derivada del error cuadrático medio (MSE) respecto a la salida
        dL_dy /= m  # Dividir por el número de ejemplos de entrenamiento

        dL_dw2 = h.T.dot(dL_dy)  # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)  # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)

        dL_dz = dL_dh  # El cálculo dL/dz = dL/dh * dh/dz. La función "h" es la función de activación lineal de la capa oculta.

        dL_dw1 = x.T.dot(dL_dz)  # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)  # Ajuste para b1

        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2



    #graficamos loss, lossval y precision en una misma ventana
    plt.plot(lista_loss, label="loss")
    plt.plot(lista_lossval, label="lossval")
    plt.plot(lista_precision_prueba, label="precision")
    plt.legend()
    plt.show()



        #graficamos los datos


def iniciar(numero_clases, numero_ejemplos, graficar_datos):
    # Generamos datos
    x,t= gd.generar_datos_regresion(numero_ejemplos, (0,10))
    # print(x)
    # print("\n\n\n")
    # print(t)

    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        plt.scatter(x, t)
        plt.show()


    x_entrenamiento,t_entrenamiento, x_prueba,t_prueba = div.dividir_conjunto_de_datos(x,t, 0.7)

    # Graficamos los datos si es necesario
    
    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=numero_clases)

    # Entrena
    LEARNING_RATE = 0.1
    EPOCHS = 10000
    train(x_entrenamiento, t_entrenamiento, x_prueba, t_prueba, pesos, LEARNING_RATE, EPOCHS)

##################################################################################Calculo de Precision#########################################################################################

##################################################################################Calculo de Loss#########################################################################################
def calcular_loss(x, t, pesos):
#se calcula el loss mediante la funcion de MSE
    ejecucion = ejecutar_adelante(x, pesos)
    y_pred = ejecucion["y"]
    
    # Cálculo del error cuadrático medio (MSE)
    mse = np.mean((y_pred - t) ** 2)
    
    return ejecucion["z"], ejecucion["h"], ejecucion["y"], mse


iniciar(numero_clases=1, numero_ejemplos=300, graficar_datos=False)


#Preguntas para consulta>>>>>>>>> Como tratar los nuevos conjuntos de datos? x, x_prueba, x_validacion, x_entrenamiento, t_entrenamiento
#Preguntas para consulta>>>>>>>>> Es correcto el if que estoy usando como criterio de parada o como lo deberia escribir?