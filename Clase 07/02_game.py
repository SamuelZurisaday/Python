import time

tablero = []
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(".")
    tablero.append(fila)

print(tablero)

"""
cómo se vería el código usando una comprensión de listas:


tablero = [["." for j in range(3)] for i in range(5)]
print(tablero)

"""

for xx in tablero:
    time.sleep(1)
    #print(xx)
    print("  ".join(xx))