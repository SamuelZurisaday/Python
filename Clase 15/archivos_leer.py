ruta_archivo = "C:/Users/samue/Downloads/CODERHOUSE/Curso Python/Ejercicios/Clase 15/archivo.txt"

f = open(ruta_archivo, "r")
contenido = f.read()
f.close()

print(contenido)

f = open(ruta_archivo, "r")
contenido = f.readline()
print(contenido)
f.close()


f = open(ruta_archivo, "r")
contenido = f.readlines()
print(contenido)
f.close()
