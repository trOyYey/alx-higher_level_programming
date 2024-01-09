#!/usr/bin/python3
"""MyInt mod"""


class MyInt (int):
    """ MyInt class inherites from int all attributes"""
    def __eq__(self, other):
        """Overrides int == opration"""
        return (int(self) != other)

    def __ne__(self, other):
        """Overrides int != opration"""
        return (int(self) == other)
