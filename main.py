import sys
from visual import juego  

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.txt")
    else:
        archivo = sys.argv[1]
        juego(archivo)
