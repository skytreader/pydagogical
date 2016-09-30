from ..union_find import UnionFind

import unittest

class DataNodeTests(unittest.TestCase):
    
    def setUp(self):
        self.union_find = UnionFind()
    
    def test_union_find(self):
        self.union_find.make_equal("a", "aa")
        self.union_find.make_equal("aaa", "aaaa")
        self.union_find.make_equal("aa", "aaa")

        self.assertTrue(self.union_find.is_equal("a", "aaaa"))

        self.union_find.make_equal("b", "bb")
        self.union_find.make_equal("b", "bbb")
        self.union_find.make_equal("b", "bbbb")

        self.assertTrue(self.union_find.is_equal("bb", "bbb"))
        self.assertTrue(self.union_find.is_equal("bbbb", "bb"))
        self.assertFalse(self.union_find.is_equal("a", "b"))
