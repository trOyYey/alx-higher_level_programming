#!/usr/bin/python3
"""def append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
        adds new_string after finding specified string in a line
    """
    with open(filename, encoding="utf-8") as file:
        string = ""
        for line in file:
            if search_string in line:
                line += new_string
            string += line
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(string)
