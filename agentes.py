import heapq

# Busqueda en profundidad
def dfs(laberinto):
    grid = laberinto['grid']
    inicio = laberinto['inicio']
    destino = laberinto['destino']
    m, n = laberinto['filas'], laberinto['cols']

    stack = [(inicio[0], inicio[1], [])]
    visitados = set()
    camino_corto = None

    while stack:
        x, y, camino = stack.pop()

        if (x, y) == destino: 
            if camino_corto is None or len(camino + [(x, y)]) < len(camino_corto): # actualiza el camino más corto
                camino_corto = camino + [(x, y)]
            continue

        if (x, y) not in visitados:
            visitados.add((x, y))
            salto = grid[x][y]

            if x - salto >= 0:
                stack.append((x - salto, y, camino + [(x, y)]))
            if y + salto < n:
                stack.append((x, y + salto, camino + [(x, y)]))
            if x + salto < m:
                stack.append((x + salto, y, camino + [(x, y)]))
            if y - salto >= 0:
                stack.append((x, y - salto, camino + [(x, y)]))

    return camino_corto

# Costo uniforme 
# Se asume que el costo de cada movimiento es 1
def costo_uniforme(laberinto):

    grid = laberinto['grid']
    inicio = laberinto['inicio']
    destino = laberinto['destino']
    m, n = laberinto['filas'], laberinto['cols']

    pq = [(0, inicio[0], inicio[1], [])]  # (costo, x, y, camino)
    visitados = set()

    while pq:
        costo, x, y, camino = heapq.heappop(pq)

        if (x, y) == destino:
            return camino + [(x, y)]

        if (x, y) not in visitados:
            visitados.add((x, y))
            salto = grid[x][y]

            if x - salto >= 0:
                heapq.heappush(pq, (costo + 1, x - salto, y, camino + [(x, y)]))

            if x + salto < m:
                heapq.heappush(pq, (costo + 1, x + salto, y, camino + [(x, y)]))

            if y + salto < n:
                heapq.heappush(pq, (costo + 1, x, y + salto, camino + [(x, y)]))

            if y - salto >= 0:
                heapq.heappush(pq, (costo + 1, x, y - salto, camino + [(x, y)]))

    return None


def costo_uniforme_variable(laberinto):
    grid = laberinto['grid']
    inicio = laberinto['inicio']
    destino = laberinto['destino']
    m, n = laberinto['filas'], laberinto['cols']

    pq = [(0, inicio[0], inicio[1], [])]
    visitados = set()

    while pq:
        costo, x, y, camino = heapq.heappop(pq)  # Tomamos el nodo de menor costo

        if (x, y) == destino:
            return camino + [(x, y)]

        
        if (x, y) not in visitados:
            visitados.add((x, y))
            salto = grid[x][y]  # El valor de la celda es la cantidad de casillas que podemos saltar

            
            if x - salto >= 0:
                heapq.heappush(pq, (costo + salto, x - salto, y, camino + [(x, y)]))
            
            if x + salto < m:
                heapq.heappush(pq, (costo + salto, x + salto, y, camino + [(x, y)]))
            
            if y + salto < n:
                heapq.heappush(pq, (costo + salto, x, y + salto, camino + [(x, y)]))
          
            if y - salto >= 0:
                heapq.heappush(pq, (costo + salto, x, y - salto, camino + [(x, y)]))

    return None
