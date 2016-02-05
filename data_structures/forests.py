#! /usr/bin/env python3

import copy
import unittest

"""
Interface and implementations of a forest abstract data type.

(Taken from my programming praxis repo~Chad)
"""

class Forest(object):
    """
    Implementations should make it clear whether the arguments passed for
    node is an index or an actual object. If, for an implementation, a
    certain method is not supported, raise a NotImplementedError .

    In using forests, be careful not to confuse nodes with its shallow
    copies and deep copies.

    Note that a single tree is a forest structure with all nodes linked.
    """
    
    def add_node(self, node_contents):
        pass

    def get_nodes(self):
        """
        Return an iterable containing all the nodes _in this forest_.
        """
        pass

    def get_children(self, node):
        pass

    def get_parents(self, node):
        """
        Should return a list of all parents of the given node, in the event
        that there is more than one. If the indicated node is a root node,
        return an empty list
        """
        pass

    def link_child(self, parent, child):
        pass

class ListForest(Forest):
    """
    Implements a forest as a list-of-lists. Don't use this if you need
    to store multiple shallow copies of data in a single forest.

    Pass actual objects for nodes --- we'll search for them!

    Family structure:
    The first node in a family is the parent of that family. The succeding
    nodes are the indices of the nodes which are direct descendants of the
    family
    """

    def __init__(self):
        self.__nodes = []
    
    def add_node(self, node_contents):
        self.__nodes.append([node_contents])

    def get_nodes(self):
        """
        Returns all the nodes inserted so far in this tree. This returns
        the nodes in the order they were inserted.
        """
        return list(map(lambda x: x[0], self.__nodes))

    def link_child(self, parent, child):
        """
        Links nodes parent and child. If there are several shallow copies
        of either parent or child scattered in in the forest, only the first
        copy inserted is used.

        Note that both parent and child must be in the set of nodes first before
        they can be linked.
        
        TODO Test with deep and shallow copies.
        """
        nodelist = self.get_nodes()
        parent_index = nodelist.index(parent)
        child_index = nodelist.index(child)

        self.__nodes[parent_index].append(child_index)

    def get_children(self, parent):
        """
        Returns all the children of parent as a list of objects.
        """
        all_nodes = self.get_nodes()
        parent_index = all_nodes.index(parent)
        parent_family = self.__nodes[parent_index]
        children = parent_family[1:len(parent_family)]
        
        return [self.__nodes[child_index][0] for child_index in children]

    def get_parents(self, child):
        parents = []
        nodes = self.get_nodes()
        child_index = nodes.index(child)

        for family in self.__nodes:
            if child_index in family:
                parents.append(family[0])

        return parents

# More-space-economical representations

class PreorderSeqForest(Forest):
    """
    Uses a preorder-sequential representation to represent the
    tree. Construction might be more expensive compared to
    ListForest but the space used should be less.
    """
    
    def __init__(self):
        """
        rtags and ltags are boolean arrays.
        """
        self.__rtags = []
        self.__nodedata = []
        self.__ltags = []

    def add_node(self, node_data):
        """
        The node data is appended as a sole node.
        """
        self.__rtags.append(True)
        self.__nodedata.append(data)
        self.__ltags.append(True)
    
    def get_tree(self, root):
        """
        Get the (sub-)tree rooted at root.

        Returns a list of nodes included in the subtree rooted at
        the specified node (root). The list should be in preorder
        sequential order and must include the root.

        But, what if the root is the last child (and it also has
        child nodes)?
        """
        root_index = self.__nodedata.index(root)
        last_index = root_index
        count = 0 if self.__rtags[root_index] and self.__ltags[root_index] else 1
        last_index += 1
        limit = len(self.__nodedata)

        while root_index < limit and count:
            if self.__rtags[root_index]:
                count += 1

            if self.__ltags[root_index]:
                count -= 1

        return self.__nodedata[root_index:last_index + 1]

    def get_children(self, parent):
        subtree = self.get_tree(parent)
        parent_index = subtree[0]
