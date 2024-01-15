#!/usr/bin/python3
'''mod for the rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

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
        self.__height = value

    @property
    def width(self):
        '''width of the rect'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def x(self):
        '''x of the rect'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of the rect'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
