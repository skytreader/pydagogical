from ..scales import construct_major_scale

import unittest

class ScalesTests(unittest.TestCase):

    def test_construct_major_scale(self):
        c_major_scale = ["C", "D", "E", "F", "G", "A", "B", "C"]

        self.assertEqual(c_major_scale, construct_major_scale("C"))
        self.assertEqual(c_major_scale, construct_major_scale("c"))
