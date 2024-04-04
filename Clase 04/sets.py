lista_funciones_ejecutadas = ["print", "print",
                              "print", "print", "type", "type", "len"]
conjunto_de_funciones_ejecutadas = set(
    ["print", "print", "print", "print", "type", "type", "len"])
# conjunto_de_funciones_ejecutadas = {"print", "print", "print", "print", "type", "type", "len"}

lista = [1, 1, 1, 1, 1, 1, 2, 2, 3]
conjunto = {1, 1, 1, 1, 1, 1, 2, 2, 3}

print()
print("Lista ", lista_funciones_ejecutadas)
print("Conjunto", conjunto_de_funciones_ejecutadas)
print()
print("Lista ", lista)
print("Conjunto", conjunto)

# Agregar
conjunto.add(6)
conjunto.add(7)
conjunto.add(8)
conjunto.update(["Frodo", "Sam", "Pippin", "Merry"])
conjunto.add("Frodo")
print("Conjunto", conjunto)
print()

# Remover
conjunto.remove(7)
print("2 -> ", "Removi", conjunto)
print()

# Longitud
print("3 -> ", "Longitud", len(conjunto))
print()

# Descartar
conjunto.discard("Gandalf")
conjunto.discard(1)
print("4 -> ", "Descartar", conjunto)
print()