from ..scales import construct_major_scale, interval_quantity

import unittest

class ScalesTests(unittest.TestCase):

    def test_construct_major_scale(self):
        c_major_scale = ["C", "D", "E", "F", "G", "A", "B", "C"]

        self.assertEqual(c_major_scale, construct_major_scale("C"))
        self.assertEqual(c_major_scale, construct_major_scale("c"))

    def test_interval_quantity(self):
        self.assertEqual(3, interval_quantity("A", "C"))
        self.assertEqual(3, interval_quantity("A#", "C"))
        self.assertEqual(3, interval_quantity("A", "C#"))
        self.assertEqual(3, interval_quantity("a", "C"))
        self.assertEqual(3, interval_quantity("a", "c"))
        self.assertEqual(3, interval_quantity("a#", "c#"))
        self.assertEqual(3, interval_quantity("a#", "c"))
        self.assertEqual(3, interval_quantity("a", "c#"))
        self.assertEqual(3, interval_quantity("a#", "C#"))
        self.assertEqual(3, interval_quantity("A#", "c#"))
        self.assertEqual(3, interval_quantity("a#", "C"))
        self.assertEqual(3, interval_quantity("a", "C#"))
        self.assertEqual(3, interval_quantity("A#", "c"))
        self.assertEqual(3, interval_quantity("a", "C#"))
