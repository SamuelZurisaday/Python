registro = {}

def registrar():
    usuario = input("Elegir para el registro un nombre de usuario: ")
    password = input("Elegir una contraseña: ")
    registro[usuario] = password

def loggear():
    max_intentos = 3
    usuario = input("Ingresar nombre de usuario: ")
    if usuario not in registro:
        print("Usuario no registrado.")
        return

    for intento in range(max_intentos, 0, -1):
        password = input("Ingresar contraseña: ")
        if password == registro[usuario]:
            print("Acceso Autorizado")
            break
        else:
            print(f"Contraseña Incorrecta. Intentos restantes: {intento - 1}")
            if intento == 1:
                print("Número de intentos excedido.")
                break

registrar()
print(registro)

loggear()