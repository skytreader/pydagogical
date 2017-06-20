from ..scales import construct_major_scale, eval_flat, interval_quality, interval_quantity

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

        self.assertNotEqual(interval_quantity("A", "C"), interval_quantity("C", "A"))
        self.assertEqual(6, interval_quantity("C", "A"))

    def test_eval_flat(self):
        self.assertEqual("G#", eval_flat("Ab"))
        self.assertEqual("B", eval_flat("Cb"))
        self.assertEqual("A#", eval_flat("Bb"))
        self.assertEqual("A#", eval_flat("bb"))
        self.assertRaises(ValueError, eval_flat, "D#")
        self.assertRaises(ValueError, eval_flat, "D")

    def test_interval_quality(self):
        self.assertEqual(4, interval_quality("A", "C"))
        self.assertEqual(3, interval_quality("A#", "C"))
        self.assertEqual(5, interval_quality("A", "C#"))
        self.assertEqual(4, interval_quality("a", "C"))
        self.assertEqual(4, interval_quality("a", "c"))
        self.assertEqual(4, interval_quality("a#", "c#"))
        self.assertEqual(3, interval_quality("a#", "c"))
        self.assertEqual(5, interval_quality("a", "c#"))
        self.assertEqual(4, interval_quality("a#", "C#"))
        self.assertEqual(4, interval_quality("A#", "c#"))
        self.assertEqual(3, interval_quality("a#", "C"))
        self.assertEqual(5, interval_quality("a", "C#"))
        self.assertEqual(3, interval_quality("A#", "c"))
        self.assertEqual(5, interval_quality("a", "C#"))

        self.assertNotEqual(interval_quality("A", "C"), interval_quality("C", "A"))
        self.assertEqual(10, interval_quality("C", "A"))
