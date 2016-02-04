from ..forests import ListForest

import unittest

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

        Galadriel is the mother of:
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

    def standard(self, forest):
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
        self.standard(listforest)

        # Test that the order of nodes returned by get_nodes is insertion order
        nodes = listforest.get_nodes()
        limit = len(nodes)

        for i in range(limit):
            self.assertEqual(self.all_nodes[i], nodes[i])

if __name__ == "__main__":
    unittest.main()
