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
