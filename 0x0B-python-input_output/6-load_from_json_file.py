#!/usr/bin/python3
"""this module opens a file and reads it."""
import json


def load_from_json_file(filename):
    """loads a JSON representation of an object from a new file"""
    with open(filename, 'r') as o_file:
        return json.load(o_file)
