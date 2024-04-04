intentos = 3
while intentos > 0:
    password = input("Di la palabra secreta amigo y entra: ")
    if password == "Mellon":
        print("La puerta esta abierta, bienvenido")
        break
    intentos -= 1
    print(f"Intentos restates: {intentos}")
    print()
else:
    print("Usuario Bloqueado")