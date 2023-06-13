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
    return ejecucion["z"], ejecucion["h"], ejecucion["y"], mse

def train(x, t, xtest, ttest, pesos, learning_rate, epochs):
    numero_ejemplos = x.shape[0]
    best_loss = float("inf")
    best_accuracy = 0
    patience = 0
    validation_frequency=100

    for i in range(epochs):
        y,h,z,loss =  calcular_loss(x, t, pesos)

        if i % validation_frequency == 0:
            _,_, _, lossval = calcular_loss(xtest, ttest, pesos)

            if lossval < best_loss:
                best_loss = lossval
                patience = 0
            else:
                patience += 1
                if patience > 2:
                    print(f"Early stopping (patience > 2) in epoch {i}")
                    break

        dL_dy = 2*(y - t) / numero_ejemplos
        dy_dw2 = h
        dL_dw2 = np.dot(dy_dw2.T, dL_dy)
        dy_db2 = 1
        dL_db2 = np.sum(dL_dy * dy_db2, axis=0, keepdims=True)

        dh_dz = h * (1 - h)
        dz_dw1 = x
        dL_dz = np.dot(dL_dy, pesos["w2"])
        dL_dw1 = np.dot(dz_dw1.T, dh_dz * dL_dz)
        dz_db1 = 1
        dL_db1 = np.sum(dL_dz * dh_dz * dz_db1, axis=0, keepdims=True)

        pesos["w1"] += -learning_rate * dL_dw1
        pesos["b1"] += -learning_rate * dL_db1
        pesos["w2"] += -learning_rate * dL_dw2
        pesos["b2"] += -learning_rate * dL_db2

    print(f"Training finished in epoch {i}, with loss {best_loss}")

    return pesos

def iniciar(n_entrada, n_capa_2, n_capa_3):
    x, t = gd.generar_datos_regresion(500, [-1,1])  # conjunto de entrenamiento
    xtest, ttest = gd.generar_datos_regresion(100, [-1,1])  # conjunto de test

    pesos = inicializar_pesos(n_entrada, n_capa_2, n_capa_3)

    pesos = train(x, t, xtest, ttest, pesos, 0.01, 5000)

    _, _, y, loss = calcular_loss(x, t, pesos)
    print(f"Training loss: {loss}")
    _, _, ytest, losstest = calcular_loss(xtest, ttest, pesos)
    print(f"Test loss: {losstest}")

iniciar(2,100,1)