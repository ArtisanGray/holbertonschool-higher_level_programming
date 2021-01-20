#!/usr/bin/python3
"""This module uses inheritance from the int type"""


class MyInt(int):
    """Myint inherited from int"""

    def __init__(self, value):
        """initialization function"""
        self.value = value

    def __ne__(self, other):
        """ 'magic method' used to manipulate the output of some operators"""
        return self.value == other

    def __eq__(self, other):
        """ 'magic method' used to manipulate the output of some operators"""
        return self.value != other
