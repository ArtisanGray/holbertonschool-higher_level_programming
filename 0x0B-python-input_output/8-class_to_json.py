#!/usr/bin/python3
"""this module opens a file, puts arguments in and saves it"""
import json


def class_to_json(obj):
    """returns the dictionary descriptiion"""
    return obj.__dict__
