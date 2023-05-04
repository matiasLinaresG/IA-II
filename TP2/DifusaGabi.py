
import numpy as np
import skfuzzy as fuzz

# Definir las variables lingüísticas de entrada y salida
posicion = np.arange(-10, 11, 1)
velocidad = np.arange(-10, 11, 1)
fuerza = np.arange(-100, 101, 1)

# Definir las particiones borrosas de las variables de entrada
posicion_izq = fuzz.trimf(posicion, [-10, -10, 0])
posicion_cen = fuzz.trimf(posicion, [-10, 0, 10])
posicion_der = fuzz.trimf(posicion, [0, 10, 10])
velocidad_neg = fuzz.trimf(velocidad, [-10, -10, 0])
velocidad_cer = fuzz.trimf(velocidad, [-10, 0, 10])
velocidad_pos = fuzz.trimf(velocidad, [0, 10, 10])

# Definir las particiones borrosas de la variable de salida
fuerza_neg_grande = fuzz.trimf(fuerza, [-100, -100, -50])
fuerza_neg_peque = fuzz.trimf(fuerza, [-75, -50, 0])
fuerza_cero = fuzz.trimf(fuerza, [-25, 0, 25])
fuerza_pos_peque = fuzz.trimf(fuerza, [0, 50, 75])
fuerza_pos_grande = fuzz.trimf(fuerza, [50, 100, 100])

# Visualizar las particiones borrosas de las variables de entrada y salida
import matplotlib.pyplot as plt

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(posicion, posicion_izq, 'b', linewidth=1.5, label='Izquierda')
ax0.plot(posicion, posicion_cen, 'g', linewidth=1.5, label='Centro')
ax0.plot(posicion, posicion_der, 'r', linewidth=1.5, label='Derecha')
ax0.set_title('Posición')
ax0.legend()

ax1.plot(velocidad, velocidad_neg, 'b', linewidth=1.5, label='Negativa')
ax1.plot(velocidad, velocidad_cer, 'g', linewidth=1.5, label='Cero')
ax1.plot(velocidad, velocidad_pos, 'r', linewidth=1.5, label='Positiva')
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

#Definir las reglas de inferencia difusa


regla1 = fuzz.relation_min(posicion_izq, velocidad_neg)
regla2 = fuzz.relation_min(posicion_izq, velocidad_cer)
regla3 = fuzz.relation_min(posicion_izq, velocidad_pos)
regla4 = fuzz.relation_min(posicion_cen, velocidad_neg)
regla5 = fuzz.relation_min(posicion_cen, velocidad_cer)
regla6 = fuzz.relation_min(posicion_cen, velocidad_pos)
regla7 = fuzz.relation_min(posicion_der, velocidad_neg)
regla8 = fuzz.relation_min(posicion_der, velocidad_cer)
regla9 = fuzz.relation_min(posicion_der, velocidad_pos)

#Definir las operaciones borrosas de conjunción, disyunción e implicación
conjuncion = np.fmin
disyuncion = np.fmax
implicacion = fuzz.defuzzify.centroid

#Definir la función para evaluar las reglas y obtener la salida borrosa
def evaluar_reglas(posicion, velocidad):
    grado_activacion = []
    for regla in [regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9]:
        grado_activacion.append(conjuncion(fuzz.interp_membership(posicion, regla.antecedent[0]), fuzz.interp_membership(velocidad, regla.antecedent[1])))
    return disyuncion(*grado_activacion)

#Definir la función para obtener la salida concreta
def obtener_salida(posicion, velocidad):
    salida_borrosa = evaluar_reglas(posicion, velocidad)
    return implicacion(fuerza, salida_borrosa)regla1 = fuzz.relation_min(posicion_izq, velocidad_neg)

#Definir las operaciones borrosas de conjunción, disyunción e implicación
conjuncion = np.fmin
disyuncion = np.fmax
implicacion = fuzz.defuzzify.centroid

#Definir la función para evaluar las reglas y obtener la salida borrosa
def evaluar_reglas(posicion, velocidad):
    grado_activacion = []
    for regla in [regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9]:
        grado_activacion.append(conjuncion(fuzz.interp_membership(posicion, regla.antecedent[0]), fuzz.interp_membership(velocidad, regla.antecedent[1])))
    return disyuncion(*grado_activacion)

#Definir la función para obtener la salida concreta
def obtener_salida(posicion, velocidad):
    salida_borrosa = evaluar_reglas(posicion, velocidad)
    return implicacion(fuerza, salida_borrosa)