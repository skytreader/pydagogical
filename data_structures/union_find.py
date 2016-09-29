#! /usr/bin/env python3

class DataNode(object):
    
    def __init__(self, data, parent=None)
        self.data = data
        self.parent = parent
        parent_weight = parent.weight if parent else 0
        self.weight = 1 + parent_weight

    def find(self):
        """
        Find the ultimate parent of this node.

        Haha it is "recursive". I wonder if this is good.
        """
        if self.parent:
            return self.parent.find()
        else:
            return self

    def union(self, other_node):
        if self.weight > other_node.weight:
            other_parent = other_node.find()
            other_parent.parent = self.parent
            other_parent.weight += self.weight
        else:
            self.parent = other_node.find()
            self.weight += other_node.weight

class UnionFind(object):
    """
    A disjointed set structure. This assumes that the data added to it cannot
    be overwritten.
    """
    
    def __init__(self):
        self.data2node = {}

    def add_object(self, data):
        if self.data2node.get(data):
            raise Exception("%s data already exists. Can't overwrite." % data)
        else:
            self.data2node[data] = DataNode(data)

    def make_equal(self, d1, d2):
        if not self.data2node.get(d1):
            self.add_object(d1)

        if not self.data2node.get(d2):
            self.add_object(d2)

        self.data2node[d1].union(self.data2node[d2])

    def is_equal(self, d1, d2):
        """
        Again, only works because of the assumption that data here cannot be
        overwritten.

        Also assumes that the data given to this object can be compared.
        """
        return d1.find().data == d2.find().data
