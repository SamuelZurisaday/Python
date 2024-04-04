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
# definimos una variable triangulo con una base de 3, altura de 4 y otro lado de 5
class Triangulo:

    def __init__(self, base=3, altura=4, lado_extra=5):
        print("----- creacion -----")
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    def obtener_superficie(self):
        print("----- superficie -----")
        superficie = (self.base * self.altura) / 2
        return superficie

# Construir un triangulo de lados 3, 4 y 5, cuya base es 4 y su altura 3
print("1")
xx = Triangulo(base=4, altura=3, lado_extra=5)
print("2")
print(f"La base del triangulo es: {xx.base} y su altura es: {xx.altura}")
print(
    f"La base del triangulo es: {xx.base} y su altura es: {xx.altura} y tiene un lado extra que mide {xx.lado_extra}")
print(
    f"La base del triangulo es: {xx.base} y su altura es: {xx.altura} y su superficie es: {xx.obtener_superficie()}")