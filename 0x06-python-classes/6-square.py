#!/usr/bin/python3
"""Square module."""


class Square:
    """Defining a named Square."""
    def __init__(self, size=0, position=(0, 0)):
        """initilazing the size value of Square"""
        self.size = size
        self.position = position

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
        
    @position.setter
    def position(self, value):
        """sets value of position"""
        if (not isinstance(value, tuple) or len(value) != 2 or type(value[0])
                != int or type(value[1]) != int or value[1] < 0 or
                value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints square #"""
        if self.__size == 0:
            print()
            return
        print(self.__position[1] * '\n', end='', sep='')
        for x in range(self.__size):
            print(self.__position[0] * ' ', self.__size * '#', sep='')
