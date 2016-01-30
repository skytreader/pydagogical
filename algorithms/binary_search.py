#! /usr/bin/env python

import math
import unittest

"""
http://programmingpraxis.com/2009/03/23/binary-search/

(Might also use this in other problems.)
"""

def binary_search(sorted_space, query):
    """
    Returns the index of the query in the sorted space if it
    is present in the list. Otherwise, returns a negative value.

    We assume that the list is sorted in ascending order.
    """
    # Hard-handle the trivial case
    if not len(sorted_space):
        return - 1

    low_limit = 0
    hi_limit = len(sorted_space)
    cur_node_index = math.floor((low_limit + hi_limit) / 2)
    visited_nodes = set()

    while cur_node_index not in visited_nodes:
        visited_nodes.add(cur_node_index)

        if sorted_space[cur_node_index] == query:
            return cur_node_index
        elif sorted_space[cur_node_index] < query:
            low_limit = cur_node_index
        else:
            hi_limit = cur_node_index

        cur_node_index = math.floor((low_limit + hi_limit) / 2)
    
    return -1

def binary_insert(ss, item):
    """
    Inserts the item in sorted_space (assumed to be sorted) such that
    the list remains to be sorted. The sorted_space is traversed as
    in binary_search.

    Returns the sorted_space with the item inserted in the proper
    place. This _does not_ modify the original list.
    """
    # Hard handle the trivial case
    if not len(ss):
        return [item]
    sorted_space = [i for i in ss]
    low_limit = 0
    hi_limit = len(sorted_space)
    cur_node_index = math.floor((low_limit + hi_limit) / 2)
    visited_nodes = set()

    while cur_node_index not in visited_nodes:
        visited_nodes.add(cur_node_index)

        if sorted_space[cur_node_index] == item:
            break
        elif sorted_space[cur_node_index] < item:
            low_limit = cur_node_index
        else:
            hi_limit = cur_node_index

        cur_node_index = math.floor((low_limit + hi_limit) / 2)
    
    if sorted_space[cur_node_index] >= item:
        sorted_space.insert(cur_node_index, item)
    else:
        sorted_space.insert(cur_node_index + 1, item)

    return sorted_space

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

if __name__ == "__main__":
    unittest.main()
