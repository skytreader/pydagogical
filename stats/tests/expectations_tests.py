import unittest

from stats.expectation import expected_value

class FunctionsTests(unittest.TestCase):

    def test_expected_value(self):
        val_table = (
            (-2, 23, 48, 73, 98),
            (0.977, 0.008, 0.008, 0.006, 0.001)
        )
        self.assertAlmostEqual(-0.85, expected_value(val_table))
