import pygame
import sys
from lectura import leer_laberintos
from agentes import dfs, costo_uniforme, costo_uniforme_variable
# SUPERIMPORTANTE!!!!Recordar quitar anotaciones antes de entregar

# Constantes
COLOR_FONDO = (224, 214, 138)  # amarillo pálido
COLOR_LINEA = (50, 10, 40)  # marrón oscuro
COLOR_TEXTO = (81, 23, 48)  # marrón más claro
COLOR_INICIO = (220, 69, 54)  # rojito
COLOR_META = (217, 145, 186)  # rosado claro
COLOR_CAMINO = (255, 197, 240)  

TAM_CELDA_MIN = 45
TAM_CELDA_MAX = 80

# Botones
BOTONES = {  # si me sobra tiempo agregar el libre para que uno pueda jugar 
    "anterior": pygame.Rect(0, 0, 120, 40),
    "siguiente": pygame.Rect(0, 0, 120, 40),
    "dfs": pygame.Rect(0, 0, 120, 40),
    "costo": pygame.Rect(0, 0, 150, 40),
    "costo var": pygame.Rect(0, 0, 180, 40),
}

# Colores de los botones
COLOR_BOTON_NORMAL = (245, 150, 190)  # Color normal del botón
COLOR_BOTON_HOVER = (224, 71, 158)  # Color cuando el mouse pasa sobre el botón


# Fuentes
pygame.font.init()
fuente_titulo = pygame.font.SysFont("Times New Roman", 52, bold=True)
fuente_normal = pygame.font.SysFont("Times New Roman", 30)

# Cálculo del tamaño de las celdas, trata de escoger el menor tamaño posible para que el laberinto se vea bien
def calcular_tam_celda(m, n):
    tam_x = (MAX_ANCHO - 20 ) // n  # Ancho menos el espacio para los bordes dividido por el número de columnas 
    tam_y = (MAX_ALTO - 100) // m  # Alto menos el espacio para los botones y titulo dividido por el número de filas
    tam_celda = min(tam_x, tam_y, TAM_CELDA_MAX) 
    return tam_celda

# Dibuja los botones en la pantalla especificada con la fuente específicada
def dibujar_botones(pantalla, fuente):
    
    # Aumentar el tamaño de los botones
    ancho_boton = 150  # Ancho de los botones
    alto_boton = 50  # Alto de los botones

    
    for nombre, rect in BOTONES.items():
        rect.width = ancho_boton
        rect.height = alto_boton

    total_width = sum([btn.width for btn in BOTONES.values()]) + 20 * (len(BOTONES) - 1)
    start_x = (MAX_ANCHO - total_width) // 2
    
    y_pos = MAX_ALTO - 100
    x_pos = start_x
    
    for nombre, rect in BOTONES.items():
        rect.x = x_pos
        rect.y = y_pos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        color_fondo = COLOR_BOTON_HOVER if rect.collidepoint(mouse_x, mouse_y) else COLOR_BOTON_NORMAL
        
        # botón con esquinas redondeadas
        pygame.draw.rect(pantalla, color_fondo, rect, border_radius=15)

        # Dibujar el texto sobre el botón
        texto = fuente.render(nombre.capitalize(), True, (255, 255, 255))
        texto_rect = texto.get_rect(center=rect.center)
        pantalla.blit(texto, texto_rect)

        # Mover la posición de los botones
        x_pos += rect.width + 20

