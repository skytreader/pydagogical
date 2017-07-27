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

    def test_multiple_first_child(self):
        pt = PrefixTree()
        pt.add_word("children")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        pt.add_word("child")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("chil"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("chicken"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)

        pt.add_word("hack")
        self.assertEqual(pt.in_tree("c"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("chil"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("chicken"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
        self.assertEqual(pt.in_tree("hack"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("heck"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
        self.assertEqual(pt.in_tree("ha"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("hacker"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)

        pt.add_word("hacker")
        self.assertEqual(pt.in_tree("child"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("children"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("chil"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("chicken"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
        self.assertEqual(pt.in_tree("hack"), PrefixTreeSearchResults.PREFIX_TERMINATED)
        self.assertEqual(pt.in_tree("heck"), PrefixTreeSearchResults.PREFIX_NOT_FOUND)
        self.assertEqual(pt.in_tree("ha"), PrefixTreeSearchResults.PREFIX_FOUND)
        self.assertEqual(pt.in_tree("hacker"), PrefixTreeSearchResults.PREFIX_TERMINATED)

    def test_more_branching(self):
        pt = PrefixTree()
        contents = ["because", "can", "do", "must", "we", "what", "dunk"]
        for c in contents:
            pt.add_word(c)
        
        self.assertEqual(PrefixTreeSearchResults.PREFIX_FOUND, pt.in_tree("d"))
        self.assertEqual(PrefixTreeSearchResults.PREFIX_FOUND, pt.in_tree("w"))
