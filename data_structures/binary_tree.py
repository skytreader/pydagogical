#! /usr/bin/env python3

import unittest

"""
Naive binary tree implementation.
"""

def debug_print(ls):
    list_string = "["

    for item in ls:
        list_string += str(item) + ","

    list_string += "]"

    return list_string

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

    def __str__(self):
        #return str(self.node_data) + ":{'left_son':'" + str(self.left_son) + "',''right_son':'" + str(self.right_son)
        # This is the __str__ for debuggin
        return str(self.node_data)

class InorderIterator(object):
    """
    Inorder traversal. Avoid modifying the tree while iterating. The modifications
    may not be reflected during traversal.
    """
    #TODO Ensure that the iterator is for Python 3
    
    def __init__(self, bintree):
        self.bintree = bintree
        # Always point to the current node
        self.roving_pointer = self.bintree
        # the traversal stack
        self.traversal_stack = []
        self.visited = []

        self.__initialize()

    def __iter__(self):
        return self

    def __initialize(self):
        """
        Initialize the tree so that the first traversal call is fast.
        """
        while self.roving_pointer.left_son is not None:
            self.traversal_stack.append(self.roving_pointer)
            self.roving_pointer = self.roving_pointer.left_son

    def __next__(self):
        """
        Return what comes next and update iterator's internal state to point to
        the DFS successor of the current node.

        Invariant: Everytime next is called, self.roving_pointer is already
        pointing to the node to be returned. All that is left for next to do
        is to update internal state of this iterator.
        """
        next_node = self.roving_pointer
        
        if next_node in self.visited:
            raise StopIteration

        # Update roving_pointer to point to what succeeds next_node

        if not self.roving_pointer.left_son or\
          self.roving_pointer.left_son in self.visited:
            if self.roving_pointer.right_son is None and len(self.traversal_stack):
                # Backtrack to parent node. If it was never visited, it goes next.
                backtrack_node = self.traversal_stack.pop()
    
                # Keep backtracking until you are not pointing to a visited node
                # anymore. FIXME Is this necessary?
                #while backtrack_node in self.visited:
                #    backtrack_node = self.traversal_stack.pop()

                self.roving_pointer = backtrack_node
            elif self.roving_pointer.right_son is not None:
                # Traverse the right son. But wait, everytime you traverse a 
                # right son, you need to get to its leaf first.
                local_rover = self.roving_pointer.right_son

                # Basically, just the __initialize function again but done on 
                # a subtree.
                while local_rover.left_son is not None:
                    self.traversal_stack.append(local_rover)
                    local_rover = local_rover.left_son

                self.roving_pointer = local_rover

        # At this point, by virtue of inorder, we are sure that the left son has
        # been visited.
        
        self.visited.append(next_node)
        return next_node

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
        pass
