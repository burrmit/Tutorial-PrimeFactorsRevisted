"""
Class for prime factors using iterable and generators.
"""

class prime_factors():
    """
    The prime factors class.
    """
    def __init__(self, num=0):
        """
        The init method for defining the proper variables within the class.
        """
        if not isinstance(num, int):
            raise ValueError
        self.number = num