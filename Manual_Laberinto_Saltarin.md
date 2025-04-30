
# Manual de Uso del Juego "Laberinto Saltarín"

## Requisitos Previos


1. **Tener Python instalado** (versión 3.7 o superior). Se puede descargar desde:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Instalar la biblioteca PyGame**. Para hacerlo, ejecute en su terminal:

   ```bash
   pip install pygame
   ```

3. **Clonar el repositorio del proyecto** desde GitHub (o copiar los archivos fuente si ya los tienes):

   ```bash
   git clone https://github.com/krsconnie/T1-IA.git 
   
   ```
El ejemplo muestra https, pero en github se encuentran más formas de clonar un repositorio.
 

---

## Archivos del Proyecto

- `main.py`: Punto de entrada del programa. Llama a la función `juego(nombre_archivo)` para iniciar la interfaz visual.
- `visual.py`: Maneja la interfaz gráfica con PyGame. Permite visualizar los laberintos, navegar entre ellos y resolverlos con distintos algoritmos.
- `lectura.py`: Lee y guarda la información del input.
- `agentes.py`: Contiene las implementaciones de búsqueda como DFS, Costo Uniforme Constante y Costo Uniforme Variable.

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

Desde una terminal, ejecute:

```bash
python main.py archivo.txt
```

Reemplace `archivo.txt` con el nombre de su archivo de entrada. También el repositorio se encuentra un "ejemplos.txt" con laberintos propuestos

**Ejemplo:**

```bash
python main.py ejemplos.txt
```

Esto ejecutará la interfaz donde se podrá observar el laberinto y el camino creado por los algoritmos

---

## Interfaz Gráfica y Controles
![Screenshot from 2025-04-27 16-19-24](https://github.com/user-attachments/assets/f1258f7b-0e02-4f94-8eaf-4e27245e08bf)
![Screenshot from 2025-04-25 17-35-38](https://github.com/user-attachments/assets/78c81ece-2259-4f23-a29e-ad272d7f2468)



Una vez abierta la ventana del juego, se tendrá acceso a los siguientes botones:

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

- Si no se ejecuta con un archivo como argumento, verá:
  ```
  Uso: python main.py archivo.txt
  ```
- Si el archivo no tiene el formato correcto o está incompleto, verá:

  ```
  No se encontraron laberintos válidos.
  ```
