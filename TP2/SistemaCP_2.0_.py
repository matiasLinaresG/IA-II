import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Se definen las variables lingüísticas de entrada
theta = ctrl.Antecedent(np.arange(-90, 91, 1), 'theta') # Angulo de la pertiga con respecto a la vertical
dtheta = ctrl.Antecedent(np.arange(-10, 11, 1), 'dtheta') # Velocidad angular de la pertiga

# Se definen las particiones borrosas para las variables de entrada
theta['NL'] = fuzz.trimf(theta.universe, [-90, -90, -45]) # NL: Negative Large
theta['NM'] = fuzz.trimf(theta.universe, [-90, -45, 0]) # NM: Negative Medium
theta['NS'] = fuzz.trimf(theta.universe, [-45, 0, 45]) # NS: Negative Small
theta['ZR'] = fuzz.trimf(theta.universe, [-1, 0, 1]) # ZR: Zero
theta['PS'] = fuzz.trimf(theta.universe, [0, 45, 90]) # PS: Positive Small
theta['PM'] = fuzz.trimf(theta.universe, [45, 90, 90]) # PM: Positive Medium
theta['PL'] = fuzz.trimf(theta.universe, [90, 90, 135]) # PL: Positive Large

dtheta['NL'] = fuzz.trimf(dtheta.universe, [-10, -10, -5]) # NL: Negative Large
dtheta['NM'] = fuzz.trimf(dtheta.universe, [-10, -5, 0]) # NM: Negative Medium
dtheta['NS'] = fuzz.trimf(dtheta.universe, [-5, 0, 5]) # NS: Negative Small
dtheta['ZR'] = fuzz.trimf(dtheta.universe, [-1, 0, 1]) # ZR: Zero
dtheta['PS'] = fuzz.trimf(dtheta.universe, [0, 5, 10]) # PS: Positive Small
dtheta['PM'] = fuzz.trimf(dtheta.universe, [5, 10, 10]) # PM: Positive Medium
dtheta['PL'] = fuzz.trimf(dtheta.universe, [10, 10, 15]) # PL: Positive Large

# Se define la variable lingüística de salida
force = ctrl.Consequent(np.arange(-10, 11, 1), 'force') # Fuerza aplicada al carro para contrarrestar el movimiento de la pertiga, ctrl.Consequent(universe, label) hace que universe sea el rango de valores de la variable de salida y label sea el nombre de la variable de salida

# Se definen las particiones borrosas para la variable de salida
force['NL'] = fuzz.trimf(force.universe, [-10, -10, -5]) # NL: Negative Large
force['NM'] = fuzz.trimf(force.universe, [-10, -5, 0]) # NM: Negative Medium
force['NS'] = fuzz.trimf(force.universe, [-5, 0, 5]) # NS: Negative Small
force['ZR'] = fuzz.trimf(force.universe, [-1, 0, 1]) # ZR: Zero
force['PS'] = fuzz.trimf(force.universe, [0, 5, 10]) # PS: Positive Small
force['PM'] = fuzz.trimf(force.universe, [5, 10, 10]) # PM: Positive Medium

# Se definen las reglas de inferencia
rule1 = ctrl.Rule(theta['NL'] & dtheta['NL'], force['PM']) # Regla 1: Si theta es NL y dtheta es NL, entonces force es PM
rule2 = ctrl.Rule(theta['NL'] & dtheta['NS'], force['PS']) # Regla 2: Si theta es NL y dtheta es NS, entonces force es PS
rule3 = ctrl.Rule(theta['NL'] & dtheta['ZR'], force['ZR']) # Regla 3: Si theta es NL y dtheta es ZR, entonces force es ZR
rule4 = ctrl.Rule(theta['NL'] & dtheta['PS'], force['NS']) # Regla 4: Si theta es NL y dtheta es PS, entonces force es NS
rule5 = ctrl.Rule(theta['NL'] & dtheta['PM'], force['NM']) # Regla 5: Si theta es NL y dtheta es PM, entonces force es NM

