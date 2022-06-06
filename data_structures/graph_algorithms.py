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

# Lifted from algorithms/snippets/grids.py
def __get_adjacent_4c(p, row_limit, col_limit):
    """
    Get the adjacent cells of the given point p assuming adjacency is 4-connected.
    """
    rows = []
    cols = []

    if p[0] == 0:
        rows.append(p[0] + 1)
    elif p[0] == (row_limit - 1):
        rows.append(p[0] - 1)
    else:
        rows.extend([p[0] + 1, p[0] - 1])

    if p[1] == 0:
        cols.append(p[1] + 1)
    elif p[1] == (col_limit - 1):
        cols.append(p[1] - 1)
    else:
        cols.extend([p[1] + 1, p[1] - 1])

    adjacent = []
    adjacent.extend([(r, p[1]) for r in rows])
    adjacent.extend([(p[0], c) for c in cols])

    return adjacent

def dijkstra(map):
    """
    This is Dijkstra's algorithm on a grid.

    TODO Rewrite for a generic graph.
    """
    width = len(map[0])
    height = len(map)

    is_in_tree = [[False for _ in range(width)] for _ in range(height)]
    distance = [[MAXINT for _ in range(width)] for _ in range(height)]
    parent = [[None for _ in range(width)] for _ in range(height)]
    distance[0][0] = 0

    # (row, col)!!!!
    curcell = (0, 0)
    next_cell = None
    weight = 0
    best_distance_so_far = MAXINT

    while not is_in_tree[curcell[0]][curcell[1]]:
        is_in_tree[curcell[0]][curcell[1]] = True
        neighbors = [
            adj for adj in __get_adjacent_4c(curcell, height, width) if map[adj[0]][adj[1]] != 1
        ]

        for n in neighbors:
            cand_distance = distance[curcell[0]][curcell[1]] + 1
            if distance[n[0]][n[1]] > cand_distance:
                distance[n[0]][n[1]] = cand_distance
                parent[n[0]][n[1]] = curcell

        # Find the closest non-tree node---at least one would've been "relaxed"
        # by the loop above. Could be improved by a priority queue.
        best_distance_so_far = MAXINT
        for row in range(height):
            for col in range(width):
                node_dist = distance[row][col]
                if not is_in_tree[row][col] and best_distance_so_far > node_dist:
                    best_distance_so_far = node_dist
                    curcell = (row, col)

    return distance[height - 1][width - 1] + 1
