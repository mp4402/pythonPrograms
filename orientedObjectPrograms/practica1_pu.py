import unittest

class PruebaUnitaria(unittest.TestCase):
    def test_validar_resultado(self):
        numero = int(input("Ingrese un número para el límite de la sumatoria: "))
        control = 1
        total = 0
        array = []
        while (control <= numero):
            total += control
            array.append(control)
            control+=1
        self.assertEqual(total, sum(array))

if __name__ == '__main__':
    unittest.main()