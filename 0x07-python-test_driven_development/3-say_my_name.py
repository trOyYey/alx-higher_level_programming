#!/usr/bin/python3
"""
    say_my_name mod using doctest
    to test cases
"""


def say_my_name(first_name, last_name=""):
    """prints given names.

    Argumentss:
        first_name: 1st name.
        last_name: last name.

    Raises:
        TypeError: first_name or last_name not strings.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/3-say_my_name.txt")
