import math

figura = input("Figura (circulo, rectangulo, triangulo): ")

if figura == "circulo":
    r = float(input("Radio: "))
    print("Area:", math.pi * r * r)
elif figura == "rectangulo":
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Area:", b * h)
elif figura == "triangulo":
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Area:", b * h / 2)
else:
    print("Figura no valida")
