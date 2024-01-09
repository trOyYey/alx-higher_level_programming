#!/usr/bin/python3
"""inherits_from method mod"""


def inherits_from(obj, a_class):
    """object is inherited from object"""
    return isinstance(obj, a_class) and type(obj) != a_class
