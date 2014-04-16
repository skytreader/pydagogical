#! /usr/bin/env python3

from errors import NotInNodesException, DuplicateNodeException, CorruptedStructureException

import random
import unittest

"""
Package for graph data structures.
"""

# TODO Be able to remove connections
class Graph(object):
    """
    General class for graphs. You can add any object for nodes so long as
    (in)equality is defined among them.

    All methods that make use of the current set of nodes in the graph (not
    methods that add a node to the graph) should throw a NotInNodesException
    if given a node that is not yet in the graph.

    Implementing classes should indicate if they are representing directed or
    undirected graphs. Typically, the only difference between a class
    representing directed graphs and one representing undirected graphs is the
    make_neighbor method. Extending a directed/undirected graph for an
    undirected/directed graph should be trivial.
    """

    def __eq__(self, g2):
        """
        Two graphs are equal if and only if they are topographically similar and
        if their corresponding nodes contain the same data.
        """
        raise NotImplementedError("equality must be defined for Graph objects.")

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
    
    def add_nodes(self, nodes):
        """
        Convenience method that adds a set of nodes as given in the nodes
        iterable. This has a default implementation.
        """
        for node in nodes:
            if node in self.added_nodes:
                raise DuplicateNodeException(node)

        for node in nodes:
            self.add_node(node)

    @property
    def added_nodes(self):
        """
        Must return a set of all the nodes in this graph.
        """
        raise NotImplementedError("added_nodes is not supported by this implementation.")

    @property
    def edge_count(self):
        """
        Must return a count of all the edges in this graph.
        """
        raise NotImplementedError("edge_count is not supported by this implementation.")
    
    def remove_node(self, node):
        """
        Removes the given node from the graph. All incoming connections to this
        node are removed as well.
        """
        pass

    def make_neighbor(self, n1, n2, weight = 0):
        """
        Makes n2 reachable from n1 (but not necessarily n1
        from n2).
        """
        pass

    def get_weight(self, n1, n2):
        """
        Get the cost of going to n2 through n1. If there is no connection from
        n1 to n2, return None. If the graph represented is not weighted, raise
        a NotImplementedError. (By default, this throws NotImplementedError).
        """
        raise NotImplementedError("This does not represent a weighted graph.")

    def get_indegree(self, n1):
        """
        For a directed graph, the number of vertices which can
        directly reach n1 (i.e., those who have n1 as a neighbor).
        For undirected graphs, get_indegree should return the same
        value as get_outdegree.
        """
        pass

    # FIXME Is this still necessary since this is just equal to get_neighbors?
    def get_outdegree(self, n1):
        """
        For a directed graph, the number of vertices which
        directly leave n1 (i.e., the neighbors of n1). For
        undirected graphs, get_outdegree should return the
        same value as get_indegree.
        """
        pass

    def get_transpose(self, GraphType):
        """
        Returns a new graph with every edge reversed. That is, if A -> B in
        current graph, the graph returned will have A <- B. Of course, if the
        graph is undirected, this will not do anything.

        GraphType - A concrete implementation of the Graph class which will be
        used by this method to construct the transpose.
        """
        transpose_graph = GraphType()

        # Add every node in this graph into transpose_graph
        for node in self.added_nodes:
            transpose_graph.add_node(node)
        
        # Get their neighbors and reverse!
        for node in self.added_nodes:
            neighbors = self.get_neighbors(node)

            for neighbor in neighbors:
                transpose_graph.make_neighbor(neighbor, node)

        return transpose_graph

