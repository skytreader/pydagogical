from ..binary_tree import NaiveBinaryTree, InorderIterator, PreorderIterator

import unittest

class NaiveBinaryTreeTest(unittest.TestCase):
    
    def setUp(self):
        """
        Creates a binary tree with the letters of the alphabet (A-O) laid out in
        level-order.
        """
        # Create the nodes
        nodes = {}
        self.node_data = "ABCDEFGHIJKLMNO"
        self.inorder = "HDIBJEKALFMCNGO"
        self.preorder = "ABDHIEJKCFLMGNO"

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

        # Ensure that binary trees are pointing to expected data
        for c in self.node_data:
            self.assertEqual(c, self.nodes[c].node_data)

        # Ensure that we expect the same number of nodes from the orders of
        # iteration
        self.assertEqual(len(self.node_data), len(self.inorder))

    def test_search(self):
        self.assertFalse(self.test_root.search("P"))
        self.assertTrue(self.test_root.search("A"))

class IteratorTest(NaiveBinaryTreeTest):
    """
    Test all the iterators in this class.
    """

    def test_inorder(self):
        inorder = InorderIterator(self.test_root)
        iterator_order = []
        
        for node in inorder:
            iterator_order.append(node)

        self.assertEqual(
            self.inorder,
            "".join([node.node_data for node in iterator_order])
        )

    def test_preorder(self):
        preorder = PreorderIterator(self.test_root)
        iterator_order = []

        for node in preorder:
            iterator_order.append(node)

        self.assertEqual(
            self.preorder,
            "".join([node.node_data for node in iterator_order])
        )

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
