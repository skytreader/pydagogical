from ..graphs import AdjacencyLists, AdjacencyMatrix, UndirectedAdjList, DFSIterator, DFSIslandIterator
from ..errors import DuplicateNodeException, NotInNodesException\

import random
import unittest

class AdjacencyListTest(unittest.TestCase):
    """
    This can be used as a master class for Graph unit tests. That is, if you are
    creating a new Graph implementation, it suffices for the unit tests to extend
    this class, and override the following methods:
        - _get_graph_instance
        - _construct_test_graph

    See the docstring of the mentioned methods for more info. You are, of course,
    more than free to add more tests and modify existing ones.

    To test:
        - Behavior when introducing deep and shallow copies.
    """

    def setUp(self):
        self.test_graph = self._get_graph_instance()
        self.test_graph.add_node("node1")
        self.test_graph.add_node("node2")
        self.test_graph.add_node("node3")
        self.test_graph.add_node("node4")

        self.test_node = "test_node"

    def _get_graph_instance(self):
        """
        Override this to return an instance of the Graph implementation you want
        to test.
        """
        return AdjacencyLists()

    def _construct_test_graph(self):
        """
        Utility test function to connect the four nodes of self.test_graph.
        After calling this function, get_neighbors_test should pass.
        """
        self.test_graph.make_neighbor("node1", "node2")
        self.test_graph.make_neighbor("node2", "node1")
        self.test_graph.make_neighbor("node1", "node3")
        self.test_graph.make_neighbor("node3", "node1")

        self.test_graph.make_neighbor("node1", "node4")
        self.test_graph.make_neighbor("node4", "node1")
        self.test_graph.make_neighbor("node2", "node4")
        self.test_graph.make_neighbor("node4", "node2")
        self.test_graph.make_neighbor("node3", "node4")
        self.test_graph.make_neighbor("node4", "node3")

    def test_add_node(self):
        """
        Test cases:
            - Introduce a new node -- should be added
            - Introduce an already-added node - must throw a
              DuplicateNodeException
        """
        self.test_graph.add_node(self.test_node)
        self.assertTrue(self.test_node in self.test_graph.added_nodes)
        self.assertRaises(DuplicateNodeException, self.test_graph.add_node, "node1")

    def test_add_nodes(self):
        """
        Adds lists of possible nodes.
        """
        # should be able to insert this fine
        test_nodes = ["the", "television's", "selling", "plastic", "figurine", "for", "leaders"]
        # none of these should be inserted---intersects with "the"
        duplicate_test_nodes = ["scared", "of", "losing", "all", "the", "time"]
        self.test_graph.add_nodes(test_nodes)

        for node in test_nodes:
            self.assertTrue(node in self.test_graph.added_nodes)

        self.assertRaises(DuplicateNodeException, self.test_graph.add_nodes, duplicate_test_nodes)

        for node in duplicate_test_nodes:
            if node != "the":
                self.assertTrue(node not in self.test_graph.added_nodes)

    def test_remove_node(self):
        """
        Add a node, check if added indeed. Then, remove that node and check that
        it is not there anymore.
        """
        self.test_graph.add_node(self.test_node)
        self.assertTrue(self.test_node in self.test_graph.added_nodes)
        
        self.test_graph.remove_node(self.test_node)
        self.assertTrue(self.test_node not in self.test_graph.added_nodes)

    def test_neighbor(self):
        """
        Tests both make_neighbor and is_reachable functionality.
        """
        self.test_graph.make_neighbor("node1", "node2")
        self.assertTrue(self.test_graph.is_reachable("node1", "node2"))
        self.assertFalse(self.test_graph.is_reachable("node2", "node1"))
        self.assertRaises(NotInNodesException, self.test_graph.make_neighbor, self.test_node, "node1")

    def test_get_weight(self):
        """
        Almost the same as _construct_test_graph except that it generates random
        weights and tests for those weights.
        """
        weights = {}
        connseq = (("node1", "node2"), ("node2", "node1"), ("node1", "node3"),
          ("node3", "node1"), ("node1", "node4"), ("node4", "node1"),
          ("node2", "node4"), ("node4", "node2"), ("node3", "node4"),
          ("node4", "node3"))

        for connection in connseq:
            weights[connection] = random.randint(1, 100)

        self.test_graph.make_neighbor("node1", "node2", weights[("node1", "node2")])
        self.test_graph.make_neighbor("node2", "node1", weights[("node2", "node1")])
        self.test_graph.make_neighbor("node1", "node3", weights[("node1", "node3")])
        self.test_graph.make_neighbor("node3", "node1", weights[("node3", "node1")])

        self.test_graph.make_neighbor("node1", "node4", weights[("node1", "node4")])
        self.test_graph.make_neighbor("node4", "node1", weights[("node4", "node1")])
        self.test_graph.make_neighbor("node2", "node4", weights[("node2", "node4")])
        self.test_graph.make_neighbor("node4", "node2", weights[("node4", "node2")])
        self.test_graph.make_neighbor("node3", "node4", weights[("node3", "node4")])
        self.test_graph.make_neighbor("node4", "node3", weights[("node4", "node3")])

        for connection in connseq:
            self.assertEqual(self.test_graph.get_weight(connection[0], connection[1]),
              weights[connection])

        # Test that, by default, the weight is 0.
        self.test_graph.add_nodes(("node5", "node6"))
        self.test_graph.make_neighbor("node5", "node6")
        self.assertEqual(self.test_graph.get_weight("node5", "node6"), 0)

    def test_edge_count(self):
        self._construct_test_graph()
        # Should be 10 since each bidirectional edge had to be created with two
        # calls to make_neighbor, therefore an edge count each.
        self.assertEqual(self.test_graph.edge_count, 10)

    def get_neighbors_test(self):
        self._construct_test_graph()
        n1_neighbors = self.test_graph.get_neighbors("node1")
        n2_neighbors = self.test_graph.get_neighbors("node2")
        n3_neighbors = self.test_graph.get_neighbors("node3")
        n4_neighbors = self.test_graph.get_neighbors("node4")

        n1_expected_neighbors = set(["node2", "node3", "node4"])
        self.assertEqual(n1_expected_neighbors, set(n1_neighbors))

        n2_expected_neighbors = set(["node4", "node1"])
        self.assertEqual(n2_expected_neighbors, set(n2_neighbors))

        n4_expected_neighbors = set(["node2", "node1", "node3"])
        self.assertEqual(n4_expected_neighbors, set(n4_neighbors))

        n3_expected_neighbors = set(["node1", "node4"])
        self.assertEqual(n3_expected_neighbors, set(n3_neighbors))

        # Isolated node test
        self.test_graph.add_node("five")
        self.assertTrue(self.test_graph.get_neighbors("five") == [])

        # NotInNodesException test
        self.assertRaises(NotInNodesException, self.test_graph.get_neighbors, "does not exist")

    def test_transpose(self):
        simple_graph = AdjacencyLists()
        simple_graph.add_nodes(("n1", "n2"))
        simple_graph.make_neighbor("n1", "n2")

        simple_graph_transpose = simple_graph.get_transpose(AdjacencyLists)
        self.assertTrue(simple_graph_transpose.is_reachable("n2", "n1"))
        self.assertFalse(simple_graph_transpose.is_reachable("n1", "n2"))

    def test_get_neighbors(self):
        self._construct_test_graph()
        self.get_neighbors_test()

    def test_get_indegree(self):
        self._construct_test_graph()
        n1_neighbors = self.test_graph.get_neighbors("node1")
        self.assertEqual(self.test_graph.get_indegree("node1"), len(n1_neighbors))

        # NotInNodesException test
        self.assertRaises(NotInNodesException, self.test_graph.get_indegree, "does not exist")

    def test_get_outdegree(self):
        n1_neighbors = self.test_graph.get_neighbors("node1")
        self.assertEqual(self.test_graph.get_outdegree("node1"), len(n1_neighbors))

