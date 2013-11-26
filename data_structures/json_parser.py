import json

from binary_tree import BinaryTree

"""
Load a json from (as from EPiQueue) and transform it into an instance of one of
the data structure classes in this package.
"""

class JSONLoader(object):
    
    def __init__(self, filename, return_class):
        self._return_class = return_class
        self._parsed_json = None

        with open(filename) as json_file:
            self._parsed_json = json.load(json_file)
    
    @property
    def return_class(self):
        """
        Returns the class of load()'s return value.
        """
        return self._return_class

    def load(self):
        """
        Return an instance of a data structure class base
        """
        raise NotImplementedError("load must be implemented.")

class BinaryTreeParser(JSONLoader):
    """
    Create an instance with the filename of the json file and call load. load
    should return an instance of the data structure class.
    """

    def __init__(self, filename):
        super(JSONLoader, self).__init__(filename, BinaryTree)

    def load(self):
        # Traverse the JSON-binary tree structure in pre order to.
        return self.__recursive_load(self._parsed_json)
    
    def __recursive_load(self, treemap):
        if treemap is None:
            return None

        btree = BinaryTree(treemap["node_data"])
        left_tree = self.__recursive_load(treemap["node_data"]["left_son"])
        right_tree = self.__recursive_load(treemap["node_data"]["right_son"])
        btree.left_son = left_tree
        btree.right_son = right_tree

        return btree
