import numpy as np
import matplotlib.pyplot as plt

CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

def calcula_F(theta, v):
    numerador=-9.8*np.sin(theta)*(CONSTANTE_M+CONSTANTE_m)
    denominador=np.cos(theta)
    return (numerador / denominador)-CONSTANTE_m*CONSTANTE_l*np.power(v,2)*np.sin(theta)

#graficar en 3d F para theta entre -pi/8 y pi/8 y v entre -5 y 5
Theta_limite = [-np.pi/8, np.pi/8]
V_limite = [-8, 8]

theta = np.linspace(Theta_limite[0], Theta_limite[1], 1000)
v = np.linspace( V_limite[0], V_limite[1], 1000)

theta, v = np.meshgrid(theta, v)
F = calcula_F(theta, v)
print(F)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(theta, v, F, 50, cmap='binary')
ax.set_xlabel('theta')
ax.set_ylabel('v')
ax.set_zlabel('F')
ax.set_title('F(theta, v)')
plt.show()

#definir los centros de las particiones de theta y v 

L0_T = (Theta_limite[1]-Theta_limite[0])/4
centros_T=[Theta_limite[0],Theta_limite[0]+L0_T, Theta_limite[0]+2*L0_T, Theta_limite[1]-L0_T, Theta_limite[1]]

L0_V = (V_limite[1]-V_limite[0])/4
centros_V=[V_limite[0],V_limite[0]+L0_V, V_limite[0]+2*L0_V, V_limite[1]-L0_V, V_limite[1]]

#definir el valor de F para las 25 convinaciones de centros de particiones de theta y v

F_centros = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        F_centros[i,j]=calcula_F(centros_T[i],centros_V[j])

#clasificar en 5 grupos los valores de F segun NG,NP, ZP, ZG, PG y definir F_clasificado
F_max = np.max(F_centros)
F_min = np.min(F_centros)
F_rango = F_max - F_min
L0_F = F_rango/5
limites_F = [F_min, F_min+L0_F, F_min+2*L0_F, F_min+3*L0_F, F_min+4*L0_F, F_max]
etiquetas = ["NG", "NP", "Z", "PP", "PG"]

#definir F_clasificado como una matriz de 5x5 de cadenas de caracteres
F_clasificado = np.empty((5,5), dtype='U2')


for i in range(5):
    for j in range(5):
        if F_centros[i,j] <= limites_F[1]:
            F_clasificado[i,j] = etiquetas[0]
        elif F_centros[i,j] <= limites_F[2]:
            F_clasificado[i,j] = etiquetas[1]
        elif F_centros[i,j] <= limites_F[3]:
            F_clasificado[i,j] = etiquetas[2]
        elif F_centros[i,j] <= limites_F[4]:
            F_clasificado[i,j] = etiquetas[3]
        else:
            F_clasificado[i,j] = etiquetas[4]

#mostrar F_clasificado en una tabla
print(F_clasificado)

#guardar F_clasificado en un archivo de texto
np.savetxt('DIY_F.txt', F_clasificado, fmt='%s')







