from ..misc import *

import unittest

class MiscTests(unittest.TestCase):

    def test_non_decreasing_subranges(self):
        self.assertEqual(set(), get_non_decreasing_subranges([]))
        self.assertEqual(set([(0, 2)]), get_non_decreasing_subranges([1, 2, 3]))
        self.assertEquals(
            set([(0, 2), (3, 3), (4, 4), (5, 5)]),
            get_non_decreasing_subranges([1, 2, 3, 2, 1, 0])
        )
        self.assertEquals(
            set([(0, 0), (1, 1), (2, 2)]),
            get_non_decreasing_subranges([3, 2, 1])
        )

    def test_proper_non_decreasing_subranges(self):
        self.assertEqual(set(), get_proper_non_decreasing_subranges([]))
        self.assertEqual(set([(0, 2), (0, 1), (1, 2)]), get_proper_non_decreasing_subranges([1, 2, 3]))
        self.assertEqual(
            set([(0, 2), (0, 1), (1, 2)]),
            get_proper_non_decreasing_subranges([1, 2, 3, 2, 1, 0])
        )
        self.assertEqual(set(), get_proper_non_decreasing_subranges([3, 2, 1]))
