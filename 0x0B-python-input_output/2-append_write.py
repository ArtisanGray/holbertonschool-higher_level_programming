#!/usr/bin/python3
"""this module opens a file and reads it."""


def append_write(filename="", text=""):
    """this function writes to a file"""
    with open(filename, 'a') as o_file:
        o_file.write(text)
    return(len(text))
