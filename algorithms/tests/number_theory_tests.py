import unittest

from ..number_theory import pulverize

class FunctionsTest(unittest.TestCase):
    
    def test_pulverize(self):
        self.assertEqual((3, -11), pulverize(259, 70))
