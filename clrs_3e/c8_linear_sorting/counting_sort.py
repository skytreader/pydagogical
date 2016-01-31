#! /usr/bin/env python3

import unittest

"""
Algorithm description (from CORMEN):

Counting sort assumes that each of the n input elements is an integer in the
range 0 to k, for some integer k. When k = O(n), the sort runs in \Theta(n) time.

Counting sort determines, for each input element x, the number of elements less
than x. It uses this information to place element x directly into its position in the
output array. For example, if 17 elements are less than x, then x belongs in
output position 18.
"""

def counting_sort(numlist, range_upper_bound):
    """
    Sorts the integers in numlist provided that all numbers in numlist are in
    the range 0 to range_upper_bound.

    Returns the sorted list.
    """
    limit = len(numlist)
    limit_range = range(limit)
    sorted_list = [None for i in limit_range]
    count_list = [0 for i in range(range_upper_bound + 1)]
    
    # "Count" the number of entries equal to numlist[i]
    for i in limit_range:
        count_list[numlist[i]] += 1

    i = 1

    # Increment by the number of items less than numlist[i]
    # Increment limit by 1 due to indexing concerns
    while i < (range_upper_bound + 1):
        count_list[i] += count_list[i - 1]
        i += 1

    i = limit - 1

    # The position of numlist[i] in sorted_list will be its count (minus 1 for
    # index adjustment). Decrement its count afterwards to handle multiple
    # instances of the same number.
    while i >= 0:
        sorted_list[count_list[numlist[i]] - 1] = numlist[i]
        count_list[numlist[i]] -= 1
        i -= 1

    return sorted_list

class FunctionsTest(unittest.TestCase):
    
    def test_counting_sort(self):
        open_ends_unique = [5, 3, 7, 1, 4, 2, 8, 6]
        open_ends_unique_sorted = [1, 2, 3, 4, 5, 6, 7, 8]

        zero_open_unique = [5, 3, 7, 1, 4, 9, 2, 8, 6]
        zero_open_unique_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        nine_open_unique = [5, 3, 7, 1, 4, 2, 0, 8, 6]
        nine_open_unique_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        zero_open_repeating = [5, 3, 4, 7, 1, 9, 4, 2, 3, 8, 1, 6]
        zero_open_repeating_sorted = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]

        nine_open_repeating = [5, 1, 3, 7, 1, 3, 4, 2, 0, 4, 8, 6]
        nine_open_repeating_sorted = [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 8]

        pi_test = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
            6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9]
        pi_sorted = [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4,
            4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9]

        self.assertEqual(counting_sort(open_ends_unique, 9), open_ends_unique_sorted)
        self.assertEqual(counting_sort(zero_open_unique, 9), zero_open_unique_sorted)
        self.assertEqual(counting_sort(nine_open_unique, 9), nine_open_unique_sorted)
        self.assertEqual(counting_sort(zero_open_repeating, 9), zero_open_repeating_sorted)
        self.assertEqual(counting_sort(nine_open_repeating, 9), nine_open_repeating_sorted)
        self.assertEqual(counting_sort(pi_test, 9), pi_sorted)

if __name__ == "__main__":
    unittest.main()
