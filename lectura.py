# La función leer_laberintos recibe el nombre del archivo con el input
# y devuelve una lista de laberintos, cada uno representado como un diccionario.
def leer_laberintos(nombre_archivo):
    laberintos = []                  #Lista de laberintos
    
    #Abre el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        while True:
            linea = archivo.readline()
            if not linea or linea.strip() == '0': # Si encuentra una línea vacia o un 0 termina de leer
                break
            m, n, ini_x, ini_y, dest_x, dest_y = map(int, linea.strip().split()) # Separa los valores de la línea, los convierte a enteros
                                                                    # y los asigna a las variables correspondientes
            grid = [] # Crea la matriz 
            for _ in range(m): # Lee las siguientes m líneas
                fila = list(map(int, archivo.readline().strip().split())) # Cada línea se convierte en una lista de enteros
                grid.append(fila) # Agrega la fila a la matriz

                #Agrega el laberinto resultante a lista de laberintos (como un diccionario)
            laberintos.append({ 
                'filas': m,
                'cols': n,
                'inicio': (ini_x, ini_y),
                'destino': (dest_x, dest_y),
                'grid': grid
            })
    return laberintos

# La función imprimir_laberintos recibe un laberinto y lo imprime en consola
# esto es usado para verificar que el laberinto se haya leído correctamente.

def imprimir_laberintos(laberintos): # Recibe la lista de laberintos
    for idx, lab in enumerate(laberintos): # Recorre cada laberinto
        # Imprime el n° del laberinto, sus dimensiones, las coordenadas del inicio y la meta
        print(f"\nLaberinto {idx + 1}")
        print(f"Tamaño: {lab['filas']} filas x {lab['cols']} columnas")
        print(f"Inicio: {lab['inicio']}")
        print(f"Destino: {lab['destino']}")
        print("Grilla:")
        for fila in lab['grid']: # Imprime cada fila del laberinto (formando la matriz del laberinto)
            print(" ".join(str(num) for num in fila))

# La función verificar_archivo recibe el nombre del archivo
# y verifica que este exista y se pueda abrir
def verificar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            return True
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe, seleccione un archivo existente por favor.")
        return False
    
    except IOError as e:
        print(f"Error: No se pudo abrir el archivo '{nombre_archivo}': {e}")
        return False
    


# Testeo de funciones básicas
if __name__ == '__main__':

    if verificar_archivo("input.txt"):
        laberintos = leer_laberintos("input.txt")
        imprimir_laberintos(laberintos)

