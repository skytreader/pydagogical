#! /usr/bin/env python3

import math
import unittest

"""
Python port of maximum subarray problem in _Introduction to Algorithms 3e_. This
uses divide and conquer techniques. Can be found in Chpater 4 Section 1 of the
book.

Running time is O(n lg(n)). I think I can do this faster at O(n) with dynamic
programming.

@author Chad Estioco
"""

SUBARRAY_START_INDEX = 0
SUBARRAY_END_INDEX = 1
SUBARRAY_SUM_INDEX = 2

def find_max_crossing_subarray(a, low, mid, high):
    """
    Parameter assumptions:
    a - the array
    low - the lowest index in the subarray we are considering (inclusive)
    mid - the midpoint. The subarray described by the returned tuple must cross
          this index.
    high - the highest index in the subarray we are considering (exclusive)

    Returns a tuple with three elements containing the index where the crossing
    subarray starts (inclusive), the index where the crossing subarray ends
    (exclusive), and the total sum of the crossing subarray, in that order.
    """
    print("find_max_crossing_subarray call with params: " + str((a, low, mid, high)))
    max_left_sum = float("-inf")
    left_sum = 0
    max_left_index = mid
    i = mid

    while i >= low:
        left_sum += a[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum
            max_left_index = i

        i -= 1

    print("For " + str((a, low, mid, high)))
    print("Left max: " + str((low, max_left_index, max_left_sum)))

    max_right_sum = float("-inf")
    right_sum = 0
    max_right_index = mid + 1
    i = mid + 1

    while i < high:
        right_sum += a[i]
        if right_sum > max_right_sum:
            max_right_sum = right_sum
            max_right_index = i

        i += 1

    print("Right max: " + str((max_right_index, high, max_right_sum)))

    return (max_left_index, max_right_index + 1, max_left_sum + max_right_sum)

def find_maximum_subarray(a, low, high):
    """
    Recursive (read: straight-from-the-book) implementation of the divide and
    conquer algorithm.
    
    Returns a tuple with three elements containing the index where the max
    subarray starts (inclusive), the index where the max subarray ends
    (exclusive), and the sum over the specified subarray, in that order.
    """

    if high == (low + 1):
        return (low, high, a[low])
    elif high == (low + 2):
        #print("For call: " + str((a, low, high)))
        #print("Return: " + str((low, high, a[low])))
        #return (low, high, a[low])
        print("Array length: " + str(len(a)))
        print("indices: " + str((low, high)))
        possibilities = ((low, low + 1, a[low]), (high - 1, high, a[high - 1]),
            (low, high, a[low] + a[high - 1]))

        max_possible = max((a[low], a[high - 1], a[low] + a[high - 1]))

        if max_possible == a[low]:
            return possibilities[0]
        elif max_possible == a[high - 1]:
            return possibilities[1]
        else:
            return possibilities[2]
    else:
        midpoint = math.floor((low + high) / 2)
        print("Midpoint: " + str(midpoint))

        # find the maximum subarray in the left of the midpoint
        lefties = find_maximum_subarray(a, low, midpoint)
        # find the maximum subarray in the right of the midpoint
        righties = find_maximum_subarray(a, midpoint, high)
        # find the maximum subarray crossing the midpoint
        crossing = find_max_crossing_subarray(a, low, midpoint, high)

        maximum_sum = max(lefties[SUBARRAY_SUM_INDEX], righties[SUBARRAY_SUM_INDEX],
            crossing[SUBARRAY_SUM_INDEX])

        print("Max between: " + str((lefties[SUBARRAY_SUM_INDEX], righties[SUBARRAY_SUM_INDEX], crossing[SUBARRAY_SUM_INDEX])))

        if maximum_sum == lefties[SUBARRAY_SUM_INDEX]:
            #print("For call: " + str((a, low, high)))
            #print("Return: " + str(lefties))
            return lefties
        elif maximum_sum == righties[SUBARRAY_SUM_INDEX]:
            #print("For call: " + str((a, low, high)))
            #print("Return: " + str(righties))
            return righties
        else:
            #print("For call: " + str((a, low, high)))
            #print("Return: " + str(crossing))
            return crossing

def find_max_subarray(a):
    """
    Driver function for find_maximum_subarray.
    """
    return find_maximum_subarray(a, 0, len(a))

def brute_max_subarray(a):
    """
    Brute-force O(n^2) method for finding the max subaray: consider all possible
    subarrays.
    """
    prev_sums = []
    start_index = 0
    limit = len(a)
    maxsum = float("-inf")
    maxstart = -1
    maxend = -1

    while start_index < limit:
        i = start_index
        current_sums = []

        while i < limit:
            sumr = 0
            if start_index == 0:
                sumr = sum(a[start_index:i+1])
                current_sums.append(sumr)
            else:
                sumr = prev_sums[i - start_index + 1] - a[start_index - 1]
                current_sums.append(sumr)
            
            if sumr > maxsum:
                maxsum = sumr
                maxstart = start_index
                maxend = i + 1

            i += 1

        prev_sums = current_sums
        start_index += 1

    return (maxstart, maxend, maxsum)

class FunctionsTest(unittest.TestCase):
    
    def setUp(self):
        self.tests = ((13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7),
        (5, 15, -30, 10, -5, 40, 10), (-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5,
        -8, -9, -7, -9, -3, -2, -3, -8, -4, -6), (5, 15, -30))

        self.expected_results = ((7, 11, 43), (3, 7, 55), (1, 2, -1), (0, 2, 20))

    def test_brute_force(self):
        for (test, result) in zip(self.tests, self.expected_results):
            self.assertEqual(brute_max_subarray(test), result)

    def test_divide_and_conquer(self):
        for (test, result) in zip(self.tests, self.expected_results):
            self.assertEqual(find_max_subarray(test), result)

if __name__ == "__main__":
    unittest.main()
