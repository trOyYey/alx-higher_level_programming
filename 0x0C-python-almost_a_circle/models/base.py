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

    @classmethod
    def save_to_file(cls, list_objs):
        '''dict to file'''
        name = cls.__name__
        lst = [x.to_dictionary() for x in list_objs] if list_objs else []
        with open(f"{name}.json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """"converts a JSON string to a python object"""
        tmp = json_string
        if tmp is None or type(tmp) is not str or len(tmp) == 0:
            return "[]"
        return json.loads(json_string)
