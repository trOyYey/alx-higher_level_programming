#!/usr/bin/python3
"""def funtion mod to return dictionary from simpledata"""


def class_to_json(obj):
    """changes object to dictionary"""
    return obj.__dict__
