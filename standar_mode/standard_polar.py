import serial
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

# SECCION LIDAR
uart1 = serial.Serial('/dev/ttyUSB0', baudrate=115200)  # Inicializa el puerto serie.
uart1.write(bytes([0xA5, 0x20]))  # Envía el comando para iniciar el escaneo en modo estándar.
sleep(0.002)  # Espera por el Descriptor de Respuesta (debe ser > 0.002).
print(uart1.read(7))  # Lee el Descriptor de Respuesta.
sleep(0.8)  # Espera por los datos de respuesta (debe ser > 0.8 a 0x20).
points = []

# SECCION POLAR
plt.ion()  # Activa el modo interactivo de matplotlib
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Establece límites en el eje radial (r) y el ángulo (theta)s
ax.set_rmax(1)
ax.set_rticks([5, 10, 15, 20, 25])
ax.set_rlabel_position(-22.5)  # Mueve las etiquetas radiales

i = 0
num_points_to_display = 5  # Número de puntos a mostrar en el gráfico

a = 1
while a <= 100:
    message = uart1.read(5)
    if len(message) == 5:
        if (message[0] & 0b11) == 1:
            print('new scan')
        elif (message[0] & 0b11) == 2:
            print('current scan')
        else:
            print('error in sampling')
            a = 200
        print(bin(message[2]), bin(message[1]), bin(message[0]), bin(message[0] & 0b11))
        angl = ((message[2] << 7)) | (message[1] >> 1)
        dist = (message[4] << 8) | (message[3])
        print(bin(angl), angl, len(bin(angl)))
        print('Angulo:', angl / 64, 'Distancia:', dist / 40)

        # Agrega el punto en coordenadas polares
        points.append([np.pi / 180 * angl / 64, dist / 40])

        # Limita la cantidad de puntos mostrados en el gráfico
        if len(points) > num_points_to_display:
            points.pop(0)

        # Actualiza los datos del gráfico directamente
        ax.clear()  # Borra el gráfico actual
        ax.scatter(*zip(*points))  # Agrega los puntos actualizados

        i += 1
        plt.pause(0.001)  # Pausa para mostrar el gráfico en tiempo real

    else:
        a = 200

uart1.write(bytes([0xA5, 0x25]))
sleep(0.5)
uart1.read()

plt.ioff()  # Desactiva el modo interactivo al finalizar
plt.show()
