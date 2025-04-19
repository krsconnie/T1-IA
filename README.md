# Tarea 1: Laberinto Saltarín IA
### Fecha de Entrega : 30 de abril

## Requisitos

1. Implementar el juego del laberinto saltarín con PyGame.
2. Implementar un agente que resuelva el laberinto saltarín con los métodos: DFS y costo uniforme.
3. Defina una heurística admisible para el problema del laberinto saltarín (bonus)

## Laberinto Saltarín

<div align="center">
  <img src="https://github.com/user-attachments/assets/8a855cfd-5cf2-425c-a771-934c6433aff8" alt="image">
</div>

Se define como una grilla de m por n de números saltarines, una celda
inicial (en un círculo arriba), y una celda de destino (marcada “G”). 

### Reglas
En base al número saltarín de cada celda:

1. Un movimiento corresponde a moverse esa cantidad exacta de celdas ya sea de forma horizontal o vertical, en línea recta.
2. No está permitido moverse de manera diagonal ni cambiar de dirección a medio camino.
3. Sólo se permiten movimientos en que el número de celdas a mover no sobrepasa alguno de los límites del laberinto.
4. El objetivo del laberinto saltarín es encontrar el camino más corto, es decir, la menor cantidad
de movimientos desde la celda inicial hasta la celda de destino.

Por ejemplo, en el laberinto de arriba, se logra llegar al objetivo en un mínimo de 13 movimientos: Abajo, Derecha,
Izquierda, Arriba, Abajo, Izquierda, Derecha, Arriba, Izquierda, Izquierda, Derecha, Abajo,
Arriba.

## Formato Archivo de Entrada

     m n fila_inicio col_inicio fila_objetivo col_objetivo 

1. m: número de filas
2. n: número de columnas
3. fila_inicio, col_inicio: coordenadas de la celda inicial
4. fila_objetivo, col_objetivo: coordenadas de la celda de destino.

Luego vienen m líneas, cada una con n números enteros, que representan la grilla de números saltarines.La entrada puede contener varios laberintos. Cuando ya no hay más, se indica con una línea que contiene solo un 0.

### Ejemplo:

      3 3 0 0 2 2
      2 3 1
      1 2 3
      2 1 2
      0

## Formato Archivo de Salida

Por cada laberinto, el programa debe imprimir una línea con:

1. El número de movimientos del camino más corto
2. "no hay solución" si el destino no es alcanzable.

### Ejemplo:

    13
    no hay solución
    20

# Entrega

Debes entregar los siguientes elementos:

1. **Código fuente** del programa (en C, C++ o Python).
2. **Informe breve** (máximo 5 páginas) que incluya:
   - Descripción general del código y sus funciones principales.
   - Un ejemplo de entrada/salida (distinto al del enunciado).

---

## Restricciones y Consideraciones

- **El agente de búsqueda (DFS y costo uniforme) debe ser implementado manualmente**.  
  No se permite usar funciones ya implementadas de librerías externas.
  
- El código debe ser **original y propio**.  
  Cualquier evidencia de copia (entre estudiantes o desde internet) implicará una calificación de **1.0** para todos los involucrados.
