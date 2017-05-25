#! /usr/bin/env python3

from enum import Enum

class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def filter_children(self, decider):
        # TODO This can be optimized by the fact that the, in a prefix tree,
        # the decider will return True for at most one child.
        return [child for child in self.children if decider(child.data)]

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

            print(child)
            return child

        print("Adding %s" % word)
        first_children = self.tree.filter_children(lambda c: c == word[0])
        # Here we are sure that this is always going to be a singleton
        if first_children:
            curnode = first_children[0]

            for idx, char in enumerate(word[1:]):
                print("considering %s %s" % (char, idx))
                print("children is %s" % curnode.children)
                children = curnode.filter_children(lambda c: c == char)
                if children:
                    print("exists so continue")
                    curnode = children[0]
                else:
                    print("does not exist anymore so we just add")
                    curnode.children.append(create_prefix_linked_tree(word[idx + 1:]))
                    break
            self.tree.children.append(curnode)
        else:
            print("There are no children so we just add")
            self.tree.children.append(create_prefix_linked_tree(word))

    def in_tree(self, prefix):
        curnode = self.tree

        for c in prefix:
            print("checking %s" % c)
            prefix_child = curnode.filter_children(lambda char: char == c)
            if prefix_child:
                curnode = prefix_child[0]
            else:
                return PrefixTreeSearchResults.PREFIX_NOT_FOUND

        if curnode.children:
            return PrefixTreeSearchResults.PREFIX_FOUND
        else:
            return PrefixTreeSearchResults.PREFIX_TERMINATED
