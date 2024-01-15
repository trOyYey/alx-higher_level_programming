#!/usr/bin/python3
'''mod for the rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        '''height of the rect'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value)
        self.__height = value

    @property
    def width(self):
        '''width of the rect'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value)
        self.__width = value

    @property
    def x(self):
        '''x of the rect'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of the rect'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value

    def validate_attributes(self, name, value, eq=True):
        '''method validating the value and error messages'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''calculates the  area of the rectangle'''
        return self.width * self.height
