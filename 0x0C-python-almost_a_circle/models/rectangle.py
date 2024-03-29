#!/usr/bin/python3
'''mod for the rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor of the rect'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of this rect'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height of the rect'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value, False)
        self.__height = value

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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''calculates the  area of the rectangle'''
        return self.width * self.height

    def display(self):
        """prints rect in form of #'s"""
        print('\n' * self.__y, end='')
        for x in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        '''returns magic string information'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''private method which updates instance attributes'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''updates instance attributes by no-keyword &-or keyword args'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''returns dictionary of rectangle'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
