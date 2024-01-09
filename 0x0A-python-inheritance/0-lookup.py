#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """ lookup function

        Arguments:
            obj: object to check its information

        Return:
            list of attributes and methods of the object
    """
    return None if not obj else dir(obj)
