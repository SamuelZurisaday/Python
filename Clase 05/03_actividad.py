nombre = input("Ingresar nombre: ")
edad = int(input("Ingresar edad: "))

print(f"Has ingresado: {nombre} - {edad}")

mi_variable_booleana = (
    nombre != "****"
    and edad > 5
    and edad < 20
    and len(nombre) >= 4
    and len(nombre) < 8
)

print(f"Mi variable booleana es:  {mi_variable_booleana}")