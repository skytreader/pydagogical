from ..prefix_tree import PrefixTree, PrefixTreeSearchResults

import unittest

class PrefixTreeTests(unittest.TestCase):

    def test_in_tree(self):
        pt = PrefixTree()
        pt.add_word("child")
        pt.add_word("children")
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
