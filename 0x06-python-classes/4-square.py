#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a Square."""
    def __init__(self, size=0):
        """initilazing the size value of Square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method returns current square area"""
        return self.__size ** 2
    @property
    def size(self):
        """returns value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
