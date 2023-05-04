import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Se definen las variables lingüísticas de entrada
theta = ctrl.Antecedent(np.arange(-90, 91, 1), 'theta')
dtheta = ctrl.Antecedent(np.arange(-10, 11, 1), 'dtheta')

# Se definen las particiones borrosas para las variables de entrada
theta['NL'] = fuzz.trimf(theta.universe, [-90, -90, -45])
theta['NM'] = fuzz.trimf(theta.universe, [-90, -45, 0])
theta['NS'] = fuzz.trimf(theta.universe, [-45, 0, 45])
theta['ZR'] = fuzz.trimf(theta.universe, [-1, 0, 1])
theta['PS'] = fuzz.trimf(theta.universe, [0, 45, 90])
theta['PM'] = fuzz.trimf(theta.universe, [45, 90, 90])
theta['PL'] = fuzz.trimf(theta.universe, [90, 90, 135])

dtheta['NL'] = fuzz.trimf(dtheta.universe, [-10, -10, -5])
dtheta['NM'] = fuzz.trimf(dtheta.universe, [-10, -5, 0])
dtheta['NS'] = fuzz.trimf(dtheta.universe, [-5, 0, 5])
dtheta['ZR'] = fuzz.trimf(dtheta.universe, [-1, 0, 1])
dtheta['PS'] = fuzz.trimf(dtheta.universe, [0, 5, 10])
dtheta['PM'] = fuzz.trimf(dtheta.universe, [5, 10, 10])
dtheta['PL'] = fuzz.trimf(dtheta.universe, [10, 10, 15])

# Se define la variable lingüística de salida
force = ctrl.Consequent(np.arange(-10, 11, 1), 'force')

# Se definen las particiones borrosas para la variable de salida
force['NL'] = fuzz.trimf(force.universe, [-10, -10, -5])
force['NM'] = fuzz.trimf(force.universe, [-10, -5, 0])
force['NS'] = fuzz.trimf(force.universe, [-5, 0, 5])
force['ZR'] = fuzz.trimf(force.universe, [-1, 0, 1])
force['PS'] = fuzz.trimf(force.universe, [0, 5, 10])
force['PM'] = fuzz.trimf(force.universe, [5, 10, 10])

# Se definen las reglas de inferencia
rule1 = ctrl.Rule(theta['NL'] & dtheta['NL'], force['PM'])
rule2 = ctrl.Rule(theta['NL'] & dtheta['NS'], force['PS'])
rule3 = ctrl.Rule(theta['NL'] & dtheta['ZR'], force['ZR'])
rule4 = ctrl.Rule(theta['NL'] & dtheta['PS'], force['NS'])
rule5 = ctrl.Rule(theta['NL'] & dtheta['PM'], force['NM'])

rule6 = ctrl.Rule(theta['NM'] & dtheta['NL'], force['PM'])
rule7 = ctrl.Rule(theta['NM'] & dtheta['NS'], force['PS'])
rule8 = ctrl.Rule(theta['NM'] & dtheta['ZR'], force['ZR'])
rule9 = ctrl.Rule(theta['NM'] & dtheta['PS'], force['NS'])
rule10 = ctrl.Rule(theta['NM'] & dtheta['PM'], force['NM'])

rule11 = ctrl.Rule(theta['NS'] & dtheta['NL'], force['PS'])
rule12 = ctrl.Rule(theta['NS'] & dtheta['NS'], force['ZR'])
rule13 = ctrl.Rule(theta['NS'] & dtheta['ZR'], force['NS'])
rule14 = ctrl.Rule(theta['NS'] & dtheta['PS'], force['NM'])
rule15 = ctrl.Rule(theta['NS'] & dtheta['PM'], force['NM'])

rule16 = ctrl.Rule(theta['ZR'] & dtheta['NL'], force['NS'])
rule17 = ctrl.Rule(theta['ZR'] & dtheta['NS'], force['NS'])
rule18 = ctrl.Rule(theta['ZR'] & dtheta['ZR'], force['ZR'])
rule19 = ctrl.Rule(theta['ZR'] & dtheta['PS'], force['PM'])
rule20 = ctrl.Rule(theta['ZR'] & dtheta['PM'], force['PM'])

rule21 = ctrl.Rule(theta['PS'] & dtheta['NL'], force['NS'])
rule22 = ctrl.Rule(theta['PS'] & dtheta['NS'], force['NM'])
rule23 = ctrl.Rule(theta['PS'] & dtheta['ZR'], force['PM'])
rule24 = ctrl.Rule(theta['PS'] & dtheta['PS'], force['PM'])
rule25 = ctrl.Rule(theta['PS'] & dtheta['PM'], force['PS'])

rule26 = ctrl.Rule(theta['PM'] & dtheta['NL'], force['NM'])
rule27 = ctrl.Rule(theta['PM'] & dtheta['NS'], force['NM'])
rule28 = ctrl.Rule(theta['PM'] & dtheta['ZR'], force['PS'])
rule29 = ctrl.Rule(theta['PM'] & dtheta['PS'], force['PS'])
rule30 = ctrl.Rule(theta['PM'] & dtheta['PM'], force['NL'])

# Se crea el controlador difuso
force_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
     rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, 
     rule21, rule22, rule13, rule24, rule25, rule26, rule27, rule28, rule29, rule30])
simulation = ctrl.ControlSystemSimulation(force_ctrl)

# Simulación del sistema
def simular_fuzzy(t_max, delta_t, theta_0, dtheta_0):
    # Listas para almacenar los valores de salida
    t_data = []
    theta_data = []
    dtheta_data = []
    f_data = []

    # Condiciones iniciales
    theta = (theta_0 * np.pi) / 180
    dtheta = (dtheta_0 * np.pi) / 180

    # Realizar la simulación
    for t in np.arange(0, t_max, delta_t):
        # Asignar entradas a la simulación
        simulation.input['theta'] = theta
        simulation.input['dtheta'] = dtheta

        # Computar el resultado
        simulation.compute()

        # Obtenemos la fuerza calculada por el sistema difuso
        f = simulation.output['force']

        # Calculamos la aceleración a partir de la fuerza calculada
        numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-f - CONSTANTE_m * CONSTANTE_l * np.power(dtheta, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
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
    fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(12,8))

    ax1.plot(t_data, np.array(theta_data) * 180 / np.pi)
    ax1.set(ylabel='Ángulo (grados)')

    ax2.plot(t_data, np.array(dtheta_data) * 180 / np.pi)
    ax2.set(ylabel='Velocidad angular (grados/s)')

    ax3.plot(t_data, f_data)
    ax3.set(ylabel='Fuerza (N)', xlabel='Tiempo (s)')

    plt.show()

# Simular el sistema difuso
simular_fuzzy(10, 0.01, 45, 0)
