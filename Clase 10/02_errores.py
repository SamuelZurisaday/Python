def consultar_elemento_en_diccionario(xx, clave):
    return xx[clave]

a = {
    1: 2,
    "tres": "tortillas de patatas"
    }
b = "tres"
resultado = consultar_elemento_en_diccionario(a, b)
print(resultado)

print()
print(" ----> Programa ejecutado con exito <----")
print()