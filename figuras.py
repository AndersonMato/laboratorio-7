import math


def area_circulo(radio):
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


def pedir_numero(mensaje):
    return float(input(mensaje))


def main():
    figura = input("Figura (circulo, rectangulo, triangulo): ").strip().lower()

    if figura == "circulo":
        area = area_circulo(pedir_numero("Radio: "))
    elif figura in ("rectangulo", "triangulo"):
        base = pedir_numero("Base: ")
        altura = pedir_numero("Altura: ")
        if figura == "rectangulo":
            area = area_rectangulo(base, altura)
        else:
            area = area_triangulo(base, altura)
    else:
        print("Figura no valida")
        return

    print(f"Area: {area:.2f}")


if __name__ == "__main__":
    main()
