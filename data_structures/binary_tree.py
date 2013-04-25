#! /usr/bin/env python3

import unittest

"""
Naive binary tree implementation.
"""

# TODO Implement binary tree as a graph

class BinaryTree(object):
    """
    Interface for binary tree objects.
    """
    
    """
    Flag for depth-first search.
    """
    DFS = "dfs"
    """
    Flag for breadth-first search.
    """
    BFS = "bfs"
    """
    Flag for in-order search
    """
    INP = "inp"

    def __init__(self, node_data):
        self.node_data = node_data
        self.left_son = None
        self.right_son = None

    def search(self, query, search_type = ""):
        """
        Searches the binary tree for the given query data.
        Returns either true or false. The optional search_type
        parameter can be used to specify the type of search
        to be done. Use the DFS, BDS, and INP fields of this
        class.
        """
        pass

class DFSIterator(object):
    
    def __init__(self, bintree):
        self.bintree = bintree
        # Always point to the current node
        self.roving_pointer = self.bintree
        # the traversal stack
        self.traversal_stack = []

    def __iter__(self):
        return self

    def next(self):
        """
        Return what comes next and update iterator's internal
        state to point to the DFS successor of the current node.

        Always returns the data of the current node, not the node
        itself.
        """
        
        # Pointing to a null node. This only happens when
        # we tried to return the right son of some non-null
        # node and that right son turned out to be null.
        if self.roving_pointer is None:
            pass
        # left node is None so next element is this node.
        elif self.roving_pointer.left_node is None:
            return_val = self.roving_pointer.node_data
            self.roving_pointer = self.roving_pointer.right_son
            return self.roving_pointer.node_data

class NaiveBinaryTree(BinaryTree):
    """
    Naive implementation of a binary tree.
    """

    def __init__(self, node_data):
        super(NaiveBinaryTree, self).__init__(node_data)

    def search(self, query, search_type = BinaryTree.DFS):
        """
        Searches using depth-first search by default.
        """

class NaiveBinaryTreeTest(unittest.TestCase):
    
    def setUp(self):
        self.bt1 = NaiveBinaryTree("root")
    
    def test_init(self):
        self.assertEqual(self.bt1.left_son, None)
        self.assertEqual(self.bt1.right_son, None)

if __name__ == "__main__":
    unittest.main()