rule6 = ctrl.Rule(theta['NM'] & dtheta['NL'], force['PM']) # Regla 6: Si theta es NM y dtheta es NL, entonces force es PM
rule7 = ctrl.Rule(theta['NM'] & dtheta['NS'], force['PS']) # Regla 7: Si theta es NM y dtheta es NS, entonces force es PS
rule8 = ctrl.Rule(theta['NM'] & dtheta['ZR'], force['ZR']) # Regla 8: Si theta es NM y dtheta es ZR, entonces force es ZR
rule9 = ctrl.Rule(theta['NM'] & dtheta['PS'], force['NS']) # Regla 9: Si theta es NM y dtheta es PS, entonces force es NS
rule10 = ctrl.Rule(theta['NM'] & dtheta['PM'], force['NM']) # Regla 10: Si theta es NM y dtheta es PM, entonces force es NM

rule11 = ctrl.Rule(theta['NS'] & dtheta['NL'], force['PS']) # Regla 11: Si theta es NS y dtheta es NL, entonces force es PS
rule12 = ctrl.Rule(theta['NS'] & dtheta['NS'], force['ZR']) # Regla 12: Si theta es NS y dtheta es NS, entonces force es ZR
rule13 = ctrl.Rule(theta['NS'] & dtheta['ZR'], force['NS']) # Regla 13: Si theta es NS y dtheta es ZR, entonces force es NS
rule14 = ctrl.Rule(theta['NS'] & dtheta['PS'], force['NM']) # Regla 14: Si theta es NS y dtheta es PS, entonces force es NM
rule15 = ctrl.Rule(theta['NS'] & dtheta['PM'], force['NM']) # Regla 15: Si theta es NS y dtheta es PM, entonces force es NM

rule16 = ctrl.Rule(theta['ZR'] & dtheta['NL'], force['NS']) # Regla 16: Si theta es ZR y dtheta es NL, entonces force es NS
rule17 = ctrl.Rule(theta['ZR'] & dtheta['NS'], force['NS']) # Regla 17: Si theta es ZR y dtheta es NS, entonces force es NS
rule18 = ctrl.Rule(theta['ZR'] & dtheta['ZR'], force['ZR']) # Regla 18: Si theta es ZR y dtheta es ZR, entonces force es ZR
rule19 = ctrl.Rule(theta['ZR'] & dtheta['PS'], force['PM']) # Regla 19: Si theta es ZR y dtheta es PS, entonces force es PM
rule20 = ctrl.Rule(theta['ZR'] & dtheta['PM'], force['PM']) # Regla 20: Si theta es ZR y dtheta es PM, entonces force es PM

rule21 = ctrl.Rule(theta['PS'] & dtheta['NL'], force['NS']) # Regla 21: Si theta es PS y dtheta es NL, entonces force es NS
rule22 = ctrl.Rule(theta['PS'] & dtheta['NS'], force['NM']) # Regla 22: Si theta es PS y dtheta es NS, entonces force es NM
rule23 = ctrl.Rule(theta['PS'] & dtheta['ZR'], force['PM']) # Regla 23: Si theta es PS y dtheta es ZR, entonces force es PM
rule24 = ctrl.Rule(theta['PS'] & dtheta['PS'], force['PM']) # Regla 24: Si theta es PS y dtheta es PS, entonces force es PM
rule25 = ctrl.Rule(theta['PS'] & dtheta['PM'], force['PS']) # Regla 25: Si theta es PS y dtheta es PM, entonces force es PS

