"""
Package for graph data structures.
"""

class NotInNodesException(Exception):
    """
    Will I really actually use this?
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Graph(object):
    """
    General class for graphs. Add objects for nodes and equality must
    be defined for the nodes.
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

class AdjacencyLists(Graph):
    """
    Adjacency list representation of a graph.
    """

    def __init__(self):
        self.__nodes = []

    def get_neighbors(self, n1):
        """
        Returns a list of all the nodes reachable via n1.
        Returns None if n1 has no neighbors or if n1 is not
        even in the graph.
        """
        for row in self.__nodes:
            if row[0] == n1:
                return row[1:len(row)]

        return None

    def is_reachable(self, n1, n2):
        n1_neighbors = self.get_neighbors(n1)
        
        if n1_neighbors is not None:
            return n2 in n1_neighbors
        else:
            return False
    
    def get_nodelist(self):
        """
        Returns a tuple of all the nodes in this graph.
        """
        return tuple(map(lambda x: x[0], self.___nodes))

    def add_node(self, node):
        # FIXME Shall I check if node is already in the graph?
        self.__nodes.append([node])

    def make_neighbor(self, n1, n2):
        nodes = self.get_nodelist()
        n1_index = nodes.index(n1)
        self.__nodes[n1_index].append(n2)

    def remove_node(self, node):
        """
        Requirement: list must not be acyclic.
        """
        for row in self.__nodes:
            neighbors = row[1:len(row)]
            
            if node in neighbors:
                neighbors.remove(row)
