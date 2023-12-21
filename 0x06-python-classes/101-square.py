#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a named Square."""
    def __init__(self, size=0, position=(0, 0)):
        """initilationg"""
        self.size = size
        self.position = position

    def area(self):
        """area method returns current square area"""
        return self.__size ** 2

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

    @property
    def position(self):
        """gets position of suqare"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position of square"""
        if (not isinstance(value, tuple) or len(value) != 2 or type(value[0])
                != int or type(value[1]) != int or value[1] < 0 or
                value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """prints square as in print()"""
        if self.__size == 0:
            return ''
        str_ = self.__position[1] * '\n'
        for i in range(self.__size):
            str_ += self.__position[0] * ' ' + self.__size * '#'
            if i is not self.__size - 1:
                str_ += '\n'
        return str_
