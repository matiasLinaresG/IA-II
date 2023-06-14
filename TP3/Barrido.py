import numpy as np

from MLP_REGRESION_V2 import inicar 
from graficar import graficaresultado

#parámetros a barrer
#learning_rate
#epochs
#nro de neuronas en la capa oculta
#funcion de activacion (sigmoidal, relu)

#definimos los valores de los parámetros a barrer a aleatoriamente
learning_rate =[0.0001,0.1]
epochs = [100,1000]
neuronas = [1,100]

N=50

config = [(np.random.uniform(learning_rate[0], learning_rate[1]), np.random.uniform(epochs[0], epochs[1]), np.random.uniform(neuronas[0], neuronas[1])) for i in range(N)]


acuaraccy_sigmoid = np.zeros ((10,10,10))
acuaraccy_relu = np.zeros ((10,10,10))

for i in range(N):
    for j in range(10):
        acuaraccy_sigmoid[i] += funcion(config, 'sigmoidal')
        acuaraccy_relu[i] += funcion(config, 'relu')


#graficar acuaraccy 
graficaresultado(acuaraccy_sigmoid, config, ['learning_rate', 'epochs','neuronas'])
graficaresultado(acuaraccy_relu, config, ['learning_rate', 'epochs','neuronas'])

