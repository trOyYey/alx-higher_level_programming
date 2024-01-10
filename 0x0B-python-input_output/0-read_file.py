#!/usr/bin/python3
"""def read_file mod"""


def read_file(filename=""):
    """prints all content of a specified file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
