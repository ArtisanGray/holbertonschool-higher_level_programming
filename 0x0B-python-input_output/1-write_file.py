#!/usr/bin/python3
"""this module opens a file and reads it."""


def write_file(filename="", text=""):
    """this function writes to a file"""
    with open(filename, 'w+') as o_file:
        o_file.write(text)
    return(len(text))
