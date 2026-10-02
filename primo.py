import math


def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, math.isqrt(numero) + 1):
        if numero % divisor == 0:
            return False
    return True