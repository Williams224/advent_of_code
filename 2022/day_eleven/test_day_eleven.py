from .day_eleven import modular_add, modular_exponent, modular_multiply
import unittest


class testModular(unittest.TestCase):
    def testArithmatic(self):
        starting_vals = [73, 37, 45, 11, 13, 17]
        mod = 7
        adds = [5, 4, 5, 6, 8, 9]

        self.assertEqual(modular_add(mod, starting_vals[0] % mod, adds[0]), 1)

        self.assertEqual(modular_multiply(mod, starting_vals[1] % mod, adds[1]), 1)

        self.assertEqual(modular_multiply(mod, starting_vals[2], adds[2]), 1)
