import matplotlib.pyplot as plt
import numpy as np

plt.ion()  # Activa el modo interactivo de matplotlib
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Establece límites en el eje radial (r) y el ángulo (theta)
ax.set_rmax(1)
ax.set_rticks([0.2, 0.4, 0.6, 0.8, 1])
ax.set_rlabel_position(-22.5)  # Mueve las etiquetas radiales

i = 0
num_points_to_display = 100  # Número de puntos a mostrar en el gráfico

while i < 1000:
    temp_y = np.random.random()
    temp_theta = 2 * np.pi * temp_y  # Convierte la coordenada y en un ángulo

    # Agrega el punto en coordenadas polares
    ax.scatter(temp_theta, temp_y)

    i += 1
    plt.pause(0.0001)  # Pausa para mostrar el gráfico en tiempo real

    # Limita la cantidad de puntos mostrados en el gráfico
    if len(ax.lines) > num_points_to_display:
        ax.lines[0].remove()  # Elimina el punto más antiguo

plt.ioff()  # Desactiva el modo interactivo al finalizar
plt.show()
