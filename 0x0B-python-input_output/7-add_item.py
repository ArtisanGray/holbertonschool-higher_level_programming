#!/usr/bin/python3
"""this module opens a file, puts arguments in and saves it"""
import json
import sys


def load_from_json_file(filename):
    """loads a JSON representation of an object from a new file"""
    with open(filename, 'r+') as o_file:
        return json.load(o_file)


def save_to_json_file(my_obj, filename):
    """writes a JSON representation of an object to a new file"""
    with open(filename, 'w+') as o_file:
        json.dump(my_obj, o_file)

try:
    new_l = list(load_from_json_file("add_item.json"))
except:
    new_l = []
args = sys.argv[1:]
for item in args:
    new_l.append(item)
save_to_json_file(new_l, "add_item.json")