class Route(object):
    """
    Super special class just for the heck of test_get_weight below.
    """

    def __init__(self, r):
        """
        r is an ordered tuple with two elements
        """
        self.origin = r[0]
        self.destination = r[1]

    def __eq__(self, r2):
        return (self.origin == r2.origin or self.origin == r2.destination) \
          and (self.destination == r2.destination or self.destination == r2.origin)

class UndirectedAdjListTest(AdjacencyListTest):
    
    def _get_graph_instance(self):
        return UndirectedAdjList()

    def test_neighbor(self):
        self.test_graph.make_neighbor("node1", "node2")
        self.assertTrue(self.test_graph.is_reachable("node1", "node2"))
        self.assertTrue(self.test_graph.is_reachable("node2", "node1"))

    def test_edge_count(self):
        self._construct_test_graph()
        self.assertEqual(self.test_graph.edge_count, 5)

    def test_get_weight(self):
        """
        Almost the same as _construct_test_graph except that it generates random
        weights and tests for those weights.

        Modified from AdjacencyListTest since this one is undirected and
        therefore going back and forth two nodes should not have different
        costs.
        """
        connseq = (("node1", "node2"), ("node2", "node1"), ("node1", "node3"),
          ("node3", "node1"), ("node1", "node4"), ("node4", "node1"),
          ("node2", "node4"), ("node4", "node2"), ("node3", "node4"),
          ("node4", "node3"))
        
        # TODO Avoid unnecessary loops if you have time to recode
        connroutes = []

        for connection in connseq:
            route = Route(connection)
            if route not in connroutes:
                connroutes.append(route)

        connroutes = tuple(connroutes)
        weights = []

        for i in range(len(connroutes)):
            weights.append(random.randint(1, 100))

        weights = tuple(weights)
        get_assigned_weight = lambda x: weights[connroutes.index(x)]

        self.test_graph.make_neighbor("node1", "node2", get_assigned_weight(Route(("node1", "node2"))))
        self.test_graph.make_neighbor("node2", "node1", get_assigned_weight(Route(("node2", "node1"))))
        self.test_graph.make_neighbor("node1", "node3", get_assigned_weight(Route(("node1", "node3"))))
        self.test_graph.make_neighbor("node3", "node1", get_assigned_weight(Route(("node3", "node1"))))

        self.test_graph.make_neighbor("node1", "node4", get_assigned_weight(Route(("node1", "node4"))))
        self.test_graph.make_neighbor("node4", "node1", get_assigned_weight(Route(("node4", "node1"))))
        self.test_graph.make_neighbor("node2", "node4", get_assigned_weight(Route(("node2", "node4"))))
        self.test_graph.make_neighbor("node4", "node2", get_assigned_weight(Route(("node4", "node2"))))
        self.test_graph.make_neighbor("node3", "node4", get_assigned_weight(Route(("node3", "node4"))))
        self.test_graph.make_neighbor("node4", "node3", get_assigned_weight(Route(("node4", "node3"))))
 
        for i in range(len(connroutes)):
            self.assertEqual(self.test_graph.get_weight(connroutes[i].origin,
              connroutes[i].destination), weights[i])

    def test_degree_eq(self):
        """
        Tests that the in degree and out degree of every node in the graph
        is equal.
        """
        nodes = self.test_graph.added_nodes

        for n in nodes:
            self.assertEqual(self.test_graph.get_indegree(n), self.test_graph.get_outdegree(n))

