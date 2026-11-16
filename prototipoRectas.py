import numpy as np
import matplotlib.pyplot as plt

alto = 160
ancho = 200
imagen = np.zeros((alto, ancho))

pendiente_real = 0.6
ordenada_real = 20

for x in range(ancho):
    y = int(pendiente_real * x + ordenada_real)
    if 0 <= y < alto:
        imagen[y, x] = 1

np.random.seed(10)
ruido_y = np.random.randint(0, alto, 45)
ruido_x = np.random.randint(0, ancho, 45)
imagen[ruido_y, ruido_x] = 1

puntos_y, puntos_x = np.where(imagen == 1)

pendientes = np.arange(-1.5, 1.51, 0.01)
b_min = -250
b_max = 350
acumulador = np.zeros((len(pendientes), b_max - b_min + 1))

for i, m in enumerate(pendientes):
    valores_b = np.rint(puntos_y - m * puntos_x).astype(int)
    indices_b = valores_b - b_min
    validos = (indices_b >= 0) & (indices_b <= b_max - b_min)
    np.add.at(acumulador[i], indices_b[validos], 1)

indice_m, indice_b = np.unravel_index(np.argmax(acumulador), acumulador.shape)

pendiente_detectada = pendientes[indice_m]
ordenada_detectada = indice_b + b_min

x_linea = np.array([0, ancho - 1])
y_linea = pendiente_detectada * x_linea + ordenada_detectada

print("Pendiente detectada:", round(pendiente_detectada, 2))
print("Ordenada al origen detectada:", ordenada_detectada)
print("Votos obtenidos:", int(acumulador[indice_m, indice_b]))

fig, ejes = plt.subplots(1, 3, figsize=(15, 5))

ejes[0].imshow(imagen, cmap="gray", origin="upper")
ejes[0].set_title("Imagen original con ruido")
ejes[0].set_xlabel("X")
ejes[0].set_ylabel("Y")

ejes[1].imshow(
    acumulador,
    aspect="auto",
    cmap="hot",
    extent=[b_min, b_max, pendientes[-1], pendientes[0]]
)
ejes[1].set_title("Espacio acumulador (m, b)")
ejes[1].set_xlabel("Ordenada al origen (b)")
ejes[1].set_ylabel("Pendiente (m)")

ejes[2].imshow(imagen, cmap="gray", origin="upper")
ejes[2].plot(x_linea, y_linea, color="red", linewidth=2)
ejes[2].set_title("Recta detectada")
ejes[2].set_xlabel("X")
ejes[2].set_ylabel("Y")

plt.tight_layout()
plt.show()