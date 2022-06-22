from ...combinatorics.combinations import binomial_coefficients, generate_combinations

import random
import unittest

class CombinationsTest(unittest.TestCase):

    def test_binomial_coefficients(self):
        self.assertEqual(binomial_coefficients(4, 2), 6)
        self.assertEqual(binomial_coefficients(7, 6), 7)

    def test_generate_combinations_against_binomial_coefficients(self):
        for i in range(50):
            n = random.randint(1, 20)
            m = random.randint(1, n)
            print("test %s: %sC%s" % (i, n, m))

            self.assertEqual(
                binomial_coefficients(n, m),
                len(list(generate_combinations(n, m)))
            )
