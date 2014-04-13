"""
All the exceptions I might use.
"""

class NotInNodesException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "These node(s) are not yet in the structure: " + repr(self.value)

class DuplicateNodeException(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Already added to the structure: " + repr(self.value)
