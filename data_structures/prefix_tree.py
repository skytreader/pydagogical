#! /usr/bin/env python3

class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def filter_children(self, decider):
        return [child for child in self.children if decider(child)]

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
                children = self.tree.filter_children(lambda c: c == char)
                if children:
                    curnode = children[0]
                else:
                    curnode.children.append(create_prefix_linked_tree(word[idx:]))
        else:
            self.tree.children.append(create_prefix_linked_tree(word))
