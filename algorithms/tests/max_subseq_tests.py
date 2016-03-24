from ..max_subseq import max_subarray, max_subarray_dp, find_biased_max

import unittest

class FunctionsTest(unittest.TestCase):
    
    def test_find_biased_max(self):
        self.assertEqual((6, 45), find_biased_max((5, 15, -30, 10, -5, 40, 10), 4, 6))

    def test_max_subarray(self):
        self.assertEqual((0, 1, 20), max_subarray((5, 15, -30, 10)))
        # The example from the book
        stocks = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        self.assertEqual((7, 10, 43), max_subarray(stocks))
        self.assertEqual((0, 1, 10), max_subarray((7, 3)))
        self.assertEqual((1, 1, 10), max_subarray((-10, 10)))
        self.assertEqual((0, 0, 10), max_subarray((10, -10)))
        self.assertEqual((0, 0, 10), max_subarray([10]))
        self.assertEqual((1, 2, 50), max_subarray((-5, 40, 10)))
        self.assertEqual((0, 0, -10), max_subarray([-10]))
        self.assertEqual((3, 6, 55), max_subarray((5, 15, -30, 10, -5, 40, 10)))

    def test_max_subarray_dp(self):
        self.assertEqual((0, 1, 20), max_subarray((5, 15, -30, 10)))
        # The example from the book
        stocks = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        self.assertEqual((7, 10, 43), max_subarray_dp(stocks))
        self.assertEqual((0, 1, 10), max_subarray_dp((7, 3)))
        self.assertEqual((1, 1, 10), max_subarray_dp((-10, 10)))
        self.assertEqual((0, 0, 10), max_subarray_dp((10, -10)))
        self.assertEqual((0, 0, 10), max_subarray_dp([10]))
        self.assertEqual((1, 2, 50), max_subarray_dp((-5, 40, 10)))
        self.assertEqual((0, 0, -10), max_subarray_dp([-10]))
        self.assertEqual((3, 6, 55), max_subarray_dp((5, 15, -30, 10, -5, 40, 10)))
