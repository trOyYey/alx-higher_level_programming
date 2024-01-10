#!/usr/bin/python3
"""def write_file function"""


def write_file(filename="", text=""):
    """writing text to a file"""
    with open(filename, "w", encoding='utf-8') as datafile:
        return datafile.write(text)
