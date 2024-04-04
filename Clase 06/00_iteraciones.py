def prueba(calificacion):
    # Convertir calificacion a entero, en caso de que no lo sea.
    calificacion = int(calificacion)

    # Verificar si la calificación es suficiente para superar la prueba.
    if calificacion >= 6:
        print("Prueba superada")
    else:
        print("Prueba no superada")

# Solicitar al usuario que ingrese una calificación
calificacion_usuario = input("Ingresa la calificación: ")

# Llamar a la función prueba con la calificación ingresada por el usuario
prueba(calificacion_usuario)