import time


filas = 8
columnas = 8
tablero = []
for i in range(filas):

    fila = []
    for j in range(columnas):
        fila.append(".")
    tablero.append(fila)

print("_____TABLERO 1")
for xx in tablero:
    time.sleep(.2)
    print("  ".join(xx))

# 1. en la tercer fila y septima columna, colocar un "0"

tablero[2][6] = "0"
print("_____TABLERO 2")
for xx in tablero:
    time.sleep(.2)
    print("  ".join(xx))