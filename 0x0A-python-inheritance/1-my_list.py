#!/usr/bin/python3
"""this module prints a sorted list"""


class MyList(list):
    """this class prints a sorted list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
