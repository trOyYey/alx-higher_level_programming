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
        if attrs is not None:
            dictionary = dict()
            for i in attrs:
                try:
                    dictionary[i] = self.__dict__[i]
                except Exception:
                    pass
            return dictionary
        return self.__dict__
