#!/usr/bin/python3
"""this module opens a file and reads it."""
import json


def save_to_json_file(my_obj, filename):
    """writes a JSON representation of an object to a new file"""
    with open(filename, 'w+') as o_file:
        json.dump(my_obj, o_file)
