"""
Descripción de la actividad

1. Para aprobar un credito, el cliente debe ser mayor de edad.
2. Además, debe de tener antiguedad en el sistema de minimo 3 años.
    un ingreso mayor a 2,500 dolares
3. En caso que no tenga la antiguedad suficiente, su ingreso
    debe de ser como minimo, 4,000 dolares.
4. Si no cumple con ninguna de las condiciones, mno se aprueba el credito.
"""

edad = 70
antiguedad = 10
ingreso = 1500

if edad >= 18:
    if antiguedad >= 3:
        print("Credito Aprobado")
else:
    print("Credito No Aprobado")
