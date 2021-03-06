#! /usr/bin/env python3
from enum import Enum, unique

"""
Naive binary tree implementation.
"""

def debug_print(ls):
    list_string = "["

    for item in ls:
        list_string += str(item) + ","

    list_string += "]"

    return list_string

@unique
class Traversals(Enum):
    INORDER = 0
    PREORDER = 1
    POSTORDER = 2

class InorderIterator(object):
    """
    Inorder traversal. Avoid modifying the tree while iterating. The modifications
    may not be reflected during traversal.
    """
    
    def __init__(self, bintree):
        self.bintree = bintree
        # Always point to the current node
        self.roving_pointer = self.bintree
        # the traversal stack
        self.traversal_stack = []
        self.visited = set()

        self.__initialize()

    def __iter__(self):
        return self

    def __initialize(self):
        """
        Initialize the tree so that the first traversal call is fast.
        """
        while self.roving_pointer.left_son:
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

        if (
            not self.roving_pointer.left_son or
            self.roving_pointer.left_son in self.visited
        ):
            if not self.roving_pointer.right_son and len(self.traversal_stack):
                # Backtrack to parent node. If it was never visited, it goes next.
                backtrack_node = self.traversal_stack.pop()
    
                # Keep backtracking until you are not pointing to a visited node
                # anymore. FIXME Is this necessary?
                #while backtrack_node in self.visited:
                #    backtrack_node = self.traversal_stack.pop()

                self.roving_pointer = backtrack_node
            elif self.roving_pointer.right_son:
                # Traverse the right son. But wait, everytime you traverse a 
                # right son, you need to get to its leaf first.
                local_rover = self.roving_pointer.right_son

                # Basically, just the __initialize function again but done on 
                # a subtree.
                while local_rover.left_son:
                    self.traversal_stack.append(local_rover)
                    local_rover = local_rover.left_son

                self.roving_pointer = local_rover

        # At this point, by virtue of inorder, we are sure that the left son has
        # been visited.
        
        self.visited.add(next_node)
        return next_node

class PreorderIterator(object):
    
    def __init__(self, bintree):
        self.bintree = bintree
        self.roving_pointer = self.bintree
        self.traversal_stack = []
        self.visited = set()

    def __can_visit(self, node):
        return node is not None and node not in self.visited

    def __next__(self):
        next_node = self.roving_pointer
        if (next_node is None or next_node in self.visited) and not self.traversal_stack:
            raise StopIteration
        self.visited.add(next_node)

        is_lson_visitable = self.__can_visit(next_node.left_son)
        is_rson_visitable = self.__can_visit(next_node.right_son)

        # Update the roving pointer to point to the node after next_node
        if is_lson_visitable:
            # By virtue of preorder, it follows that rson is not yet visited too.
            self.roving_pointer = next_node.left_son 
        elif is_rson_visitable:
            self.roving_pointer = next_node.right_son
        elif self.traversal_stack:
            # This subtree is done. Keep popping stack to find node with
            # visitable right_son
            stack_rover = self.traversal_stack.pop()

            while self.traversal_stack and not self.__can_visit(stack_rover.right_son):
                stack_rover = self.traversal_stack.pop()

            self.roving_pointer = stack_rover.right_son

        if is_lson_visitable or is_rson_visitable:
            self.traversal_stack.append(next_node)

        return next_node

    def __iter__(self):
        return self

class BinaryTree(object):
    """
    Interface for binary tree objects.
    """

    ITERATORS = {
        Traversals.INORDER: InorderIterator
    }

    def __init__(self, node_data):
        self.node_data = node_data
        self.left_son = None
        self.right_son = None

    def search(self, query, search_type=Traversals.INORDER):
        """
        Searches the binary tree for the given query data.  Returns either true
        or false. The optional search_type parameter can be used to specify the
        type of search to be done. Use the fields of the traversals Enum.
        """
        pass

    def __str__(self):
        # This is the __str__ for debugging
        return str(self.node_data)

class NaiveBinaryTree(BinaryTree):
    """
    Naive implementation of a binary tree.
    """

    def __init__(self, node_data):
        super(NaiveBinaryTree, self).__init__(node_data)

    def search(self, query, search_type=Traversals.INORDER):
        """
        Searches using inorder search by default.

        Returns True if the query can be found in this tree, False otherwise.
        """
        walkthrough = BinaryTree.ITERATORS[search_type](self)

        for node in walkthrough:
            if node.node_data == query:
                return True

        return False