class IteratorTest(unittest.TestCase):
    
    def test_dfs_iterator(self):
        singleset = UndirectedAdjList()
        singleset.add_node("node1")
        dfs_iteration = ["node1"]
        dfs_result = [node for node in DFSIterator(singleset)]
        self.assertEqual(dfs_iteration, dfs_result)

        # Square four-node graph
        square = UndirectedAdjList()
        square.add_nodes(["node1", "node2", "node3", "node4"])
        square.make_neighbor("node1", "node2")
        square.make_neighbor("node2", "node3")
        square.make_neighbor("node3", "node4")
        square.make_neighbor("node4", "node1")
        
        # The test is that we should only iterate on square four times
        iteration_count = 0
        for node in DFSIterator(square):
            iteration_count += 1

        self.assertEqual(iteration_count, 4)

    def test_dfs_islands(self):
        four_single_islands = UndirectedAdjList()
        four_single_islands.add_node("node1")
        four_single_islands.add_node("node2")
        four_single_islands.add_node("node3")
        four_single_islands.add_node("node4")

        islander = lambda node: [n for n in DFSIslandIterator(four_single_islands, node)]

        self.assertEqual(["node1"], islander("node1"))
        self.assertEqual(["node2"], islander("node2"))
        self.assertEqual(["node3"], islander("node3"))
        self.assertEqual(["node4"], islander("node4"))

