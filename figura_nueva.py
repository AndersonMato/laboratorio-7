import math

from figuras_solid import Figura, CalculadoraAreas, Presentador


class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2


class Elipse(Figura):
    def __init__(self, semieje_a, semieje_b):
        self.semieje_a = semieje_a
        self.semieje_b = semieje_b

    def area(self):
        return math.pi * self.semieje_a * self.semieje_b


if __name__ == "__main__":
    calculadora = CalculadoraAreas()
    presentador = Presentador()

    figuras = [Trapecio(6, 4, 3), Elipse(5, 2)]
    for figura in figuras:
        presentador.mostrar(type(figura).__name__, calculadora.calcular(figura))