rule26 = ctrl.Rule(theta['PM'] & dtheta['NL'], force['NM']) # Regla 26: Si theta es PM y dtheta es NL, entonces force es NM
rule27 = ctrl.Rule(theta['PM'] & dtheta['NS'], force['NM']) # Regla 27: Si theta es PM y dtheta es NS, entonces force es NM
rule28 = ctrl.Rule(theta['PM'] & dtheta['ZR'], force['PS']) # Regla 28: Si theta es PM y dtheta es ZR, entonces force es PS
rule29 = ctrl.Rule(theta['PM'] & dtheta['PS'], force['PS']) # Regla 29: Si theta es PM y dtheta es PS, entonces force es PS
rule30 = ctrl.Rule(theta['PM'] & dtheta['PM'], force['NL']) # Regla 30: Si theta es PM y dtheta es PM, entonces force es NL
#creamos tabla de reglas de inferencia para mostrarlas en pantalla mediante un dataframe,se imprime la tabla de reglas
reglas = pd.DataFrame({'Regla': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
                        'Antecedentes': ['NL & NL', 'NL & NM', 'NL & NS', 'NL & PS', 'NL & PM',
                                            'NM & NL', 'NM & NS', 'NM & ZR', 'NM & PS', 'NM & PM',
                                            'NS & NL', 'NS & NS', 'NS & ZR', 'NS & PS', 'NS & PM',
                                            'ZR & NL', 'ZR & NS', 'ZR & ZR', 'ZR & PS', 'ZR & PM',
                                            'PS & NL', 'PS & NS', 'PS & ZR', 'PS & PS', 'PS & PM',
                                            'PM & NL', 'PM & NS', 'PM & ZR', 'PM & PS', 'PM & PM'],
                        'Consecuente': ['NL', 'NL', 'NS', 'NS', 'NM',
                                        'NL', 'NS', 'ZR', 'NM', 'NM',
                                        'NS', 'NM', 'NS', 'NM', 'NM',
                                        'NS', 'NS', 'ZR', 'PM', 'PM',
                                        'NS', 'NM', 'PM', 'PM', 'PS',
                                        'NM', 'NM', 'PS', 'PS', 'NL']})
print(reglas)


# Se crea el controlador difuso
force_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
     rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, 
     rule21, rule22, rule13, rule24, rule25, rule26, rule27, rule28, rule29, rule30])
simulation = ctrl.ControlSystemSimulation(force_ctrl)
# Se crea la simulación del controlador difuso con el controlador difuso creado, ctrol.ControlSystemSimulation(controlador_difuso) trabaja de la siguiente manerea:
# 1. Se asignan las entradas a la simulación con la función simulation.input['nombre_entrada'] = valor_entrada
# 2. Se computa el resultado con la función simulation.compute()
# 3. Se obtiene el valor de salida con la función simulation.output['nombre_salida']


# Simulación del sistema
def simular_fuzzy(t_max, delta_t, theta_0, dtheta_0): # Función para simular el sistema difuso con las entradas theta_0 y dtheta_0 en el tiempo t_max con un delta_t
    # Listas para almacenar los valores de salida
    t_data = []
    theta_data = []
    dtheta_data = []
    f_data = []

    # Condiciones iniciales
    theta = (theta_0 * np.pi) / 180
    dtheta = (dtheta_0 * np.pi) / 180

    # Realizar la simulación
    for t in np.arange(0, t_max, delta_t): # Para cada instante de tiempo
        # Asignar entradas a la simulación
        simulation.input['theta'] = theta
        simulation.input['dtheta'] = dtheta

        # Computar el resultado
        simulation.compute()

        # Obtenemos la fuerza calculada por el sistema difuso
        f = simulation.output['force']

        # Calculamos la aceleración a partir de la fuerza calculada
        numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(dtheta, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m)) # Aceleración angular del péndulo invertido (ecuación de Euler-Lagrange)
        denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
        ddtheta = numerador / denominador

        # Integramos la aceleración para obtener la velocidad y el ángulo en el siguiente instante de tiempo
        theta = theta + dtheta * delta_t
        dtheta = dtheta + ddtheta * delta_t

        # Almacenamos los datos de la simulación
        t_data.append(t)
        theta_data.append(theta)
        dtheta_data.append(dtheta)
        f_data.append(f)

    # Graficamos los resultados
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

    ax1.plot(t_data, np.array(theta_data) * 180 / np.pi)
    ax1.set(ylabel='Ángulo (grados)')

    ax2.plot(t_data, np.array(dtheta_data) * 180 / np.pi)
    ax2.set(ylabel='Velocidad angular (grados/s)')

    ax3.plot(t_data, f_data)
    ax3.set(ylabel='Fuerza (N)', xlabel='Tiempo (s)')


    plt.show()

# Simular el sistema difuso
simular_fuzzy(10, 0.01, 45, 0)




