import sys

sys.path.append("..")

from data_structures.graphs import AdjacencyLists

COLORS = set(("RED", "GREEN", "BLUE", "CYAN", "MAGENTA", "YELLOW"))

def get_available_color(taken_colors):
    """
    taken_colors should be a set
    """
    return COLORS.difference(taken_colors)

def color(g):
    """
    Returns a dictionary with the nodes of the graph as keys and the assigned
    colors as values.
    
    g is assumed to be an instance of AdjacencyLists.
    """
    nodes = tuple(g.added_nodes)
    coloring = {}

    for node in nodes:
        neighbors = g.get_neighbors(node)
        adjacent_colors = set()

        for neighbor in neighbors:  
            if coloring.get(neighbor):
                adjacent_colors.add(coloring.get(neighbor))
        
        # If no more colors are available, will throw IndexOutOfBounds exception
        node_color = tuple(get_available_color(adjacent_colors))[0]
        
        coloring[node] = node_color

   return coloring
