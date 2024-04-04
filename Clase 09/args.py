def saludar(**kwargs):
#    print(type(args), len(args), args)
    for posicion, nombre in kwargs.items():
        print(f"Hola {nombre}, {posicion}!")

"""
print()
sumar(1)

print()
sumar(1, 25)
"""

def saludar(**kwargs):
    print(kwargs)


saludar(jugador_1="Bilbo", jugador_2="Frodo", jugador_3="Pippin")