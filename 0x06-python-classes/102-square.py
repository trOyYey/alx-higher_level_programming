#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a named Square."""
    def __init__(self, size=0):
        """initilationg"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method returns current square area"""
        return self.__size ** 2

    def __lt__(self, other):
            return self.area() < other.area()

    def __gt__(self, other):
            return self.area() > other.area()

    def __le__(self, other):
            return self.area() <= other.area()

    def __ge__(self, other):
            return self.area() >= other.area()

    def __ne__(self, other):
            return self.area() != other.area()

    def __eq__(self, other):
            return self.area() == other.area()

        @property
    def size(self):
        """gets size of the squar"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
