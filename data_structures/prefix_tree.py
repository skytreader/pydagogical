#! /usr/bin/env python3

from enum import Enum

class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def filter_children(self, decider):
        # TODO This can be optimized by the fact that the, in a prefix tree,
        # the decider will return True for at most one child.
        return [child for child in self.children if child is not None and decider(child.data)]

    def __str__(self):
        children_str = "(%s)" % " ".join([str(c) for c in self.children])
        return "(%s %s)" % (self.data, children_str)

    def __repr__(self):
        return self.__str__()

class PrefixTreeSearchResults(Enum):
    """Prefix in tree but did not lead to terminal node."""
    PREFIX_FOUND = 0
    """Prefix in tree and lead to terminal node."""
    PREFIX_TERMINATED = 1
    """Prefix completely not found."""
    PREFIX_NOT_FOUND = 2

class PrefixTree(object):

    def __init__(self):
        self.tree = Node(None)

    def add_word(self, word):
        def create_prefix_linked_tree(word):
            child = None
            for w in word[::-1]:
                node = Node(w)
                if child:
                    node.children.append(child)
                child = node

            return child

        first_children = self.tree.filter_children(lambda c: c == word[0])
        # Here we are sure that this is always going to be a singleton
        if first_children:
            curnode = first_children[0]

            for idx, char in enumerate(word[1:]):
                children = curnode.filter_children(lambda c: c == char)
                if children:
                    curnode = children[0]
                else:
                    # None is a sentinel value signifying that a word ends in this
                    # letter too
                    curnode.children.append(None)
                    curnode.children.append(create_prefix_linked_tree(word[idx + 1:]))
                    break

            if curnode.children:
                curnode.children.append(None)
            else:
                self.tree.children.append(curnode)
        else:
            self.tree.children.append(create_prefix_linked_tree(word))

    def in_tree(self, prefix):
        curnode = self.tree

        for c in prefix:
            prefix_child = curnode.filter_children(lambda char: char == c)
            if prefix_child:
                curnode = prefix_child[0]
            else:
                return PrefixTreeSearchResults.PREFIX_NOT_FOUND

        if curnode.children and None not in curnode.children:
            return PrefixTreeSearchResults.PREFIX_FOUND
        else:
            return PrefixTreeSearchResults.PREFIX_TERMINATED
