#!/usr/bin/python3
"""this module checks the instance of an object/class"""


def is_same_class(obj, a_class):
    """returns whether something is the exact instance of a class"""
    if type(obj) == a_class:
        return(isinstance(obj, a_class))
    else:
        return False