class UndirectedAdjMatTest(AdjacencyListTest):
    
    def _get_graph_instance(self):
        return AdjacencyMatrix()

    def test_add_nodes(self):
        # The standard tests...
        super(UndirectedAdjMatTest, self).test_add_nodes()
        # Then my own
        own_adjmat = AdjacencyMatrix()
        own_adjmat.add_node("cn1")
        own_adjmat.add_node("cn2")
        own_adjmat.add_node("cn3")
        own_adjmat.add_node("cn4")

        for node1 in own_adjmat.added_nodes:
            for node2 in own_adjmat.added_nodes:
                if node1 == node2:
                    print("Puzzle me: " + node1 + " " + node2)
                    self.assertEqual(own_adjmat.get_weight(node1, node2), 0)
                else:
                    self.assertEqual(own_adjmat.get_weight(node1, node2), AdjacencyMatrix.DISCONNECTED)

    def test_edge_count(self):
        # TODO Must reconsider the definition of edge count for graphs
        # super(UndirectedAdjMatTest, self).test_edge_count()
        self._construct_test_graph()
        self.assertEqual(5, self.test_graph.edge_count)

    def test_get_weight(self):
        """
        Almost the same as _construct_test_graph except that it generates random
        weights and tests for those weights.
        """
        weights = {}
        connseq = (("node1", "node2"), ("node1", "node3"), ("node1", "node4"),
          ("node2", "node4"), ("node3", "node4"))

        for connection in connseq:
            weights[connection] = random.randint(1, 100)

        self.test_graph.make_neighbor("node1", "node2", weights[("node1", "node2")])
        self.test_graph.make_neighbor("node1", "node3", weights[("node1", "node3")])

        self.test_graph.make_neighbor("node1", "node4", weights[("node1", "node4")])
        self.test_graph.make_neighbor("node2", "node4", weights[("node2", "node4")])
        self.test_graph.make_neighbor("node3", "node4", weights[("node3", "node4")])

        for connection in connseq:
            self.assertEqual(self.test_graph.get_weight(connection[0], connection[1]),
              weights[connection])
            self.assertEqual(self.test_graph.get_weight(connection[1], connection[0]),
              self.test_graph.get_weight(connection[0], connection[1]))

        # Test that, by default, the weight is 0.
        self.test_graph.add_nodes(("node5", "node6"))
        self.test_graph.make_neighbor("node5", "node6")
        self.assertEqual(self.test_graph.get_weight("node5", "node6"), 0)

    def test_neighbor(self):
        """
        Tests both make_neighbor and is_reachable functionality.
        """
        self.test_graph.make_neighbor("node1", "node2")
        self.assertTrue(self.test_graph.is_reachable("node1", "node2"))
        self.assertTrue(self.test_graph.is_reachable("node2", "node1"))
        self.assertRaises(NotInNodesException, self.test_graph.make_neighbor, self.test_node, "node1")

if __name__ == "__main__":
    unittest.main()
