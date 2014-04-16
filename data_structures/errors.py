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

class CorruptedStructureException(Exception):
    """
    Thrown when suddenly a given invariant for a structure fails to hold.

    This is almost always programmer error. Concurrency bug? Sloppy programming?
    I'd check those.
    """
    
    def __init__(self, value):
        """
        The value is expected to be the class of the structure that was
        corrupted. Otherwise, you may not get meaningful exception messages.
        """
        self.value = value

    def __str__(self):
        return "Corrupted structure: " + str(self.value)
