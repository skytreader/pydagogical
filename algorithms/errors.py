class InvalidParameterException(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Invalid value for a parameter: " + repr(self.value)
