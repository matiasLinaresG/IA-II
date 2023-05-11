
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir las variables lingüísticas de entrada y salida
#np.arange(start, stop, step) # Genera un arreglo de números desde start hasta stop con incrementos de step

posicion = np.arange(-10, 11, 1) # Posición del carro (-10 a 10) en cmasd
velocidad = np.arange(-10, 11, 1) # Velocidad del carro (-10 a 10) en cm/s
fuerza = np.arange(-100, 101, 1) # Fuerza ejercida sobre el carro (-100 a 100) en N

# Definir las particiones borrosas de las variables de entrada considerando 5 conjuntos difusos para posicion y 5 para velocidad
#fuzz.trimf(x, [a, b, c]) # Función de membresía triangular con a, b y c como los puntos de inflexión izquierdo, medio y derecho respectivamente

posicion_izqmayor = fuzz.trimf(posicion, [-10, -10, -5]) #  [-10, -10, -5] es el rango de la función de membresía izquierdamayor
posicion_izq = fuzz.trimf(posicion, [-10, -5, -0]) #  [-7.5, -5, -2.5] es el rango de la función de membresía izquierda
posicion_cen = fuzz.trimf(posicion, [-5, 0, 5]) #  [-2.5, 0, 2.5] es el rango de la función de membresía central
posicion_der = fuzz.trimf(posicion, [0 ,5, 10]) #  [2.5, 5, 7.5] es el rango de la función de membresía derecha
posicion_dermayor = fuzz.trimf(posicion, [5, 10, 10]) #  [5, 10, 10] es el rango de la función de membresía derechamayor


velocidad_neg_grande = fuzz.trimf(velocidad, [-10, -10, -5]) #  [-10, -10, -5] es el rango de la función de membresía negativa grande
velocidad_neg_peque = fuzz.trimf(velocidad, [-10, -5, 0]) #  [-7.5, -2.5, 0] es el rango de la función de membresía negativa pequeña
velocidad_cero = fuzz.trimf(velocidad, [-5, 0, 5]) #  [-2.5, 0, 2.5] es el rango de la función de membresía cero
velocidad_pos_peque = fuzz.trimf(velocidad, [0, 5, 10]) #  [0, 2.5, 7.5] es el rango de la función de membresía positiva pequeña
velocidad_pos_grande = fuzz.trimf(velocidad, [5, 10, 10]) #  [5, 10, 10] es el rango de la función de membresía positiva grande


# Definir las particiones borrosas de la variable de salida
fuerza_neg_grande = fuzz.trimf(fuerza, [-100, -100, -50]) #  [-100, -100, -50] es el rango de la función de membresía negativa grande
fuerza_neg_peque = fuzz.trimf(fuerza, [-75, -50, 0]) #  [-75, -50, 0] es el rango de la función de membresía negativa pequeña
fuerza_cero = fuzz.trimf(fuerza, [-25, 0, 25] ) #  [-25, 0, 25] es el rango de la función de membresía cero
fuerza_pos_peque = fuzz.trimf(fuerza, [0, 50, 75]) #  [0, 50, 75] es el rango de la función de membresía positiva pequeña
fuerza_pos_grande = fuzz.trimf(fuerza, [50, 100, 100]) #  [50, 100, 100] es el rango de la función de membresía positiva grande

# Visualizar las particiones borrosas de las variables de entrada y salida



fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9)) # Crear una figura con 3 subfiguras (3 filas y 1 columna) y un tamaño de 8x9 pulgadas

ax0.plot(posicion, posicion_izq, 'b', linewidth=1.5, label='Izquierda')
ax0.plot(posicion, posicion_cen, 'g', linewidth=1.5, label='Centro')
ax0.plot(posicion, posicion_der, 'r', linewidth=1.5, label='Derecha')
ax0.plot(posicion, posicion_dermayor, 'c', linewidth=1.5, label='Derecha Mayor')
ax0.plot(posicion, posicion_izqmayor, 'm', linewidth=1.5, label='Izquierda Mayor')

ax0.set_title('Posición')
ax0.legend()

ax1.plot(velocidad, velocidad_neg_grande, 'b', linewidth=1.5, label='Negativa Grande')
ax1.plot(velocidad, velocidad_neg_peque, 'g', linewidth=1.5, label='Negativa Pequeña')
ax1.plot(velocidad, velocidad_cero, 'r', linewidth=1.5, label='Cero')
ax1.plot(velocidad, velocidad_pos_peque, 'c', linewidth=1.5, label='Positiva Pequeña')
ax1.plot(velocidad, velocidad_pos_grande, 'm', linewidth=1.5, label='Positiva Grande')

ax1.set_title('Velocidad')
ax1.legend()

