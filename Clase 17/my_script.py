import sys

print("Hello!")
print()
print(sys.argv)
print(type(sys.argv))
print()

# Comprobar si se han pasado argumentos adicionales
if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        print("El usuario ingreso 1")
    else:
        print("No reconozco el numero")
else:
    print("No se proporcionaron argumentos adicionales.")