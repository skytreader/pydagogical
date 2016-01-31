import math
import unittest

def merge_by(numlist, skip_count):
    i = 0
    limit = len(numlist)

    while i < limit:
        # list 1 is the range [i, i + skip_count]
        # list 2 is the range [i + skip_count + 1, i + 2 * skip_count]
        l1 = numlist[i:i + skip_count]
        l2 = numlist[i + skip_count:i + (2 * skip_count)]

        j = i
        sublimit = i + (2 * skip_count)

        while j < sublimit and len(l1) and len(l2):
            if l1[0] <= l2[0]:
                numlist[j] = l1.pop(0)
            else:
                numlist[j] = l2.pop(0)

            j += 1

        while j < sublimit and len(l1):
            numlist[j] = l1.pop(0)
            j += 1

        while j < sublimit and len(l2):
            numlist[j] = l2.pop(0)
            j += 1

        i = sublimit

    leftover = limit % skip_count

    if leftover:
        # merge the leftover with the rest of the sorted part
        cutpoint = limit - leftover
        l1 = numlist[0:cutpoint]
        l2 = numlist[cutpoint:limit]

        i = 0
        while i < limit and len(l1) and len(l2):
            if l1[0] < l2[0]:
                numlist[i] = l1.pop(0)
            else:
                numlist[i] = l2.pop(0)

            i += 1
        
        # Since we are sure that l1 is longer than l2
        while i < limit and len(l1):
            numlist[i] = l1.pop(0)
            i += 1

def merge_sort(numlist):
    """
    Keep merging til a skip count of half the numlist size.
    """
    limit = len(numlist)
    i = 1 
    while i < limit:
        merge_by(numlist, i)
        i *= 2


class FunctionsTest(unittest.TestCase):
    
    def test_sort(self):
        one = [1]
        merge_sort(one)
        self.assertEqual(one, [1])
        pi = [1, 4, 1 ,5 ,9, 2]
        merge_sort(pi)
        self.assertEqual(pi, [1, 1, 2, 4, 5, 9])
        pi_odd = [1, 4, 1, 5, 9]
        merge_sort(pi_odd)
        self.assertEqual(pi_odd, [1, 1, 4, 5, 9])

        inversion_case = [2, 3, 8, 6, 1]
        sorted_inversion_case = sorted(inversion_case)
        merge_sort(inversion_case)
        self.assertEqual(sorted_inversion_case, inversion_case)

if __name__ == "__main__":
    unittest.main()
