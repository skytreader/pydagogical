"""
Package for graph data structures.
"""

class Graph(object):
    """
    General class for graphs.
    """

    def is_reachable(n1, n2):
        """
        Returns true if we can go to n2 via n1. Note
        that if the graph is directed, is_reachable(n1, n2)
        might not always mean is_reachable(n2, n1) .
        """
        pass

    def get_neighbors(n1):
        """
        Returns all nodes reachable via n1.
        """
        pass
    
    def add_node(node):
        """
        Adds this node to the graph.
        """
        pass
    
    def remove_node(node):
        """
        Removes the given node from the graph. All incoming
        connections to this node are removed as well.
        """
        pass

    def make_neighbor(n1, n2):
        """
        Makes n2 reachable from n1 (but not necessarily n1
        from n2).
        """
        pass
