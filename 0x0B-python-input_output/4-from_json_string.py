#!/usr/bin/python3
import json
"""this module opens a file and reads it."""


def from_json_string(my_str):
    """returns a JSON representation of an object"""
    return json.loads(my_str)
