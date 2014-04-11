#! /usr/bin/env python3

import unittest

from graphs import Graph, AdjacencyLists, DFSIterator
from json_parser import GraphParser

def is_acyclic(graph):
    """
    Loop through the graph via DFS. Take note of each node visited. Get the
    neighbors of each visited node and, if one of the neighbors has been
    visited previously, the graph is acyclic (we have found a "back edge").

    Return True is the graph is acyclic ("no cycles"). Otherwise False.
    """
    visited = []
    dfs_seq = DFSIterator(graph)

    for node in dfs_seq:
        visited.insert(0, node)
        node_neighbors = graph.get_neighbors(node)
        
        for neighbor in node_neighbors:
            if neighbor in visited:
                return False

    return True

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
