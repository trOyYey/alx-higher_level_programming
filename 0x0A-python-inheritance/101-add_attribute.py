#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, key, value):
    """adds a new attribute to object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
