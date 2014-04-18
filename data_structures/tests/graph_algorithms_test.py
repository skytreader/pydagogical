from ..graphs import AdjacencyLists
from ..graph_algorithms import is_acyclic

import unittest

class FunctionsTest(unittest.TestCase):
    # TODO Make use of json_parser and the epiqueue submodule. 
    def test_acyclic(self):
        acyclic_graph = AdjacencyLists()
        acyclic_graph.add_nodes(("node1", "node2", "node3", "node4"))
        # Let's have a simple circle here...
        acyclic_graph.make_neighbor("node1", "node2")
        acyclic_graph.make_neighbor("node2", "node3")
        acyclic_graph.make_neighbor("node3", "node4")
        acyclic_graph.make_neighbor("node4", "node1")

        self.assertFalse(is_acyclic(acyclic_graph))

if __name__ == "__main__":
    unittest.main()