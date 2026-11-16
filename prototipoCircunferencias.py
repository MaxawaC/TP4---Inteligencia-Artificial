import numpy as np
import matplotlib.pyplot as plt

alto = 160
ancho = 160
imagen = np.zeros((alto, ancho))

centro_x_real = 82
centro_y_real = 75
radio = 35

angulos = np.linspace(0, 2 * np.pi, 720)

for angulo in angulos:
    x = int(round(centro_x_real + radio * np.cos(angulo)))
    y = int(round(centro_y_real + radio * np.sin(angulo)))
    if 0 <= x < ancho and 0 <= y < alto:
        imagen[y, x] = 1

np.random.seed(20)
ruido_y = np.random.randint(0, alto, 35)
ruido_x = np.random.randint(0, ancho, 35)
imagen[ruido_y, ruido_x] = 1

puntos_y, puntos_x = np.where(imagen == 1)

acumulador = np.zeros((alto, ancho))
angulos_busqueda = np.linspace(0, 2 * np.pi, 360, endpoint=False)
desplazamientos_x = radio * np.cos(angulos_busqueda)
desplazamientos_y = radio * np.sin(angulos_busqueda)

for x, y in zip(puntos_x, puntos_y):
    posibles_centros_x = np.rint(x - desplazamientos_x).astype(int)
    posibles_centros_y = np.rint(y - desplazamientos_y).astype(int)

    validos = (
        (posibles_centros_x >= 0) &
        (posibles_centros_x < ancho) &
        (posibles_centros_y >= 0) &
        (posibles_centros_y < alto)
    )

    np.add.at(
        acumulador,
        (posibles_centros_y[validos], posibles_centros_x[validos]),
        1
    )

centro_y_detectado, centro_x_detectado = np.unravel_index(
    np.argmax(acumulador),
    acumulador.shape
)

print("Centro X detectado:", centro_x_detectado)
print("Centro Y detectado:", centro_y_detectado)
print("Centro X original:", centro_x_real)
print("Centro Y original:", centro_y_real)
print("Radio utilizado:", radio)
print("Votos obtenidos:", int(acumulador[centro_y_detectado, centro_x_detectado]))

fig, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray", origin="upper")
ejes[0].set_title("Imagen original con ruido")
ejes[0].set_xlabel("X")
ejes[0].set_ylabel("Y")

ejes[1].imshow(acumulador, cmap="hot", origin="upper")
ejes[1].set_title("Acumulador de centros")
ejes[1].set_xlabel("X")
ejes[1].set_ylabel("Y")

ejes[2].imshow(imagen, cmap="gray", origin="upper")
circunferencia = plt.Circle(
    (centro_x_detectado, centro_y_detectado),
    radio,
    fill=False,
    color="red",
    linewidth=2
)
ejes[2].add_patch(circunferencia)
ejes[2].plot(centro_x_detectado, centro_y_detectado, "bo")
ejes[2].set_title("Circunferencia detectada")
ejes[2].set_xlabel("X")
ejes[2].set_ylabel("Y")

plt.tight_layout()
plt.show()