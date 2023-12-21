#!/usr/bin/python3
"""Square module."""
import math


class MagicClass:
    """Defining a named circle"""
    def __init__(self, radius=0):
        """initilation"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area method return are of circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of our magical class"""
        return (2 * math.pi * self.__radius)
