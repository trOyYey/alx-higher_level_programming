#!/usr/bin/python3
"""funtion mod to class student and returns dictionary discrp """


class Student:
    """Student class representative"""
    def __init__(self, first_name, last_name, age):
        """initialization with 3 attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dicttionary"""
        return self.__dict__
