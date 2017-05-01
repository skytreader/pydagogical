import unittest

from stats import expectation as exp

class FunctionsTests(unittest.TestCase):

    def test_cardinality_check(self):
        val_table = (
            (-2, 23, 48, 73),
            (0.977, 0.008, 0.008, 0.006, 0.001)
        )
        self.assertRaises(
            ValueError,
            exp._cardinality_check,
            val_table[0],
            val_table[1]
        )

    def test_expected_value(self):
        val_table = (
            (-2, 23, 48, 73, 98),
            (0.977, 0.008, 0.008, 0.006, 0.001)
        )
        self.assertAlmostEqual(-0.85, exp.expected_value(val_table[0], val_table[1]))
