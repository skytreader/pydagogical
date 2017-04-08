#! /usr/bin/env python3

import math

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
