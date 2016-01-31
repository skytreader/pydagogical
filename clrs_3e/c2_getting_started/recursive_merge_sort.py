import math
import unittest

"""
Implementation of merge sort as in [CORMEN3], the only difference being that
this does not rely on sentinel data.
"""

def merge(numlist, start_index, mid_index, end_index):
    l1 = []
    l2 = []
    i = start_index

    while i <= mid_index:
        l1.append(numlist[i])
        i += 1

    while i <= end_index:
        l2.append(numlist[i])
        i += 1

    i = start_index

    while i <= end_index and len(l1) and len(l2):
        if l1[0] <= l2[0]:
            numlist[i] = l1.pop(0)
        else:
            numlist[i] = l2.pop(0)

        i += 1

    if len(l2) and not len(l1):
        while len(l2) and i <= end_index:
            numlist[i] = l2.pop(0)
            i += 1

    if len(l1) and not len(l2):
        while len(l1) and i <= end_index:
            numlist[i] = l1.pop(0)
            i += 1

def merge_sort_actual(numlist, start_index, end_index):
    if start_index == end_index:
        return
    else:
        midpoint = math.floor((start_index + end_index) / 2)
        merge_sort_actual(numlist, start_index, midpoint)
        merge_sort_actual(numlist, midpoint + 1, end_index)
        merge(numlist, start_index, midpoint, end_index)

def merge_sort(numlist):
    merge_sort_actual(numlist, 0, len(numlist) - 1)

class FunctionsTest(unittest.TestCase):
    
    def test_sort(self):
        one = [1]
        merge_sort(one)
        self.assertEqual(one, [1])
        pi = [1, 4, 1 ,5 ,9, 2]
        merge_sort(pi)
        self.assertEqual(pi, [1, 1, 2, 4, 5, 9])

if __name__ == "__main__":
    unittest.main()
