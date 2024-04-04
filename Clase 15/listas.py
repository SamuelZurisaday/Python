import json

mi_lista = ["Magenta", "Riff Raff", "Columbia", "Rocky", 4, 5, True]

f = open("personaje.txt", "w")
lista_convertida_a_json = json.dumps(mi_lista)
f.write(lista_convertida_a_json)

f.close()

f = open("personajes.txt", "r")
contenido = f.read()
f.close()

print(contenido)
print(list(contenido))