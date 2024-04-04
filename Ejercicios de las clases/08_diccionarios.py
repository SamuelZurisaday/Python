agenda = {}
agenda["Frodo"] = 222
agenda["Drogo"] = 333

print("Agenda inicial", agenda)

nombre = input("Ingresar nombre del contacto: ")
numero = input("Ingresar numero telefonico: ")

agenda[nombre] = numero

print("Agenda actualizada", agenda)

contacto_para_buscar = input("Ingresar nombre del contacto para buscar: ")
telefono = agenda[contacto_para_buscar]

print("El telefono de tu contacto es: ", telefono)
print(f"El telefono de {contacto_para_buscar} es: {telefono}")