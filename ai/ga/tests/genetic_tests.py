from ..genetic import GASolver

import random
import string
import unittest

class MockSolver(GASolver):

    def __init__(self, initial_pool):
        super(MockSolver, self).__init__(initial_pool, show_print=False)

    def mutate(self, variation):
        return "".join([random.choice(string.ascii_lowercase) for _ in range(len(variation))])

    def compute_fitness(self, variation):
        return random.random()

class GeneticTests(unittest.TestCase):

    def setUp(self):
        self.ga_solver = MockSolver(["abcd"])

    def test_create_offspring(self):
        pre_offspring_len = len(self.ga_solver.current_pool)
        self.assertNotEqual(pre_offspring_len, self.ga_solver.max_pool_size)
        self.ga_solver.create_offspring()
        post_offspring_len = len(self.ga_solver.current_pool)
        self.assertTrue(post_offspring_len > pre_offspring_len)
