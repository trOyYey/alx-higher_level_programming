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
