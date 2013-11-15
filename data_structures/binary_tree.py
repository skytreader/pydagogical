#! /usr/bin/env python3

import unittest

"""
Naive binary tree implementation.
"""

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

        self.__initialize()

    def __iter__(self):
        return self

    def __initialize(self):
        """
        Initialize the tree so that the first traversal call is fast.
        """
        while self.roving_pointer.left_son is not None:
            self.roving_pointer = self.roving_pointer.left_son

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
            # Point roving_pointer to last node visited
            self.roving_pointer = self.traversal_stack.pop()
            # Check the right son
            if self.roving_pointer.right_son is not None:
                # Point roving_pointer to its right_son
                self.roving_pointer = self.roving_pointer.right_son
            
            # Otherwise it is None and so we are already pointing at the next
            # DFS node in the tree---no need to change where roving_pointer is
            # currently pointing.

        # left node is not None so that is the next element
        if self.roving_pointer.left_son is not None:
            # Push to stack for backtracking
            self.traversal_stack.append(self.roving_pointer)
            # Update roving_pointer to point to the left_son
            self.roving_pointer = self.roving_pointer.left_son
        
        return self.roving_pointer

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

class DFSIteratorTest(unittest.TestCase):
    
    def setUp(self):
        """
        Creates a binary tree with the letters of the alphabet (A-O) laid out in
        level-order.
        """
        # Create the nodes
        nodes = {}
        self.node_data = "ABCDEFGHIJKLMNO"

        for c in self.node_data:
            nodes[c] = NaiveBinaryTree(c)

        self.test_root = nodes["A"]

        # Connect the nodes
        # LEVEL 0
        nodes["A"].left_son = nodes["B"]
        nodes["A"].right_son = nodes["C"]

        # LEVEL 1
        nodes["B"].left_son = nodes["D"]
        nodes["B"].right_son = nodes["E"]

        nodes["C"].left_son = nodes["F"]
        nodes["C"].right_son = nodes["G"]

        # LEVEL 2
        nodes["D"].left_son = nodes["H"]
        nodes["D"].right_son = nodes["I"]

        nodes["E"].left_son = nodes["J"]
        nodes["E"].right_son = nodes["K"]

        nodes["F"].left_son = nodes["L"]
        nodes["F"].right_son = nodes["M"]

        nodes["G"].left_son = nodes["N"]
        nodes["G"].right_son = nodes["O"]

        self.nodes = nodes

    def test_setUp(self):
        """
        Ensures that setUp is not wonky and is as expected.
        """
        for c in self.node_data:
            self.assertEqual(c, self.nodes[c].node_data)

if __name__ == "__main__":
    unittest.main()
