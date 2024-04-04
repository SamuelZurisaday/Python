ruta_archivo = "C:/Users/samue/Downloads/CODERHOUSE/Curso Python/Ejercicios/Clase 15/archivo.txt"

f = open(ruta_archivo, "r")
contenido = f.readline()
print(contenido)
f.close()
print()


f = open(ruta_archivo, "r")
f.seek(3)
contenido = f.readline()
print(contenido)
f.close()
print()