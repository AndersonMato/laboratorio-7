import unittest
from primo import es_primo


class TestEsPrimo(unittest.TestCase):
    def test_numeros_primos(self):
        for numero in (2, 3, 5, 7, 11, 13, 97):
            self.assertTrue(es_primo(numero), f"{numero} deberia ser primo")

    def test_numeros_no_primos(self):
        for numero in (4, 6, 9, 15, 100):
            self.assertFalse(es_primo(numero), f"{numero} no deberia ser primo")

    def test_casos_limite(self):
        for numero in (-5, 0, 1):
            self.assertFalse(es_primo(numero), f"{numero} no deberia ser primo")


if __name__ == "__main__":
    unittest.main()