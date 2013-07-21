#! /usr/bin/env python3

import unittest

"""
Package for graph data structures.
"""

class NotInNodesException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "These node(s) are not yet added to the graph: " + repr(self.value)

class DuplicateNodeException(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Already added to the graph: " + repr(self.value)

class Graph(object):
    """
    General class for graphs. Add objects for nodes and equality must
    be defined for the nodes.

    All methods that make use of the current set of nodes in the graph
    (not methods that add a node to the graph) should throw a
    NotInNodesException if given a node that is not yet in the graph.
    """

    def is_reachable(self, n1, n2):
        """
        Returns true if we can go to n2 via n1. Note
        that if the graph is directed, is_reachable(n1, n2)
        might not always mean is_reachable(n2, n1) .

        Mathematically, the call is_reachable(n1, n2) will
        return true iff n2 is in get_neighbors(n1) .
        """
        pass

    def get_neighbors(self, n1):
        """
        Returns all nodes reachable via n1.
        """
        pass
    
    def add_node(self, node):
        """
        Adds this node to the graph.
        """
        pass
    
    def remove_node(self, node):
        """
        Removes the given node from the graph. All incoming
        connections to this node are removed as well.
        """
        pass

    def make_neighbor(self, n1, n2):
        """
        Makes n2 reachable from n1 (but not necessarily n1
        from n2).
        """
        pass

    def get_indegree(self, n1):
        """
        For a directed graph, the number of vertices which can
        directly reach n1 (i.e., those who have n1 as a neighbor).
        For undirected graphs, get_indegree should return the same
        value as get_outdegree.
        """
        pass

    def get_outdegree(self, n1):
        """
        For a directed graph, the number of vertices which
        directly leave n1 (i.e., the neighbors of n1). For
        undirected graphs, get_outdegree should return the
        same value as get_indegree.
        """
        pass

class AdjacencyLists(Graph):
    """
    Adjacency list representation of a graph. Note that no two nodes
    may be the same in a graph. Otherwise, we'll have confusion when
    making nodes adjacent.

    Convention:
    The graph is represented as a list-of-lists. The first element
    in each list is a specific node in the graph. The rest of the
    list represents nodes immediately reachable from the node
    represented by the first element.
    """

    def __init__(self):
        # self.__nodes is the adjacency list
        self.__nodes = []
        self.__added_nodes = set()

    def get_neighbors(self, n1):
        """
        Returns a list of all the nodes reachable via n1. Returns an 
        empty list if n1 has no neighbors. Throws a NotInNodesException
        if n1 is not even in the graph.
        """
        for row in self.__nodes:
            if row[0] == n1:
                return row[1:len(row)]

        raise NotInNodesException(n1)

    def is_reachable(self, n1, n2):
        n1_neighbors = self.get_neighbors(n1)
        
        if n1_neighbors is not None:
            return n2 in n1_neighbors
        else:
            return False
    
    @property
    def added_nodes(self):
        """
        Returns a set of all the nodes in this graph.
        """
        return self.__added_nodes

    def add_node(self, node):
        # TODO Make thread safe
        if node in self.__added_nodes:
            raise DuplicateNodeException(node)
        else:
            self.__added_nodes.add(node)
            self.__nodes.append([node])

    def make_neighbor(self, n1, n2):
        """
        The connection created is only one-way: n2 will be
        reachable from n1 but n1 will not be necessarily
        reachable from n2.
        """
        if n1 not in self.added_nodes or n2 not in self.added_nodes:
            raise NotInNodesException([n1, n2])
        nodes = self.__get_nodelist()
        n1_index = nodes.index(n1)
        # Check if the connection already exists. If so, do
        # not make it redundant!
        if n2 not in self.__nodes[n1_index]:
            self.__nodes[n1_index].append(n2)

    def __get_nodelist(self):
        return list(map(lambda x: x[0], self.__nodes))

    def remove_node(self, node):
        """
        Requirement: list must not be acyclic.
        """
        # Remove from added_nodes
        self.__added_nodes.remove(node)

        # Remove incoming connections
        for index, row in enumerate(self.__nodes):
            neighbors = row[1:len(row)]
            
            if node in neighbors:
                neighbors.remove(row)

            # Check if the row is the adjacency list
            # for the given node and delete.
            if row[0] == node:
                self.__nodes.remove(row)

    def get_outdegree(self, n1):
        """
        Returns the number of nodes reachable from n1. Throws
        a NotInNodesException if n1 is not in the graph.
        """
        neighbors = self.get_neighbors(n1)
        return len(neighbors)

    def get_indegree(self, n1):
        """
        Returns the number of nodes that can reach n1. Throws
        a NotInNodesException if n1 is not in the graph.
        """
        if n1 in self.added_nodes:
            outcount = 0
            
            for node in self.added_nodes:
                outcount += 1 if self.is_reachable(node, n1) else 0

            return outcount
        else:
            raise NotInNodesException(n1)

class UndirectedAdjList(AdjacencyLists):
    """
    Creates undirected graphs with an adjacency list
    representation.
    """

    def make_neighbor(self, n1, n2):
        super(UndirectedAdjList, self).make_neighbor(n1, n2)
        super(UndirectedAdjList, self).make_neighbor(n2, n1)

############## HERE BE UNIT TESTS ##############

class AdjacencyListTest(unittest.TestCase):
    """
    To test:
        - Behavior when introducing deep and shallow copies.
    """

    def setUp(self):
        self.four_nodes = AdjacencyLists()
        self.four_nodes.add_node("node1")
        self.four_nodes.add_node("node2")
        self.four_nodes.add_node("node3")
        self.four_nodes.add_node("node4")

        self.test_node = "test_node"

    def test_add_node(self):
        """
        Test cases:
            - Introduce a new node -- should be added
            - Introduce an already-added node - must throw a
              DuplicateNodeException
        """
        self.four_nodes.add_node(self.test_node)
        self.assertTrue(self.test_node in self.four_nodes.added_nodes)
        self.assertRaises(DuplicateNodeException, self.four_nodes.add_node, "node1")

    def test_remove_node(self):
        """
        Add a node, check if added indeed. Then, remove that node
        and check that it is not there anymore.
        """
        self.four_nodes.add_node(self.test_node)
        self.assertTrue(self.test_node in self.four_nodes.added_nodes)
        
        self.four_nodes.remove_node(self.test_node)
        self.assertTrue(self.test_node not in self.four_nodes.added_nodes)

    def test_neighbor(self):
        """
        Tests both make_neighbor and is_reachable functionality.
        """
        self.four_nodes.make_neighbor("node1", "node2")
        self.assertTrue(self.four_nodes.is_reachable("node1", "node2"))
        self.assertFalse(self.four_nodes.is_reachable("node2", "node1"))
        self.assertRaises(NotInNodesException, self.four_nodes.make_neighbor, self.test_node, "node1")

    def construct_four_nodes(self):
        """
        Utility test function to connect the four nodes of self.four_nodes.
        After calling this function, get_neighbors_test should pass.
        """
        self.four_nodes.make_neighbor("node1", "node2")
        self.four_nodes.make_neighbor("node2", "node1")
        self.four_nodes.make_neighbor("node1", "node3")
        self.four_nodes.make_neighbor("node3", "node1")

        self.four_nodes.make_neighbor("node1", "node4")
        self.four_nodes.make_neighbor("node4", "node1")
        self.four_nodes.make_neighbor("node2", "node4")
        self.four_nodes.make_neighbor("node4", "node2")
        self.four_nodes.make_neighbor("node3", "node4")
        self.four_nodes.make_neighbor("node4", "node3")

    def get_neighbors_test(self):
        n1_neighbors = self.four_nodes.get_neighbors("node1")
        n2_neighbors = self.four_nodes.get_neighbors("node2")
        n3_neighbors = self.four_nodes.get_neighbors("node3")
        n4_neighbors = self.four_nodes.get_neighbors("node4")

        n1_expected_neighbors = set(["node2", "node3", "node4"])
        self.assertEqual(n1_expected_neighbors, set(n1_neighbors))

        n2_expected_neighbors = set(["node4", "node1"])
        self.assertEqual(n2_expected_neighbors, set(n2_neighbors))

        n4_expected_neighbors = set(["node2", "node1", "node3"])
        self.assertEqual(n4_expected_neighbors, set(n4_neighbors))

        n3_expected_neighbors = set(["node1", "node4"])
        self.assertEqual(n3_expected_neighbors, set(n3_neighbors))

        # Isolated node test
        self.four_nodes.add_node("five")
        self.assertTrue(self.four_nodes.get_neighbors("five") == [])

        # NotInNodesException test
        self.assertRaises(NotInNodesException, self.four_nodes.get_neighbors, "does not exist")

    def test_get_neighbors(self):
        self.construct_four_nodes()
        self.get_neighbors_test()

    def test_get_indegree(self):
        n1_neighbors = self.four_nodes.get_neighbors("node1")
        self.assertEqual(self.four_nodes.get_indegree("node1"), len(n1_neighbors))

        # NotInNodesException test
        self.assertRaises(NotInNodesException, self.four_nodes.get_indegree, "does not exist")

    def test_get_outdegree(self):
        n1_neighbors = self.four_nodes.get_neighbors("node1")
        self.assertEqual(self.four_nodes.get_outdegree("node1"), len(n1_neighbors))

class UndirectedAdjListTest(AdjacencyListTest):
    
    def setUp(self):
        super(UndirectedAdjListTest, self).setUp()

        self.four_nodes = UndirectedAdjList()
        self.four_nodes.add_node("node1")
        self.four_nodes.add_node("node2")
        self.four_nodes.add_node("node3")
        self.four_nodes.add_node("node4")

    def test_neighbor(self):
        self.four_nodes.make_neighbor("node1", "node2")
        self.assertTrue(self.four_nodes.is_reachable("node1", "node2"))
        self.assertTrue(self.four_nodes.is_reachable("node2", "node1"))

    def test_degree_eq(self):
        """
        Tests that the in degree and out degree of every node in the graph
        is equal.
        """
        nodes = self.four_nodes.added_nodes

        for n in nodes:
            self.assertEqual(self.four_nodes.get_indegree(n), self.four_nodes.get_outdegree(n))

if __name__ == "__main__":
    unittest.main()
