#!/usr/bin/python3
"""class Square mod"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherited from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """square width getter"""
        return self.width

    @size.setter
    def size(self, value):
        """square width setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns magic string information"""
        ID = self.id
        SIZE = self.width
        X = self.x
        Y = self.y
        return "[Square] ({}) {}/{} - {}".format(ID, X, Y, SIZE)

    def __update(self, id=None, size=None, x=None, y=None):
        '''private method that updates instance attributes by **args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''updates instance attributes by no-keyword-or with-arguments.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns the square as a dictionary"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
