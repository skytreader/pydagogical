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

    def get_nodes(self, node_contents):
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

class Person(object):
    """
    A dummy object for testing shallow and deep copies.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __deepcopy__(self, memo):
        return Person(self.name, self.age)

class ListForestTests(unittest.TestCase):
    """
    This class features two kinds of tests: the standard test and a
    custom test for each implementation. The standard test tests that
    tree implementations actually do what is expected of them. You
    You may then test the kinks of your implementation in the custom
    test.
    """
    
    def setUp(self):
        """
        Creates the nodes but _does not_ assemble them in a tree. The
        nodes and the expected tree structure is as follows...

        Earwen is the mother of:
          Finrod
          Angrod
          Edhellos (in-law)
          Aegnor
          Galadriel

        Edhellos is the mother of:
          Orodreth
          Orodreth's wife (in-law and unnamed)

        Orodreth's wife is the mother of:
          Gil-Galad
          Findulas

        Garadriel is the mother of:
          Celebrian
        
        And, when in doubt, always check their ages. :D
        """
        self.earwen = Person("Earwen", 200)
        self.finrod = Person("Finrod", 150)
        self.angrod = Person("Angrod", 150)
        self.edhellos = Person("Edhellos", 145)
        self.aegnor = Person("Aegnor", 150)
        self.orodreth = Person("Orodreth", 100)
        self.orodreth_wife = Person("Orodreth's Wife", 95)
        self.gil_galad = Person("Gil-galad", 50)
        self.findulias = Person("Findulias", 50)
        self.galadriel = Person("Galadriel", 150)
        self.celebrian = Person("Celebrian", 100)

        self.all_nodes = [self.earwen, self.finrod, self.angrod, self.edhellos, self.aegnor, self.orodreth, self.orodreth_wife, self.gil_galad, self.findulias, self.galadriel, self.celebrian]

    def standard_tests(self, forest):
        """
        The standard test always assumes that an elf-child is linked
        to its elf-mother but not necessarily to its elf-father.
        """
        galadriel_mother = forest.get_parents(self.galadriel)
        self.assertEqual(galadriel_mother[0], self.earwen)
        self.assertEqual(len(galadriel_mother), 1)

        earwen_elfchildren = [self.finrod, self.angrod, self.edhellos, self.aegnor, self.galadriel]
        earwen_treechildren = forest.get_children(self.earwen)

        self.assertEqual(len(earwen_elfchildren), len(earwen_treechildren))

        for elfchild in earwen_elfchildren:
            self.assertTrue(elfchild in earwen_treechildren)

    def test_listforest_standard(self):
        listforest = ListForest()

        for elf in self.all_nodes:
            listforest.add_node(elf)

        listforest.link_child(self.earwen, self.finrod)
        listforest.link_child(self.earwen, self.angrod)
        listforest.link_child(self.earwen, self.edhellos)
        listforest.link_child(self.earwen, self.aegnor)
        listforest.link_child(self.earwen, self.galadriel)

        listforest.link_child(self.edhellos, self.orodreth)
        listforest.link_child(self.edhellos, self.orodreth_wife)
        
        listforest.link_child(self.galadriel, self.celebrian)
        
        listforest.link_child(self.orodreth_wife, self.gil_galad)
        listforest.link_child(self.orodreth_wife, self.findulias)
        
        # Standard testing
        self.standard_tests(listforest)

        # Test that the order of nodes returned by get_nodes is insertion order
        nodes = listforest.get_nodes()
        limit = len(nodes)

        for i in range(limit):
            self.assertEqual(self.all_nodes[i], nodes[i])

if __name__ == "__main__":
    unittest.main()
