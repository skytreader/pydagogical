from ..binary_search import binary_search, binary_insert

import unittest


class FunctionsTest(unittest.TestCase):
    
    def test_binary_search(self):
        """
        Test cases:
        even-length list positive result
        even-length list negative result
        odd-length list positive result
        odd-length list negative result
        """
        pi_list = [1,4,1,5,9,9,6,5,3,5,8,9,7,9,3,2,3,5,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9]
        pi_list.sort()
        
        for i in range(10):
            positive_even = binary_search(pi_list, i)
            self.assertTrue(positive_even >= 0)
            self.assertEqual(pi_list[positive_even], i)
        
        negative_even = binary_search(pi_list, 42)
        self.assertEqual(negative_even, -1)

        odd_list = pi_list[0:len(pi_list) - 1]
        positive_odd = binary_search(odd_list, 5)
        self.assertTrue(positive_odd > 0)
        self.assertEqual(odd_list[positive_odd], 5)

        negative_odd = binary_search(odd_list, 34)
        self.assertEqual(negative_odd, -1)

        loner = binary_search([1], 1)
        self.assertEqual(loner, 0)

        self.assertTrue(binary_search([], 1) < 0)

        couple = [1, 2]
        self.assertEqual(binary_search(couple, 1), 0)
        self.assertEqual(binary_search(couple, 2), 1)

    def test_binary_insert(self):
        """
        """
        # Base cases
        self.assertEqual(binary_insert([1, 3], 2), [1, 2, 3])
        self.assertEqual(binary_insert([2], 1), [1, 2])
        self.assertEqual(binary_insert([1], 2), [1, 2])
        self.assertEqual(binary_insert([1, 1], 2), [1, 1, 2])
        self.assertEqual(binary_insert([2, 2], 1), [1, 2, 2])
        
        heavy_test = [2, 4, 5, 7, 9]
        self.assertEqual(binary_insert(heavy_test, 1), [1, 2, 4, 5, 7, 9])
        self.assertEqual(binary_insert(heavy_test, 2), [2, 2, 4, 5, 7, 9])
        self.assertEqual(binary_insert(heavy_test, 6), [2, 4, 5, 6, 7, 9])
        self.assertEqual(binary_insert(heavy_test, 10), [2, 4, 5, 7, 9, 10])

        self.assertEqual(binary_insert([], 1), [1])
