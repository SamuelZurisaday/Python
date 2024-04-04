mi_lista = [1, ["Bilbo", "Gandalf", "Frodo"], "saruman", 99]

print("El mago blanco es: ", mi_lista[2])
print("El texto en mayuscula: ", mi_lista[2].capitalize())

print("El portador del anillo es: ", mi_lista[1][2])

mi_otra_lista = ["Harry", "Ron", "Hermione"]
print()
print(type(mi_otra_lista))

mi_tupla = tuple(mi_otra_lista)
print(type(mi_tupla), mi_tupla)