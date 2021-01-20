#!/usr/bin/python3
"""this module opens a file and reads it."""


def read_file(filename=""):
    """this function reads a file"""
    with open(filename, 'r') as o_file:
        print(o_file.read(), end="")
