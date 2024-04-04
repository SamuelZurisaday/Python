class Cuadrilatero:

    def __init__(self, lado1, lado2, lado3, lado4):
        self.l1 = lado1
        self.l2 = lado2
        self.l3 = lado3
        self.l4 = lado4

    def __str__(self):
        return f"Soy un cuadrilatero: {self.l1}, {self.l2}, {self.l3}, {self.l4}"

    def calcular_perimetro(self):
        return self.l1 + self.l2 + self.l3 + self.l4


class Rectangulo(Cuadrilatero):  # 1

    def __init__(self, base, altura):
        super().__init__(base, base, altura, altura)  # 2
        self.base = base
        self.altura = altura
        self.area = self.obtener_superficie()

    def obtener_superficie(self):
        superficie = (self.base * self.altura)
        return superficie

    def __str__(self):
        return f"Rectangulo: {self.base}, {self.altura} "

    def __len__(self):
        return self.calcular_perimetro()


xx = Rectangulo(3, 4)
yy = Cuadrilatero(3, 3, 4, 4)
print(xx.obtener_superficie())
print(yy.calcular_perimetro())
print(len(xx))