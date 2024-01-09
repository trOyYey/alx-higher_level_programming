#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry here we go again"""
    def area(self):
        """error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not value > 0:
            raise ValueError("{} must be greater than 0".format(name))
