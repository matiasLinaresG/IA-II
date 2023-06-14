import numpy as np

from MLP_REGRESION_V23 import iniciar 
from graficar import graficaresultado


#parámetros a barrer
#learning_rate
#epochs
#nro de neuronas en la capa oculta
#funcion de activacion (sigmoidal, relu)

#definimos los valores de los parámetros a barrer a aleatoriamente
learning_rate =[0.0001,0.2]
epochs = [100,10000]
neuronas = [20,200]

N=10

config = [(np.random.uniform(learning_rate[0], learning_rate[1]), np.random.randint(epochs[0], epochs[1]), np.random.randint(neuronas[0], neuronas[1])) for i in range(N)]


acuaraccy_sigmoid = np.zeros (N)
acuaraccy_relu = np.zeros (N)



for i in range(N):
    for j in range(10):
        acuaraccy_sigmoid[i] += iniciar(2,config[i][2],1,config[i][0],config[i][1], 'sigmoid')
        acuaraccy_relu[i] += iniciar(2,config[i][2],1,config[i][0],config[i][1], 'relu')
        print("Configuracion: ", i, "iter: ", j, "acuaraccy_sigmoid: ", acuaraccy_sigmoid[i]/(j+1))
        print("Configuracion: ", i, "iter: ", j, "acuaraccy_relu: ", acuaraccy_relu[i]/(j+1))
    acuaraccy_sigmoid[i] = acuaraccy_sigmoid[i]/N
    acuaraccy_relu[i] = acuaraccy_relu[i]/N
    print("=======================================")


#graficar acuaraccy 
graficaresultado(acuaraccy_sigmoid, config, ['learning_rate', 'epochs','neuronas'])
graficaresultado(acuaraccy_relu, config, ['learning_rate', 'epochs','neuronas'])

