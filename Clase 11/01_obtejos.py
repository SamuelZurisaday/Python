class Triangulo:

    def __init__(self, base, altura, lado_extra):
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    def obtener_superficie(self):
        superficie = (self.base * self.altura) / 2
        return superficie

    def __str__(self):
        return f"Triangulo: {self.base}, {self.altura}, {self.lado_extra}. Superficie: {self.obtener_superficie()}"


xx = Triangulo(3, 4, 5)
yy = Triangulo(4, 7, 20)
ww = Triangulo(41, 79, 250)
zz = Triangulo(45, 67, 520)

print(xx, yy, ww, zz)

# Codigo mejorado y comentado


class Triangulo:
    def __init__(self, base: float, altura: float, lado_extra: float):
        """
        Inicializa un objeto de la clase Triangulo.

        :param base: longitud de la base del triángulo
        :param altura: altura del triángulo
        :param lado_extra: longitud de un lado adicional del triángulo
        """
        if base <= 0 or altura <= 0 or lado_extra <= 0:
            raise ValueError(
                "La base, altura y lado extra deben ser mayores que 0")
        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra

    @property
    def superficie(self) -> float:
        """
        Calcula y retorna la superficie del triángulo.

        :return: superficie del triángulo
        """
        return (self.base * self.altura) / 2

    def __str__(self) -> str:
        """
        Representación en string del objeto Triangulo.

        :return: representación en string del triángulo
        """
        return f"Triángulo con base {self.base}, altura {self.altura}, " \
               f"lado extra {self.lado_extra}. Superficie: {self.superficie}"


# Creación de instancias y pruebas
xx = Triangulo(3, 4, 5)
yy = Triangulo(4, 7, 20)
ww = Triangulo(41, 79, 250)
zz = Triangulo(45, 67, 520)

print(xx, yy, ww, zz)
