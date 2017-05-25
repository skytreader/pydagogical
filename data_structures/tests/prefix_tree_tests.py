from ..prefix_tree import PrefixTree, PrefixTreeSearchResults

import unittest

class PrefixTreeTests(unittest.TestCase):

    def test_in_tree(self):
        pt = PrefixTree()
        pt.add_word("child")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
        pt.add_word("children")
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("chil"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("chicken"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)

    def test_in_tree_reverse_add(self):
        pt = PrefixTree()
        pt.add_word("children")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        pt.add_word("child")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("chil"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("chicken"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
