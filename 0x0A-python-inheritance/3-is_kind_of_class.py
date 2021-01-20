#!/usr/bin/python3
"""this module checks if two instances are the same class and type"""


def is_kind_of_class(obj, a_class):
    """checks if an object is subclass or inherited"""
    return(isinstance(obj, a_class))
