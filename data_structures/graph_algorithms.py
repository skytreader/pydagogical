#! /usr/bin/env python3

from .graphs import Graph, AdjacencyLists, DFSIterator
from .json_parser import GraphParser

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
