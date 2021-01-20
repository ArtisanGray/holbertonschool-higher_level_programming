#!/usr/bin/python3
"""this module checks the instance of an object/class"""


def inherits_from(obj, a_class):
    """returns whether something is child of a class"""
    if type(obj) is not a_class:
        return(issubclass(type(obj), a_class))
    else:
        return False
