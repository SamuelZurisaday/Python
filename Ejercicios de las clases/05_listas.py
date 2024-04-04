mi_lista = ["a", "b", "a", "a", "b"]

#Contar ocurrencias
ocurrencias = mi_lista.count("a")
print("La letra 'a' aparece", ocurrencias, " veces")
ocurrencias = mi_lista.count("b")
print("La letra 'b' aparece", ocurrencias, " veces")
ocurrencias = mi_lista.count("c")
print("La letra 'c' aparece", ocurrencias, " veces")

print("La letra 'c' aparece", mi_lista.count("c"), " veces")

#Averiguar en que posición está el elemento
posicion = mi_lista.index("a")
print("La letra 'a' esta en la posicion", posicion)
posicion = mi_lista.index("b")
print("La letra 'b' esta en la posicion", posicion)
