"""
Class for prime factors using iterable and generators.
"""

class prime_factors:
    """
    The prime factors class.
    """
    def __init__(self, num=0):
        """
        The init method for defining the proper variables
        within the class.
        """
        self.number = int(num)
        self.factor = 2
        self.factors = []

    def __iter__(self):
        """
        This is the iter function that will allow the class to
        be iterable.
        """
        return self

    def __next__(self):
        """
        This method allows the class to continue to the next
        iterator.
        """
        if self.number > 1:
            while self.number % self.factor == 0:
                self.factors.append(self.factor)
                self.number = int(self.number / self.factor)

            while self.number >= self.factor:
                self.factor += 1
                while self.number % self.factor == 0:
                    self.factors.append(self.factor)
                    self.number = int(self.number / self.factor)
        else:
            raise StopIteration

        return self.factors
