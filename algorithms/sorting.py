#! /usr/bin/env python3
import unittest
"""
Some "exotic" sorts. Will sooner or later deprecate some scripts in clrs_3e.

Will not optimize for anything other than asymptotic time.
"""

def flipsort(numlist):
    """
    This is basically just bubble sort but with the added caveat that "bubbling"
    the biggest element leftwards affects not just the biggest element but those
    in between.

    On the surface, it seems to me that the running time is the same as as bubble
    sort (O(n^2)) but the nature of the adversarial input for this algorithm
    might be different.

    Returns the list sorted in ascending order.
    """
    def flip(i):
        """
        flip the first $i$ elements of numlist. Returns the list.
        """
        sublist = numlist[0:i]
        sublist.reverse()
        sublist.extend(numlist[i:len(numlist)])
        return sublist

    for i in range(len(numlist), 0, -1):
        max_item = max(numlist[0:i])
        max_item_index = numlist.index(max_item)
        
        numlist = flip(max_item_index + 1)
        numlist = flip(i)

    return numlist

class FunctionsTest(unittest.TestCase):
    
    def test_flipsort(self):
        small_pi_test = [3, 1, 4, 1]
        small_pi_sorted = sorted(small_pi_test)
        self.assertEqual(small_pi_sorted, flipsort(small_pi_test))

        pi_test = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
            6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9]
        pi_sorted = sorted(pi_test)
        self.assertEqual(pi_sorted, flipsort(pi_test))

if __name__ == "__main__":
    unittest.main()
