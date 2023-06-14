import matplotlib.pyplot as plt

# Datos para la primera figura
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Datos para la segunda figura
x2 = [1, 3, 5, 7, 9]
y2 = [1, 4, 9, 16, 25]

# Crear la primera figura
plt.figure(1)
plt.plot(x1, y1)
plt.title('Figura 1')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Crear la segunda figura
plt.figure(2)
plt.plot(x2, y2)
plt.title('Figura 2')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar las dos figuras
plt.show()

