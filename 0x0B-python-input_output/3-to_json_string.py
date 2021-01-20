#!/usr/bin/python3
import json
"""this module opens a file and reads it."""


def to_json_string(my_obj):
    """returns a JSON representation of an object"""
    return json.dumps(my_obj)
