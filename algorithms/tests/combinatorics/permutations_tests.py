from ...combinatorics.permutations import permute_dfs

import unittest

class PermutationsTest(unittest.TestCase):

    def setUp(self):
        self.cases = {
            "abc": ["abc", "acb", "bac", "bca", "cab", "cba"],
            "": []
        }

        for k in self.cases:
            tplify = [tuple(char for char in string) for string in self.cases[k]]
            self.cases[k] = set(tplify)

    def test_permute_dfs(self):
        for k in self.cases:
            actual = permute_dfs(k)
            self.assertEqual(self.cases[k], actual)
