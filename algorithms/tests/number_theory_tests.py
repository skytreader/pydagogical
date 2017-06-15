import unittest

from ..number_theory import pulverize, gcd
import fractions

class FunctionsTest(unittest.TestCase):
    
    def test_pulverize(self):
        self.assertEqual((3, -11), pulverize(259, 70))

    def test_gcd(self):
        self.assertEqual(fractions.gcd(5, 3), gcd(5, 3))
        self.assertEqual(fractions.gcd(3, 5), gcd(3, 5))
        self.assertEqual(fractions.gcd(258, 147), gcd(258, 147))
        self.assertEqual(fractions.gcd(147, 258), gcd(147, 258))