# Dibuja el laberinto en la ventana específicada
# recibe también el laberinto a mostrar, la fuente a usar
# el camino a mostrar (puede ser nulo), el n° del laberinto y los pasos mostrados (empezando en 0)
def dibujar_laberinto(pantalla, laberinto, fuente, camino=None, lab_index=None, pasos_mostrados=0):
   
    # Obtener la información básica del laberinto (filas, columnas, inicio y destino)
    m = laberinto['filas']
    n = laberinto['cols']
    grid = laberinto['grid']
    inicio = laberinto['inicio']
    destino = laberinto['destino']

    # Centrar el laberinto en la pantalla
    offset_x = (MAX_ANCHO - n * TAM_CELDA) // 2
    offset_y = (MAX_ALTO - (m * TAM_CELDA)) // 2
    if offset_y < 60:   # evita que el laberinto quede muy arriba
        offset_y = 60

    texto_lab = fuente_titulo.render(f"Laberinto {lab_index + 1}", True, COLOR_TEXTO) # titulo del laberinto
    texto_lab_rect = texto_lab.get_rect(center=(MAX_ANCHO // 2, 80)) # centrado
    pantalla.blit(texto_lab, texto_lab_rect)

    # Prepara el camino a mostrar
    camino_visto = set()
    if camino:
        camino_visto = set(camino[:pasos_mostrados])

    # Recorre el laberinto y dibuja cada celda
    for i in range(m):
        for j in range(n):
            x = offset_x + j * TAM_CELDA
            y = offset_y + i * TAM_CELDA
            rect = pygame.Rect(x, y, TAM_CELDA, TAM_CELDA)

            # Pintar fondo celdas en el camino
            if camino:
                for idx, (cx, cy) in enumerate(camino[:pasos_mostrados]):
                    if cx == i and cy == j:
                    # Escalar el color según la posición en el camino, podría ver si queda bonito con los números de distinto color
                        intensidad = idx / max(1, len(camino))  # valor entre 0 y 1
                    
                        r = int(COLOR_CAMINO[0] * (0.4 + 0.6 * intensidad))  
                        g = int(COLOR_CAMINO[1] * (0.4 + 0.6 * intensidad))
                        b = int(COLOR_CAMINO[2] * (0.4 + 0.6 * intensidad))
                        color_variable = (r, g, b)
                        pygame.draw.rect(pantalla, color_variable, rect)
                        break 

            # Dibujar el borde de la celda
            pygame.draw.rect(pantalla, COLOR_LINEA, rect, 2)

            # Dibujar el valor de la celda
            valor = grid[i][j] 
            texto = fuente.render(str(valor), True, COLOR_TEXTO)
            texto_rect = texto.get_rect(center=rect.center)
            pantalla.blit(texto, texto_rect)

    # Dibujar casillas de inicio
    ix, iy = inicio
    x0 = offset_x + iy * TAM_CELDA
    y0 = offset_y + ix * TAM_CELDA
    rect_inicio = pygame.Rect(x0, y0, TAM_CELDA, TAM_CELDA)
    pygame.draw.rect(pantalla, COLOR_INICIO, rect_inicio, 3)
   
    # Dibujar casillas de meta
    dx, dy = destino
    xg = offset_x + dy * TAM_CELDA
    yg = offset_y + dx * TAM_CELDA
    rect_meta = pygame.Rect(xg, yg, TAM_CELDA, TAM_CELDA)
    pygame.draw.rect(pantalla, COLOR_META, rect_meta, 3)

# Dibuja el contorno del camino encontrado
# si me sobra el tiempo, agregar animación y color degradado
# para que se vea más bonito
def dibujar_camino(pantalla, camino, offset_x, offset_y, tam_celda, pasos_mostrados):
    for idx in range(pasos_mostrados):
        fila, col = camino[idx]
        x = offset_x + col * tam_celda
        y = offset_y + fila * tam_celda
        rect = pygame.Rect(x, y, tam_celda, tam_celda)
        pygame.draw.rect(pantalla, COLOR_LINEA, rect, width=4)


def juego(nombre_archivo):
    pygame.init()
    laberintos = leer_laberintos(nombre_archivo)
    if not laberintos:
        print("No se encontraron laberintos válidos.")
        return

    info_pantalla = pygame.display.Info()
    ancho_pantalla = info_pantalla.current_w
    alto_pantalla = info_pantalla.current_h

    global MAX_ANCHO, MAX_ALTO
    MAX_ANCHO = min(ancho_pantalla, 1000)
    MAX_ALTO = min(alto_pantalla, 800)

    lab_actual = 0
    camino_actual = None
    pasos_mostrados = 0
    mensaje_error = ""
    tiempo_mensaje_error = 0 
    reloj = pygame.time.Clock()

    pantalla = pygame.display.set_mode((MAX_ANCHO, MAX_ALTO))
    pygame.display.set_caption("Laberinto")

    while True:
        lab = laberintos[lab_actual]
        m, n = lab['filas'], lab['cols']
        global TAM_CELDA
        TAM_CELDA = calcular_tam_celda(m, n)
        pantalla.fill(COLOR_FONDO)
        dibujar_botones(pantalla, fuente_normal)

        offset_x = (MAX_ANCHO - n * TAM_CELDA) // 2
        offset_y = (MAX_ALTO - (m * TAM_CELDA)) // 2
        if offset_y < 60:
            offset_y = 60

        dibujar_laberinto(pantalla, lab, fuente_normal, camino_actual, lab_actual, pasos_mostrados)

        if camino_actual:
            if pasos_mostrados < len(camino_actual):
                pasos_mostrados += 1
            dibujar_camino(pantalla, camino_actual, offset_x, offset_y, TAM_CELDA, pasos_mostrados)

        # Mostrar mensaje de error si existe y no han pasado 3 segundos
        if mensaje_error:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_mensaje_error < 3000:  # 3 segundos, probar si queda bien!!!!! 
                texto_error = fuente_normal.render(mensaje_error, True, (255, 0, 0))  # Rojo
                rect_error = texto_error.get_rect(center=(MAX_ANCHO // 2, MAX_ALTO - 120))
                pantalla.blit(texto_error, rect_error)
            else:
                mensaje_error = ""  # Borrar mensaje pasado el tiempo

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if BOTONES['siguiente'].collidepoint(pos):
                    lab_actual = (lab_actual + 1) % len(laberintos)
                    camino_actual = None
                    mensaje_error = ""
                elif BOTONES['anterior'].collidepoint(pos):
                    lab_actual = (lab_actual - 1) % len(laberintos)
                    camino_actual = None
                    mensaje_error = ""
                elif BOTONES['dfs'].collidepoint(pos):
                    camino_actual = dfs(lab)
                    pasos_mostrados = 0
                    if camino_actual is None:
                        mensaje_error = "No hay solución usando DFS."
                        tiempo_mensaje_error = pygame.time.get_ticks()
                        print(mensaje_error)
                    else:
                        mensaje_error = ""
                        print(f"Camino DFS encontrado: {camino_actual}")
                elif BOTONES['costo'].collidepoint(pos):
                    camino_actual = costo_uniforme(lab)
                    pasos_mostrados = 0
                    if camino_actual is None:
                        mensaje_error = "No hay solución usando Costo Uniforme."
                        tiempo_mensaje_error = pygame.time.get_ticks()
                        print(mensaje_error)
                    else:
                        mensaje_error = ""
                        print(f"Camino Costo Uniforme encontrado: {camino_actual}")
                elif BOTONES['costo var'].collidepoint(pos):
                    camino_actual = costo_uniforme_variable(lab)
                    pasos_mostrados = 0
                    if camino_actual is None:
                        mensaje_error = "No hay solución usando Costo variable."
                        tiempo_mensaje_error = pygame.time.get_ticks()
                        print(mensaje_error)
                    else:
                        mensaje_error = ""
                        print(f"Camino Costo variable encontrado: {camino_actual}")

        reloj.tick(5)
