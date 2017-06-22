from ..scales import *

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
        self.assertEqual("G#", norm_flat("Ab"))
        self.assertEqual("B", norm_flat("Cb"))
        self.assertEqual("A#", norm_flat("Bb"))
        self.assertEqual("A#", norm_flat("bb"))
        self.assertEqual("D#", norm_flat("D#"))
        self.assertEqual("D", norm_flat("D"))

    def test_interval_quality(self):
        self.assertEqual("perfect 4th", interval_quality("C", "F"))
        self.assertEqual("minor 3rd", interval_quality("A", "C"))
        self.assertEqual("major 2nd", interval_quality("A#", "C"))
        self.assertEqual("major 3rd", interval_quality("A", "C#"))
        self.assertEqual("minor 3rd", interval_quality("a", "C"))
        self.assertEqual("minor 3rd", interval_quality("a", "c"))
        self.assertEqual("minor 3rd", interval_quality("a#", "c#"))
        self.assertEqual("major 2nd", interval_quality("a#", "c"))
        self.assertEqual("major 3rd", interval_quality("a", "c#"))
        self.assertEqual("minor 3rd", interval_quality("a#", "C#"))
        self.assertEqual("minor 3rd", interval_quality("A#", "c#"))
        self.assertEqual("major 2nd", interval_quality("a#", "C"))
        self.assertEqual("major 3rd", interval_quality("a", "C#"))
        self.assertEqual("major 2nd", interval_quality("A#", "c"))
        self.assertEqual("major 3rd", interval_quality("a", "C#"))

        self.assertNotEqual(interval_quality("A", "C"), interval_quality("C", "A"))
        self.assertEqual("major 6th", interval_quality("C", "A"))

    def test_add_interval(self):
        self.assertEqual("C", add_interval("A", "minor 3rd"))
        self.assertEqual("C#", add_interval("A", "major 3rd"))
        self.assertEqual("A", add_interval("A", "octave"))
        self.assertEqual("A", add_interval("A", "unison"))
