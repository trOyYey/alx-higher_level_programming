#!/usr/bin/python3
"""Rectangle mod"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass of BaseGeometry"""
    def __init__(self, width, height):
        """initialize baseGeometry values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns  Area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle in format magic string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
