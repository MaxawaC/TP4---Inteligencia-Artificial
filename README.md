# Instalación y ejecución

## 1. Requisitos

Para ejecutar los prototipos se necesita:
- Python instalado
- Los archivos `.py` incluidos

Las librerías necesarias son:
- **NumPy:** permite trabajar con matrices, arreglos y operaciones numéricas
- **Matplotlib:** permite generar y mostrar los gráficos de los resultados
Ambas dependencias están especificadas en el archivo `requirements.txt`.

## 2. Preparar el proyecto

Descargar el repositorio desde gitHub mediante la opción **Code → Download ZIP** y descomprimirlo.

También se puede clonar desde una terminal con el siguiente comando:

```bash
git clone URL_DEL_REPOSITORIO
```

Una vez descargado, abrir una terminal dentro de la carpeta principal del proyecto. Allí deben encontrarse los archivos `requirements.txt`, `prototipoRectas.py` y `prototipoCircunferencias.py`.

## 3. Instalar las librerías

Desde la terminal, ejecutar:

```bash
py -m pip install -r requirements.txt
```

Este comando lee el archivo `requirements.txt` e instala automáticamente todas las librerías necesarias para ejecutar los prototipos.

No es necesario instalar NumPy y Matplotlib por separado.

Al finalizar las dependencias estarán instaladas y el proyecto estará listo para ejecutarse.

## 4. Ejecutar los prototipos

Los archivos se ejecutan de manera independiente. Desde la terminal, ubicada en la carpeta principal del proyecto, utilizar los siguientes comandos:

**Prototipo de detección de rectas:**

```bash
python prototipoRectas.py
```

**Prototipo de detección de circunferencias:**

```bash
python prototipoCircunferencias.py
```

En cada ejecución se abrirá una ventana con los gráficos correspondientes al procesamiento realizado.