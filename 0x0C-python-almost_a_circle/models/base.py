#!/usr/bin/python3
"""base class mod"""
from json import dumps, loads

class Base:
    """base class for all geometric forms"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"dictionary to JSON"""
        tmp = list_dictionaries
        if tmp is None or type(tmp) is not list:
            return "[]"
        elif len(tmp) == 0:
            return "[]"
        else:
            return dumps(list_dictionaries)
