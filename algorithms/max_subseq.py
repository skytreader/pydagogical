#! /usr/bin/env python3

import unittest

"""
An O(n lg n) solution to the maximum sequence subarray problem
(taken from [CORMEN3e]).
"""

def find_max_crossing_subarray(numseq, low, mid, high):
    """
    Find the maximum subarray crossing the midpoint. The halves
    of the array are defined as [0, midpoint] to [midpoint + 1, len(numseq) - 1].

    Returns a tuple containing the index of the start of the
    crossing subarray (which is at the first half) and the
    end index (which is at the second half) and then the sum
    over that subarray.
    """
    left_side = find_biased_max(numseq, mid, low)
    right_side = find_biased_max(numseq, mid + 1, high)

    return (left_side[0], right_side[0], left_side[1] + right_side[1])

def find_biased_max(numseq, origin_index, dest_index):
    """
    Find the maximum subarray that starts at origin_index
    and ends towards (but not always exactly on) dest_index.

    Returns a tuple containing the index where the biased
    maximum subarray _ends_ and the total sum over that
    array, in that order.
    """
    updater = (lambda x: x + 1) if origin_index < dest_index else (lambda x: x - 1)

    i = origin_index
    limit = updater(dest_index)
    max_end_index = i - 1 if origin_index < dest_index else i + 1
    max_sum = float("-inf")
    run_sum = 0

    while i != limit:
        run_sum += numseq[i]
        
        if run_sum > max_sum:
            max_sum = run_sum
            max_end_index = i
        
        i = updater(i)

    return (max_end_index, max_sum)

def find_max_on(sequence, max_criteria):
    """
    Returns the item in the sequence which is maximum based
    on the given criteria. max_criteria must be a function
    that gets the "comparison point" for an item in sequence.
    This comparison point must be comparable to all the other
    comparison points in the sequence.
    """
    max_val = max_criteria(sequence[0])
    max_item = sequence[0]

    for item in sequence:
        to_compare = max_criteria(item)

        if to_compare > max_val:
            max_val = to_compare
            max_item = item
    
    return max_item

def find_max_subarray(numseq, low, high):
    """
    Recursive function (hence the method signature). low
    and high are indices.

    Returns a tuple containing the start index of the max
    subarray, the end index of the max subarray, and the
    sum over that subarray, in that order.

    Challenge: Write an iterative version.
    """
    if low == high: # Base case: we need to consider only one element
        return (low, high, numseq[low])
    elif low == (high - 1): # Another base case: sequence has only two elements
        # Deviation from CORMEN. Consider the case when low = 0, high = 1.
        # Left recursion will terminate with low = 0, high = 0 but right
        # recursion will loop indefinitely with low = 0, high = 1. FIXME
        possible_max = numseq[low] + numseq[high]

        if possible_max < numseq[low] and numseq[low] > numseq[high]:
            return (low, low, numseq[low])
        elif possible_max < numseq[high] and numseq[high] > numseq[low]:
            return (high, high, numseq[high])
        else:
            return (low, high, possible_max)
    else:
        # Determine the midpoint.
        midpoint = int((low + high) / 2)
        
        # Get the max subarray of the left side
        lmax = find_max_subarray(numseq, low, midpoint)

        # Get the max subaray of the right side
        rmax = find_max_subarray(numseq, midpoint + 1, high)

        # Get the maximum crossing subarray
        cmax = find_max_crossing_subarray(numseq, low, midpoint, high)
        
        max_criteria = lambda x: x[2]
        return find_max_on((lmax, rmax, cmax), max_criteria)

def max_subarray(numseq):
    """Driver method. Call this not find_max_subarray"""
    return find_max_subarray(numseq, 0, len(numseq) - 1)

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

if __name__ == "__main__":
    unittest.main()
