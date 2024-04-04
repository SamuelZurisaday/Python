"""

Calculo de Area:
Triangulo: (b * a) / 2
Rectangulo: b * a
Trapecio: (base mayor + base menor) * altura / 2

Calculo de Perimetro:
Triangulo: a + b + c
Rectangulo: 2 * base + 2 * altura
Trapecio: a + b + c + d

"""

triangulo = {
    "lado1": 3,
    "lado2": 4,
    "lado3": 5
}


def calcular_superficie(triangulo):
    return (triangulo["lado1"] * triangulo["lado2"]/2)


print(calcular_superficie(triangulo))