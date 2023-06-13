import numpy as np
import matplotlib.pyplot as plt
import Generadores_Datos as gd
import Divisores as div

def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):  
    randomgen = np.random.default_rng()
    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))
    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1, n_capa_3))
    y_precision = 0
    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos):
    z = x.dot(pesos["w1"]) + pesos["b1"]
    h = 1 / (1 + np.exp(-z)) 
    y = h.dot(pesos["w2"]) + pesos["b2"]

    return {"z": z, "h": h, "y": y}


def calcular_loss(x, t, pesos):
    ejecucion = ejecutar_adelante(x, pesos)
    y_pred = ejecucion["y"]
    mse = np.mean((y_pred - t) ** 2)
    return mse, ejecucion




def train(x, t, xtest, ttest, pesos, learning_rate, epochs):  
    m = x.shape[0]  
    lista_precision_prueba = []
    lista_loss = []
    lista_lossval = []
    best_loss = np.inf
    best_accuracy = 0
    patience = 0


    x2, t2, xval, tval = div.dividir_conjunto_de_datos(x, t, 0.8)

    for i in range(epochs):
        loss, resultados = calcular_loss(x, t, pesos)
        lista_loss.append(loss)
        lossval, _ = calcular_loss(xval, tval, pesos)
        lista_lossval.append(lossval)

        #print(f"Epoch {i}: loss = {loss}, loss val = {lossval}")

        h = resultados["h"]
        z = resultados["z"]
        y = resultados["y"]


        # e. calculo accuracy con datos de precision
        
        y_precision, h_precision, z_precision = ejecutar_adelante(xtest, pesos)
        ttest = np.array(ttest, dtype=np.float64)

        
        #accuracy
        precision_prueba = np.mean((y_precision - ttest) ** 2)

        #guardamos la precision prueba en una lista para graficarla
        lista_precision_prueba.append(precision_prueba)
        
        validation_frequency = 100

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


        # Cálculo de los gradientes
        dL_dy = 2 * (y - t) / m
        dy_dh = pesos["w2"]
        dh_dz = h * (1 - h)
        dz_dw1 = x

        dL_dw2 = np.dot(h.T, dL_dy)
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)
        dL_dh = np.dot(dL_dy, dy_dh.T)
        dL_dz = dL_dh * dh_dz

        dL_dw1 = np.dot(x.T, dL_dz)
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)

        # Actualización de los pesos
        pesos["w1"] -= learning_rate * dL_dw1
        pesos["b1"] -= learning_rate * dL_db1
        pesos["w2"] -= learning_rate * dL_dw2
        pesos["b2"] -= learning_rate * dL_db2

    # Graficar el error y la precision
    plt.plot(lista_precision_prueba, label="precision prueba")
    plt.plot(lista_loss, label="loss")
    plt.plot(lista_lossval, label="lossval")
    plt.legend()
    plt.show()

    return pesos


def iniciar( n_entrada, n_capa_2, n_capa_3, learning_rate, epochs):
    # Generar los datos
    x, t = gd.generar_datos_regresion(100, [-1, 1])
    xtest, ttest = gd.generar_datos_regresion(30,[-1, 1])
    t = t.reshape(-1, 1)
    ttest = ttest.reshape(-1, 1)

    #graficar los datos originales en 3 dimensiones
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[:, 0], x[:, 1], t, label="Datos")
    plt.legend()
    plt.show()


    # Inicializar los pesos
    pesos = inicializar_pesos(n_entrada, n_capa_2, n_capa_3)

    # Entrenar el modelo
    pesos = train(x, t, xtest, ttest, pesos, learning_rate, epochs)

    # Graficar los datos en 3 dimensiones junto con la salida de la red
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[:, 0], x[:, 1], t, label="Datos")
    ax.scatter(x[:, 0], x[:, 1], ejecutar_adelante(x, pesos)["y"], label="Predicción")
    plt.legend()
    plt.show()
    
    #plt.scatter(x[:, 0], t, label="Datos")
    #plt.scatter(x[:, 0], ejecutar_adelante(x, pesos)["y"], label="Predicción")
    #plt.legend()
    #plt.show()


    return pesos

NEURONAS_CAPA_OCULTA = 100
NEURONAS_ENTRADA = 2
LEARNING_RATE = 0.1
EPOCHS = 10000
iniciar( NEURONAS_ENTRADA, NEURONAS_CAPA_OCULTA, 1, LEARNING_RATE, EPOCHS)