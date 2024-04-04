mi_lista = [1, 5, 6, 7, "Frodo", "Sam", "Merry"]

#Imprimir Frodo
print(mi_lista[4])

print("La longitud de la lista es: ", len(mi_lista))
print("La longitud del nombre Frodo es: ", len(mi_lista[4]))

#Reemplazar un elemento
mi_lista[3] = "Gandalf"
print("La nueva lista es: ", mi_lista)

#Reemplazar de a rebanadas (slices)
mi_lista[:2] = ["Aragorn", "Boromir"]
print("La nueva lista es: ", mi_lista)

#Concatenar otra lista
mi_otra_lista = ["Legolas", "Gimli"]
mi_lista = mi_lista + mi_otra_lista
print("La nueva lista es: ", mi_lista)

#Agregar 1 elemento
elemento = "Pippin"
mi_lista.append(elemento)
print("La nueva lista es: ", mi_lista)

#Remover 1 elemento

del mi_lista[2]
print("La nueva lista es: ", mi_lista)

#Agregar 1 elemento
elemento = "Luke Skywalker"
mi_lista.append(elemento)
print("La nueva lista es: ", mi_lista)

#Extraer el último elemento
mi_personaje = mi_lista.pop()
print("La nueva lista es: ", mi_lista)
print("El personaje extraido es: ", mi_personaje)

