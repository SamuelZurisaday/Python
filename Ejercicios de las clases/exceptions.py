def dividir(a, b):
    try:
        resultado = a / b
        print("El resultado es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

dividir(10, 2)  # Esto funcionará sin problemas
dividir(10, 0)  # Esto generará una excepción que será manejada por el bloque except