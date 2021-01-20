#!/usr/bin/python3
"""not a module but returns a list of available methods and attributes"""


def lookup(obj):
    """returns the list of available data from class"""
    return(dir(obj))
