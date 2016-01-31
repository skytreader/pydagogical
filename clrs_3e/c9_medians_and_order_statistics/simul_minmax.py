#! /usr/bin/env python3

import unittest

"""
Deliberately avoids using Python's built-in min and max functions to explicitly
show comparisons.

TODO Note how many comparisons are made for each algorithm.
"""

def simul_minmax(numlist):
    """
    From the given list of numbers, simulatneously pick the minimum and maximum.
    The return value is a tuple pair with the minimum as the first element and
    the maximum as the second element.

    Assumes that list is not empty.
    """
    curmindex = 0
    curmaxdex = 0

    for i, v in enumerate(numlist):
        if v < numlist[curmindex]:
            curmindex = i
        elif v > numlist[curmaxdex]:
            curmaxdex = i

    return (numlist[curmindex], numlist[curmaxdex])

def cormen_simulminmax(numlist):
    """
    I figured it out. As described in CORMEN using at most 3*floor(n/2) 
    comparisons. Returns a tuple pair with the minimum as the first element and
    the maximum as the second element.
    """
    curmindex = 0
    curmaxdex = 0
    startdex = 0

    if len(numlist) % 2:
        startdex = 1
    else:
        startdex = 2

        if numlist[0] < numlist[1]:
            curmindex = 0
            curmaxdex = 1
        elif numlist[0] > numlist[1]:
            curmaxdex = 0
            curmindex = 1
        # else they are equal and it does not really matter

    limit = len(numlist)

    while startdex < limit:
        if numlist[startdex] < numlist[startdex + 1]:
            if numlist[startdex] < numlist[curmindex]:
                curmindex = startdex

            if numlist[startdex + 1] > numlist[curmaxdex]:
                curmaxdex = startdex + 1
        elif numlist[startdex] > numlist[startdex + 1]:
            pass #TODO
            

class FunctionsTest(unittest.TestCase):
    
    def test_simul_minmax(self):
        singleton = [1]
        self.assertEqual(simul_minmax(singleton), (1, 1))

        odd_count = [3, 1, 4, 1, 5]
        self.assertEqual(simul_minmax(odd_count), (1, 5))

        even_count = [3, 1, 4, 1, 5, 9]
        self.assertEqual(simul_minmax(even_count), (1, 9))

        self.assertEqual(simul_minmax([1, 2]), (1, 2))
        self.assertEqual(simul_minmax([2, 1]), (1, 2))
        self.assertEqual(simul_minmax([1, 1]), (1, 1))

if __name__ == "__main__":
    unittest.main()
