import json

from binary_tree import BinaryTree
from graphs import Graph

"""
Load a json from (as from EPiQueue) and transform it into an instance of one of
the data structure classes in this package.
"""

class JSONLoader(object):
    """
    All modules meant to parse JSON should extend this.

    A typical pattern is as follows:
     - The subclass would take a filename for its constructor. The subclass
       would then invoke the constructor of JSONLoader (it would know its
       return_class, of course).
     - The subclass needs to implement the load method. The parsed JSON object
       can be referenced via self._parsed_json. The load method should return
       an instance of the specified return_class.
    """
    
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
        # Traverse the JSON-binary tree structure in pre order to reconstruct
        # it as a Python object.
        # return self.__recursive_load(self._parsed_json)
        righties = []
        parent_pointer = BinaryTree(self._parsed_json["node_data"])
        root_pointer = parent_pointer

        node = self._parsed_json

        while True:
            while node["left_son"] is not None:
                next_node = BinaryTree(node["left_son"]["node_data"])

                if node["right_son"]:
                    righties.append(node["right_son"])

                parent_pointer.left_son = next_node
                node = node["left_son"]
            
            if len(righties):
                right_node = righties.pop()
            else:
                break
        
        return root_pointer
    
    def __recursive_load(self, treemap):
        if treemap is None:
            return None

        btree = BinaryTree(treemap["node_data"])
        left_tree = self.__recursive_load(treemap["node_data"]["left_son"])
        right_tree = self.__recursive_load(treemap["node_data"]["right_son"])
        btree.left_son = left_tree
        btree.right_son = right_tree

        return btree

class GraphParser(JSONLoader):
    
    def __init__(self, filename):
        super(self, JSONLoader).__init(filename, Graph)

    def __load_adjancency_list(self):
        pass

    def __load_adjacency_matrix(self):
        pass

    def load(self):
        if self._parsed_json["is_matrix"]:
            return self.__load_adjacency_matrix()
        else:
            return self.__load_adjacency_list()