class AdjacencyLists(Graph):
    """
    Adjacency list representation of a graph. Note that no two nodes may be the
    same in a graph. Otherwise, we'll have confusion when making nodes adjacent.
    The graph created by default is directed.

    Convention:
    The graph is represented as a list-of-lists. The first element in each list
    is a specific node in the graph. The rest of the list represents nodes
    immediately reachable from the node represented by the first element.

    This can represent a directed, possibly weighted, graph.
    """

    def __init__(self):
        # self.__nodes is the adjacency list
        self.__nodes = dict()
        self.__added_nodes = set()
        self._edge_count = 0

    def get_neighbors(self, n1):
        """
        Returns a list of all the nodes reachable via n1. Returns an 
        empty list if n1 has no neighbors. Throws a NotInNodesException
        if n1 is not even in the graph.
        """
        if n1 in self.added_nodes:
            return list(map(lambda x: x[0], self.__nodes[n1]))
        else:
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

    @property
    def edge_count(self):
        return self._edge_count

    def add_node(self, node):
        # TODO Make thread safe
        if node in self.__added_nodes:
            raise DuplicateNodeException(node)
        else:
            self.__added_nodes.add(node)
            self.__nodes[node] = []

    def make_neighbor(self, n1, n2, weight = 0):
        """
        The connection created is only one-way: n2 will be
        reachable from n1 but n1 will not be necessarily
        reachable from n2.

        You can't represent self-loops here, unfortunately.
        """
        if n1 not in self.added_nodes:
            raise NotInNodesException(n1)

        if n2 not in self.added_nodes:
            raise NotInNodesException(n2)

        n1_list = self.__nodes[n1]
        if n2 not in n1_list:
            n1_list.append((n2, weight))
            self.__nodes[n1] = n1_list
            self._edge_count += 1

    def get_weight(self, n1, n2):
        if n2 not in self.get_neighbors(n1):
            return None
        else:
            n1_neighbors = self.__nodes[n1]
            # Find n2 and return its weight
            for node_weight in n1_neighbors:
                if node_weight[0] == n2:
                    return node_weight[1]

    def remove_node(self, node):
        """
        Requirement: list must not be acyclic.
        """
        # Remove from added_nodes
        self.__added_nodes.remove(node)

        # Remove outgoing connections
        self.__nodes.pop(node)

        # Remove incoming connections
        for n in tuple(self.__added_nodes):
            n_neighbors = self.__nodes[n]

            if node in n_neighbors:
                n_neighbors.remove(node)
                self.__nodes[n] = n_neighbors

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

class AdjacencyMatrix(Graph):
    """
    An AdjacenyMatrix representation of an _undirected_ graph. Usage of this
    class for weighted connections is valid as long as the weights are
    nonnegative.
    """

    DISCONNECTED = -1
    
    def __init__(self):
        self.__adjmat = []
        self.__added_nodes = set()
        self.__node_sequence = []
        self.__edge_count = 0

    @property
    def added_nodes(self):
        return self.__added_nodes

    @property
    def edge_count(self):
        return self.__edge_count

    def add_node(self, node):
        self.added_nodes.add(node)
        self.__node_sequence.insert(0, node)
        self.__adjmat.insert(0, [AdjacencyMatrix.DISCONNECTED for i in range(len(self.__node_sequence))])
        # Always costs nothing to get to yourself from yourself, at least initially.
        self.__adjmat[0][0] = 0
        
        for index, row in enumerate(self.__adjmat, start=1):
            row.insert(0, 0)

    def __get_index(self, node):
        """
        Return the index of this node in the matrix.

        (Idea: It might be faster if we implement this as a hash.)
        """
        if node not in self.added_nodes:
            raise NotInNodesException(node)

        for idx, n in enumerate(self.__node_sequence):
            if n == node:
                return idx
    
    def get_indegree(self, node):
        in_count = 0
        node_index = self.__get_index(node)

        for index, row in enumerate(self.__adjmat):
            if node_index != self.__node_sequence[index]:
                in_count += 1 if row[node_index] else 0

        return in_count

    def get_neighbors(self, node):
        neighbors = []
        node_index = self.__get_index(node)
        node_adjacency = self.__adjmat[node_index]

        for neighbor in node_adjacency:
            if neighbor:
                neighbors.insert(0, neighbor)

        return neighbors

    def get_outdegree(self, node):
        # This is undirected so this is totally valid
        return self.get_indegree(node)

    def get_weight(self, n1, n2):
        """
        Gets the cost of going to n2 via n1. Returns a negative value if n1 and
        n2 is not connected.
        """
        n1_index = self.__get_index(n1)
        n2_index = self.__get_index(n2)

        n1_adjacency = self.__adjmat[n1_index]
        return n1_adjacency[n2_index]
    
    def is_reachable(self, n1, n2):
        connection = self.get_weight(n1, n2)
        return connection >= 0
    
    def make_neighbor(self, n1, n2, weight=0):
        if n1 not in self.added_nodes:
            raise NotInNodesException(n1)

        if n2 not in self.added_nodes:
            raise NotInNodesException(n2)

        n1_index = self.__get_index(n1)
        n2_index = self.__get_index(n2)

        if self.__adjmat[n1_index][n2_index] == self.__adjmat[n2_index][n1_index] \
          and self.__adjmat[n1_index][n2_index] < 0:
            # Since this is undirected, toggling the direction marker should go
            # both ways
            n1_adjacency = self.__adjmat[n1_index]
            n1_adjacency[n2_index] = weight
    
            n2_adjacency = self.__adjmat[n2_index]
            n2_adjacency[n1_index] = weight
            self.__edge_count += 1
        elif self.__adjmat[n1_index][n2_index] != self.__adjmat[n2_index][n1_index]:
            raise CorruptedStructureException(type(self))

    def remove_node(self, node):
        node_index = self.__get_index(node)
        self.added_nodes.remove(node)
        self.__node_sequence.remove(node)

        # Fix the adjmat!
        # Remove the row
        temp_adjmat = self.__adjmat[0:node_index]
        temp_adjmat.extend(self.__adjmat[node_index + 1:len(self.__adjmat)])
        self.__adjmat = temp_adjmat

        for i, row in enumerate(self.__adjmat):
            self.__adjmat[i] = row[0:node_index]
            self.__adjmat[i].extend(row[node_index + 1:len(row)])

