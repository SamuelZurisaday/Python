max_intentos = 3  # Mejor práctica: usar nombres de variables descriptivos
# Permite cambiar fácilmente la palabra secreta sin modificar la lógica del programa
palabra_secreta = "Mellon"

# Utiliza un bucle for con range para controlar el número de intentos
for intento in range(max_intentos, 0, -1):
    password = input("Di la palabra secreta amigo y entra: ")
    if password == palabra_secreta:
        print("La puerta está abierta, bienvenido")
        break
    else:
        print(f"Intentos restantes: {intento - 1}")
        if intento > 1:  # Solo muestra la línea en blanco si no es el último intento
            print()

# Este 'else' pertenece al bucle for y se ejecuta solo si el bucle no se rompe (es decir, si se agotan los intentos)
else:
    print("Has agotado todos tus intentos.")