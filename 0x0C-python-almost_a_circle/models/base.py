#!/usr/bin/python3
"""base class mod"""
from json import dumps, loads
from os.path import exists

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
        '''saves JSON string in file'''
        name = cls.__name__
        lst = [x.to_dictionary() for x in list_objs] if list_objs else []
        with open(f"{name}.json", "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """"converts a JSON string to a python object"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''creates or updates class values from dictionary list'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            fresh_class = Rectangle(1, 1)
        elif cls is Square:
            fresh_class = Square(1)
        else:
            fresh_class = None
        fresh_class.update(**dictionary)
        return fresh_class

    @classmethod
    def load_from_file(cls):
        '''creates new object from JSON string inside a  file.'''
        name = cls.__name__ + ".json"
        if not exists(name):
            return []
        with open(name, "r+", encoding="utf-8") as file:
            tmp = cls.from_json_string(file.read())
        return [cls.create(**a) for a in tmp]
