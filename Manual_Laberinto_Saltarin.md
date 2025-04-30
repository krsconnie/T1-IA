
# Manual de Uso del Juego "Laberinto Saltarín"

## Requisitos Previos

Antes de ejecutar el juego, asegúrate de cumplir con los siguientes requisitos:

1. **Tener Python instalado** (versión 3.7 o superior). Puedes descargarlo desde:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar la biblioteca PyGame**. Para hacerlo, ejecuta en tu terminal:

   ```bash
   pip install pygame
   ```

3. **Clonar el repositorio del proyecto** desde GitHub (o copiar los archivos fuente si ya los tienes):

   ```bash
   git clone https://github.com/usuario/laberinto-saltarin.git
   cd laberinto-saltarin
   ```

   Reemplaza la URL con la correcta si es distinta.

---

## Archivos del Proyecto

- `main.py`: Punto de entrada del programa. Llama a la función `juego(nombre_archivo)` para iniciar la interfaz visual.
- `visual.py`: Maneja la interfaz gráfica con PyGame. Permite visualizar los laberintos, navegar entre ellos y resolverlos con distintos algoritmos.
- `lectura.py`: Lee y procesa uno o varios laberintos desde un archivo de entrada.
- `agentes.py`: Contiene las implementaciones de búsqueda como DFS, Costo Uniforme y Costo Variable.

---

## Formato del Archivo de Entrada (`archivo.txt`)

El archivo puede contener uno o **varios laberintos**, cada uno definido con el siguiente formato:

```
m n fila_inicio col_inicio fila_destino col_destino
fila1
fila2
...
fila_m
```

Donde:

- `m`: número de filas del laberinto.
- `n`: número de columnas del laberinto.
- `(fila_inicio, col_inicio)`: coordenadas de la celda inicial.
- `(fila_destino, col_destino)`: coordenadas de la celda objetivo.
- Cada `filaX` contiene `n` enteros que indican el "número saltarín" de cada celda.
- Las coordenadas parten desde `(0, 0)`.

**Ejemplo de entrada para dos laberintos:**

```
4 4 0 0 3 3
2 3 1 1
1 2 1 1
1 1 3 2
1 1 1 1
3 3 0 0 2 2
2 1 1
1 2 1
1 1 3
0
```

- El archivo **debe terminar con una línea que contiene solo un `0`** para indicar el fin del archivo.

---

## Ejecución del Juego

Desde una terminal, ejecuta:

```bash
python main.py archivo.txt
```

Reemplaza `archivo.txt` con el nombre de tu archivo de entrada.

**Ejemplo:**

```bash
python main.py laberintos.txt
```

Esto abrirá una ventana con interfaz visual donde podrás explorar y resolver los laberintos.

---

## Interfaz Gráfica y Controles

Una vez abierta la ventana del juego, tendrás acceso a los siguientes botones:

- **Anterior**: Muestra el laberinto anterior del archivo.
- **Siguiente**: Muestra el siguiente laberinto del archivo.
- **DFS**: Resuelve el laberinto actual usando *búsqueda en profundidad*.
- **Costo Uniforme**: Resuelve el laberinto usando *búsqueda de costo uniforme* (UCS).
- **Costo Variable**: Resuelve el laberinto considerando un costo personalizado por celda.

Además, **cada vez que se ejecuta un algoritmo**, en la **consola se imprime el costo total de la solución encontrada** o un mensaje indicando que **no existe solución usando el algoritmo seleccionado**.

Visualmente:

- La **celda de inicio** se marca en **rojo**.
- La **celda destino** se marca en **lila**.
- El **camino entre inicio y destino** se pinta con un **gradiente de color**, donde el color es **más oscuro al comienzo** y se **aclara progresivamente** a medida que se acerca al destino.

---

## Posibles Errores Comunes

- Si no ejecutas con un archivo como argumento, verás:
  ```
  Uso: python main.py archivo.txt
  ```
- Si el archivo no tiene el formato correcto o está incompleto, el programa puede cerrarse o no mostrar nada.
- Asegúrate de terminar el archivo con un `0` en una línea separada para indicar el fin de los laberintos.

---

## Personalización

- Puedes modificar o añadir algoritmos en `agentes.py`.
- Puedes cambiar colores, tamaños de celda u otros aspectos visuales en `visual.py`.
