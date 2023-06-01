import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from scipy import constants

# Definir las variables de entrada y salida
angulo = ctrl.Antecedent(np.arange(-90, 90, 1), 'angulo')
velocidad = ctrl.Antecedent(np.arange(-10, 10, 0.1), 'velocidad')
fuerza = ctrl.Consequent(np.arange(-10, 10, 0.1), 'fuerza')

# Definir los conjuntos difusos para cada variable
angulo['negativo'] = fuzz.trimf(angulo.universe, [-180, -90, 0])
angulo['cero'] = fuzz.trimf(angulo.universe, [-90, 0, 90])
angulo['positivo'] = fuzz.trimf(angulo.universe, [0, 90, 180])

velocidad['negativa'] = fuzz.trimf(velocidad.universe, [-10, -5, 0])
velocidad['cero'] = fuzz.trimf(velocidad.universe, [-5, 0, 5])
velocidad['positiva'] = fuzz.trimf(velocidad.universe, [0, 5, 10])

fuerza['negativa'] = fuzz.trimf(fuerza.universe, [-10, -5, 0])
fuerza['cero'] = fuzz.trimf(fuerza.universe, [-5, 0, 5])
fuerza['positiva'] = fuzz.trimf(fuerza.universe, [0, 5, 10])

# Definir las reglas de inferencia
regla1 = ctrl.Rule(angulo['negativo'] & velocidad['positiva'], fuerza['negativa'])
regla2 = ctrl.Rule(angulo['negativo'] & velocidad['cero'], fuerza['cero'])
regla3 = ctrl.Rule(angulo['negativo'] & velocidad['negativa'], fuerza['positiva'])
regla4 = ctrl.Rule(angulo['cero'] & velocidad['positiva'], fuerza['negativa'])
regla5 = ctrl.Rule(angulo['cero'] & velocidad['cero'], fuerza['cero'])
regla6 = ctrl.Rule(angulo['cero'] & velocidad['negativa'], fuerza['positiva'])
regla7 = ctrl.Rule(angulo['positivo'] & velocidad['positiva'], fuerza['negativa'])
regla8 = ctrl.Rule(angulo['positivo'] & velocidad['cero'], fuerza['cero'])
regla9 = ctrl.Rule(angulo['positivo'] & velocidad['negativa'], fuerza['positiva'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9])
controlador = ctrl.ControlSystemSimulation(sistema_control)

# Función para obtener la fuerza de salida
def obtener_fuerza(angulo_actual, velocidad_actual):
    controlador.input['angulo'] = angulo_actual
    controlador.input['velocidad'] = velocidad_actual
    controlador.compute()
    return controlador.output['fuerza']

# Implementación del Modelo Carro - Proporcionado

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Simula el modelo del carro-pendulo.
# Parametros:
#   t_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   theta_0: Angulo inicial (grados)
#   v_0: Velocidad angular inicial (radianes/s)
#   a_0: Aceleracion angular inicial (radianes/s2)

def simular(t_max, delta_t, theta_0, v_0, a_0):
  theta = (theta_0 * np.pi) / 180
  v = v_0
  a = a_0

  # Simular
  y = []
  x = np.arange(0, t_max, delta_t)
  F=[]
  V=[]
  for t in x:
    f = obtener_fuerza(theta, v)  # Obtenemos la fuerza del controlador difuso
    F.append(f)
    a = calcula_aceleracion(theta, v, f)
    v = v + a * delta_t
    V.append(v)
    theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
    y.append(theta)

  fig, ax = plt.subplots()
  ax.plot(x, y)

  ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
  ax.grid()
  
  plt.show()

  fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
  fig.suptitle('Delta t = ' + str(delta_t) + " s")

  ax1.plot(x, y)
  ax1.set(xlabel='time (s)', ylabel='theta')
  ax1.grid()

  ax2.plot(x, V)
  ax2.set(xlabel='time (s)', ylabel='V')
  ax2.grid()

  ax3.plot(x, F)
  ax3.set(xlabel='time (s)', ylabel='F')
  ax3.grid()
  plt.show()

# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v, f):
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador

simular(50, 0.001, 180, 6, 0)
