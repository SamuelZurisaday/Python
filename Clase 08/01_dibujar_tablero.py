def dibujar_tablero():
    filas = 8
    columnas = 10


    tablero = []
    for i in range(filas):
        fila = ["."] * columnas
        tablero.append(fila)

    for xx in tablero:
        print(".".join(xx))

for indice, xx in enumerate(range(10)):
    print(indice)
    dibujar_tablero()
    print()
