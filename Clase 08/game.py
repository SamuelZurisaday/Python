import time

filas = 8
columnas = 8

def dibujar_tablero(x, y):
    # Aquí iría la lógica para dibujar el tablero, por ejemplo, imprimir las coordenadas
    print(f"Dibujando el tablero en fila {x}, columna {y}")

fila = 0
columna = 0

while fila < filas and columna < columnas:
    fila += 1
    columna += 1
    print("______________")
    dibujar_tablero(fila, columna)
    print("______________")
    time.sleep(1)
    if fila == filas or columna == columnas:
        print("Alcanzado el limite del tablero. Terminando...")
        break