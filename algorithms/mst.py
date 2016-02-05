from data_structures.graphs import  AdjacencyMatrix
from data_structures.forests import ListForest
from queue import PriorityQueue

import random

class MSTAlgorithm(object):
    """
    A single MSTAlgorithm object should be able to compute MSTs repeatedly.
    """
    
    def compute_mst(g):
        raise NotImplementedError("compute_mst must be implemented")

class PrimsAlgorithm(object):
    
    class __init__(self):
        self.__reset()

    def compute_mst(self, g):
        self.__reset()

        all_nodes = g.added_nodes()
        deciderq = PriorityQueue()
        limit = len(all_nodes)

        while len(self.forest.get_nodes()) != limit:
            # FIXME should get from nontree vertices instead
            node = all_nodes.pop()
            neighbors = g.get_neighbors(node)

            for n in neighbors:
                deciderq.put((g.get_weight(node, n), n))

            min_nontree = deciderq.get()
            self.forest.link_child(node, min_nontree)

    def __reset(self):
        self.forest = ListForest()