class UndirectedAdjList(AdjacencyLists):
    """
    Creates undirected graphs with an adjacency list
    representation.

    This may represent an undirected, possibly weighted, graph.
    """

    def __init__(self):
        super(UndirectedAdjList, self).__init__()
        self.__edge_count = 0
        self.__edge_set = []

    def make_neighbor(self, n1, n2, weight = 0):
        edge = set((n1, n2))

        if edge in self.__edge_set:
            pass
        else:
            self.__edge_set.append(edge)
            super(UndirectedAdjList, self).make_neighbor(n1, n2, weight)
            super(UndirectedAdjList, self).make_neighbor(n2, n1, weight)
            self.__edge_count += 1
            self._edge_count = self.__edge_count

############## HERE BE ITERATORS ##############

class DFSIterator(object):
    """
    Enumerates all the nodes in the graph via depth-first search. This is not
    concerened with path finding and so there is no way to specify where to
    start the search.

    Avoid modifying the graph structure while iteration. This will lead to
    undefined behaviors; it will not be guaranteed that the modifications will
    be reflected in the graph.
    """

    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.traversal_stack = []
        self.current_node = None

    def __iter__(self):
        return self

    def __next__(self):
        """
        A DFS driver method, incidentally designed to work for the iterator.
        """
        if self.visited == self.graph.added_nodes:
            raise StopIteration
        elif len(self.traversal_stack): # A current connected node is being traversed.
            return self._dfs()
        else:
            # Randomly pick a node that is not yet visited.
            unvisited = self.graph.added_nodes.difference(self.visited)
            random_node = random.choice(tuple(unvisited))
            return self._dfs(start_node = random_node)

    def _dfs(self, start_node = None):
        """
        Where all the magic of this iterator happens.

        Assumes that if start_node is None, traversal_stack is not empty.
        Otherwise, traversal_stack is empty.
        """
        # TODO Beware of possible cycles
        if start_node and start_node not in self.visited:
            # FIXME What about nodes reachable from themselves?
            self.traversal_stack.extend(self.graph.get_neighbors(start_node))
            self.visited.add(start_node)
            return start_node
        elif len(self.traversal_stack):
            # Note: Would've been an excellent use of a do-while construct
            next_node = self.traversal_stack.pop()
            while next_node in self.visited:
                next_node = self.traversal_stack.pop()
            self.traversal_stack.extend(self.graph.get_neighbors(next_node))
            self.visited.add(next_node)
            return next_node

class DFSIslandIterator(DFSIterator):
    """
    Traverses the graph in a depth-first manner and allows you to specify where
    to start. If the given graph has islands, only the nodes in the start_node's
    island will be enumerated by this iterator.

    As with DFIterator, modifications done on the graph while traversal is
    taking place may or may not reflect in the traversal.
    """
    
    #FIXME What if the specified start_node is not in the graph?

    def __init__(self, graph, start_node):
        super(DFSIslandIterator, self).__init__(graph)
        self.traversal_stack.append(start_node)

    def __next__(self):
        if len(self.traversal_stack):
            self.current_node = self.traversal_stack.pop()
            # Get the unvisited neighbors
            node_neighbors = set(self.graph.get_neighbors(self.current_node))
            # Difference from the visited nodes
            unvisited = node_neighbors.difference(self.visited)
            self.visited.add(self.current_node)
            return self.current_node
        else:
            raise StopIteration

############## HERE BE UNIT TESTS ##############

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

if __name__ == "__main__":
    unittest.main()
