#!/usr/bin/python3
"""Square class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size):
        """init Square values"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Method calculating area of square.'''
        return self.__size ** 2

    def __str__(self):
        """returns square as magic string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
