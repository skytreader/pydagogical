from ..binary_tree import NaiveBinaryTree, InorderIterator, PreorderIterator

import unittest

class NaiveBinaryTreeTest(unittest.TestCase):
    
    def setUp(self):
        self.__setup_full_binary_tree()
        self.__setup_strictly_binary_tree()
        self.__setup_left_skewed_binary_tree()
        self.__setup_right_skewed_binary_tree()

    def __setup_full_binary_tree(self):
        """
        Creates a binary tree with the letters of the alphabet (A-O) laid out in
        level-order.
        """
        # Create the nodes
        nodes = {}
        self.node_data_full = "ABCDEFGHIJKLMNO"
        self.inorder_full = "HDIBJEKALFMCNGO"
        self.preorder_full = "ABDHIEJKCFLMGNO"

        for c in self.node_data_full:
            nodes[c] = NaiveBinaryTree(c)

        self.root_full = nodes["A"]

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

        self.nodes_full = nodes

    def __setup_strictly_binary_tree(self):
        """
              A
             / \
             B C
            / \
            D E
             / \
             F  G
        """
        nodes = {}
        self.node_data_strictly_binary = "ABCDEFG"
        self.inorder_strictly_binary = "DBFEGAC"
        self.preorder_strictly_binary = "ABDEFGC"

        for c in self.node_data_strictly_binary:
            nodes[c] = NaiveBinaryTree(c)

        # LEVEL 0
        self.root_strictly_binary = nodes["A"]

        # LEVEL 1
        nodes["A"].left_son = nodes["B"]
        nodes["A"].right_son = nodes["C"]

        # LEVEL 2
        nodes["B"].left_son = nodes["D"]
        nodes["B"].right_son = nodes["E"]

        # LEVEL 3
        nodes["E"].left_son = nodes["F"]
        nodes["E"].right_son = nodes["G"]

    def __setup_left_skewed_binary_tree(self):
        nodes = {}
        self.node_data_left_skewed = "ABC"
        self.inorder_left_skewed = "CBA"
        self.preorder_left_skewed = "ABC"

        for c in self.node_data_left_skewed:
            nodes[c] = NaiveBinaryTree(c)

        # LEVEL 0
        self.root_left_skewed = nodes["A"]

        # LEVEL 1
        nodes["A"].left_son = nodes["B"]

        # LEVEL 2
        nodes["B"].left_son = nodes["C"]

    def __setup_right_skewed_binary_tree(self):
        nodes = {}
        self.node_data_right_skewed = "ABC"
        self.inorder_right_skewed = "ABC"
        self.preorder_right_skewed = "ABC"

        for c in self.node_data_right_skewed:
            nodes[c] = NaiveBinaryTree(c)

        # LEVEL 0
        self.root_right_skewed = nodes["A"]

        # LEVEL 1
        nodes["A"].right_son = nodes["B"]

        # LEVEL 2
        nodes["B"].right_son = nodes["C"]

    def test_setUp(self):
        """
        Ensures that setUp is not wonky and is as expected.
        """
        # Ensure that we expect the same number of nodes from the orders of
        # iteration
        self.assertEqual(len(self.node_data_full), len(self.inorder_full))
        self.assertEqual(len(self.node_data_full), len(self.preorder_full))

        self.assertEqual(
            len(self.node_data_strictly_binary),
            len(self.inorder_strictly_binary)
        )
        self.assertEqual(
            len(self.node_data_strictly_binary),
            len(self.preorder_strictly_binary)
        )

        self.assertEqual(
            len(self.node_data_left_skewed),
            len(self.inorder_left_skewed)
        )
        self.assertEqual(
            len(self.node_data_left_skewed),
            len(self.preorder_left_skewed)
        )

        self.assertEqual(
            len(self.node_data_right_skewed),
            len(self.inorder_right_skewed)
        )
        self.assertEqual(
            len(self.node_data_right_skewed),
            len(self.preorder_right_skewed)
        )

    def test_search(self):
        self.assertFalse(self.root_full.search("P"))
        self.assertTrue(self.root_full.search("A"))

class IteratorTest(NaiveBinaryTreeTest):
    """
    Test all the iterators in this class.
    """

    def __iterator_unit(self, iterator, binary_tree, expected_order):
        iterated = iterator(binary_tree)
        iterator_order = [node for node in iterated]
        self.assertEqual(
            expected_order,
            "".join([node.node_data for node in iterator_order])
        )

    def test_inorder(self):
        self.__iterator_unit(InorderIterator, self.root_full, self.inorder_full)

    def test_preorder(self):
        self.__iterator_unit(PreorderIterator, self.root_full, self.preorder_full)

class BooleanTest(unittest.TestCase):
    
    def setUp(self):
        self.boole_tree = NaiveBinaryTree(True)
        self.boole_tree.left_son = NaiveBinaryTree(False)
        self.boole_tree.right_son = NaiveBinaryTree(False)
        self.boole_tree.left_son.left_son = NaiveBinaryTree(True)
        self.boole_tree.left_son.right_son = NaiveBinaryTree(True)

    def test_inorder(self):
        inorder = InorderIterator(self.boole_tree)
        iterator_order = []

        for data in inorder:
            iterator_order.append(data)

        self.assertEqual(
            [True, False, True, True, False],
            [node.node_data for node in iterator_order]
        )

class StructureTest(unittest.TestCase):
    
    def setUp(self):
        self.boole_tree = NaiveBinaryTree("A")
        self.boole_tree.left_son = NaiveBinaryTree("B")
        self.boole_tree.right_son = NaiveBinaryTree("C")
        self.boole_tree.left_son.left_son = NaiveBinaryTree("D")
        self.boole_tree.left_son.right_son = NaiveBinaryTree("E")

    def test_inorder(self):
        inorder = InorderIterator(self.boole_tree)
        iterator_order = []

        for data in inorder:
            iterator_order.append(data)

        self.assertEqual(["D", "B", "E", "A", "C"], [node.node_data for node in iterator_order])

if __name__ == "__main__":
    unittest.main()
