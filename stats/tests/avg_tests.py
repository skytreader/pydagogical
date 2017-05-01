import math
import unittest

from stats.avg import mean, variance, standard_deviation

class FunctionsTests(unittest.TestCase):
    
    def test_mean(self):
        self.assertAlmostEqual(2.5, mean((1, 2, 3, 4)))

    def test_variance(self):
        self.assertAlmostEqual(1.25, variance((1, 2, 3, 4)))

    def test_std_deviation(self):
        self.assertAlmostEqual(math.sqrt(variance((1, 2, 3, 4))), standard_deviation((1, 2, 3, 4)))
