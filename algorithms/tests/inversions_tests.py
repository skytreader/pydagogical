from ..inversions import naive_inversion_count, merge_inversion_count

import unittest

class FunctionsTest(unittest.TestCase):
    
    def test_naive(self):
        self.assertEqual(5, naive_inversion_count([2, 3, 8, 6, 1]))
        self.assertEqual(5, naive_inversion_count([1, 4, 1, 5, 9, 2, 6]))
        self.assertEqual(6, naive_inversion_count([4, 1, 5, 2, 6, 3]))
        self.assertEqual(60, naive_inversion_count((0,15,14,1,13,2,3,12,11,4,5,10,6,9,8,7)))

    def test_merge_inversion_count(self):
        self.assertEqual(5, merge_inversion_count([2, 3, 8, 6, 1]))
        self.assertEqual(5, merge_inversion_count([1, 4, 1, 5, 9, 2, 6]))
        self.assertEqual(6, merge_inversion_count([4, 1, 5, 2, 6, 3]))
        self.assertEqual(60, merge_inversion_count((0,15,14,1,13,2,3,12,11,4,5,10,6,9,8,7)))
        self.assertEqual(0, merge_inversion_count([]))
        self.assertEqual(0, merge_inversion_count([1]))
        self.assertEqual(0, merge_inversion_count([1, 2, 3]))

        spam = [2, 3, 8, 6, 1]
        self.assertEqual(5, merge_inversion_count(spam))
        self.assertEqual([2, 3, 8, 6, 1], spam)
