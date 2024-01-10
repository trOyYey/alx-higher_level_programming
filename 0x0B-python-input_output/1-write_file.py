#!/usr/bin/python3
"""def write_file function"""


def write_file(filename="", text=""):
    """writing text to a file"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
