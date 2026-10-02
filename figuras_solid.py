import math
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


class CalculadoraAreas:
    def calcular(self, figura):
        return figura.area()

    def total(self, figuras):
        return sum(figura.area() for figura in figuras)


class Presentador:
    def mostrar(self, nombre, area):
        print(f"{nombre}: {area:.2f}")


if __name__ == "__main__":
    calculadora = CalculadoraAreas()
    presentador = Presentador()

    figuras = [Circulo(3), Rectangulo(4, 5), Triangulo(6, 2)]
    for figura in figuras:
        presentador.mostrar(type(figura).__name__, calculadora.calcular(figura))