ax2.plot(fuerza, fuerza_neg_grande, 'b', linewidth=1.5, label='Negativa Grande')
ax2.plot(fuerza,fuerza_neg_peque, 'g', linewidth=1.5, label='Negativa Pequeña')
ax2.plot(fuerza, fuerza_cero, 'r', linewidth=1.5, label='Cero')
ax2.plot(fuerza, fuerza_pos_peque, 'c', linewidth=1.5, label='Positiva Pequeña')
ax2.plot(fuerza, fuerza_pos_grande, 'm', linewidth=1.5, label='Positiva Grande')
ax2.set_title('Fuerza')
ax2.legend()

plt.tight_layout()
plt.show()

# Definir las reglas de inferencia difusa
# fuzz.relation_min() es la función que se utiliza para definir las reglas de inferencia difusa
# fuzz.relation_min() toma dos argumentos: el primer argumento es la función de membresía de la variable de entrada y el segundo argumento es la función de membresía de la variable de salida

# agregar consecuente ---> usar lo del Maxi en su otra rama
# recordar aplicar la regla de disyuncion ---> corregir luego de lo del maxi
# aplicar las funciones de el otro codigo y agregar importando penduloinvertido
# estandar pep8, usarlo para el codigo



# reglas de inferencia difusa para la posición izquierda mayor
regla1 = fuzz.relation_min(posicion_izqmayor, velocidad_neg_grande)
regla2 = fuzz.relation_min(posicion_izqmayor, velocidad_neg_peque)
regla3 = fuzz.relation_min(posicion_izqmayor, velocidad_cero)
regla4 = fuzz.relation_min(posicion_izqmayor, velocidad_pos_peque)
regla5 = fuzz.relation_min(posicion_izqmayor, velocidad_pos_grande)

# reglas de inferencia difusa para la posición derecha mayor
regla6 = fuzz.relation_min(posicion_dermayor, velocidad_neg_grande)
regla7 = fuzz.relation_min(posicion_dermayor, velocidad_neg_peque)
regla8 = fuzz.relation_min(posicion_dermayor, velocidad_cero)
regla9 = fuzz.relation_min(posicion_dermayor, velocidad_pos_peque)
regla10 = fuzz.relation_min(posicion_dermayor, velocidad_pos_grande)

# reglas de inferencia difusa para la posición derecha
regla11 = fuzz.relation_min(posicion_der, velocidad_neg_grande)
regla12 = fuzz.relation_min(posicion_der, velocidad_neg_peque)
regla13 = fuzz.relation_min(posicion_der, velocidad_cero)
regla14 = fuzz.relation_min(posicion_der, velocidad_pos_peque)
regla15 = fuzz.relation_min(posicion_der, velocidad_pos_grande)

# reglas de inferencia difusa para la posición centro
regla16 = fuzz.relation_min(posicion_cen, velocidad_neg_grande)
regla17 = fuzz.relation_min(posicion_cen, velocidad_neg_peque)
regla18 = fuzz.relation_min(posicion_cen, velocidad_cero)
regla19 = fuzz.relation_min(posicion_cen, velocidad_pos_peque)
regla20 = fuzz.relation_min(posicion_cen, velocidad_pos_grande)

#reglas de inferencia difusa para la posición izquierda
regla21 = fuzz.relation_min(posicion_izq, velocidad_neg_grande)
regla22 = fuzz.relation_min(posicion_izq, velocidad_neg_peque)
regla23 = fuzz.relation_min(posicion_izq, velocidad_cero)
regla24 = fuzz.relation_min(posicion_izq, velocidad_pos_peque)
regla25 = fuzz.relation_min(posicion_izq, velocidad_pos_grande)



#Definir las operaciones borrosas de conjunción, disyunción e implicación
conjuncion = np.fmin
disyuncion = np.fmax
implicacion = fuzz.defuzzify.centroid

#Definir la función para evaluar las reglas y obtener la salida borrosa
def evaluar_reglas(posicion, velocidad):
    grado_activacion = []
    for regla in [regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13, regla14, regla15, regla16, regla17, regla18, regla19, regla20, regla21, regla22, regla23, regla24, regla25 ]:
        grado_activacion.append(conjuncion(fuzz.interp_membership(posicion, regla.antecedent[0]), fuzz.interp_membership(velocidad, regla.antecedent[1])))
    return disyuncion(*grado_activacion)

#Definir la función para obtener la salida concreta
def obtener_salida(posicion, velocidad):
    salida_borrosa = evaluar_reglas(posicion, velocidad)
    return implicacion(fuerza, salida_borrosa)

#Definir las operaciones borrosas de conjunción, disyunción e implicación
conjuncion = np.fmin
disyuncion = np.fmax
implicacion = fuzz.defuzzify.centroid

#realizamos un caso de prueba

posicion = 0.5
velocidad = 0.5

salida = obtener_salida(posicion, velocidad)
print('La salida es: ', salida)



