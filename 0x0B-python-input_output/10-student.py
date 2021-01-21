#!/usr/bin/python3
"""this module creates a student"""


class Student:
    """ Class for student"""
    def __init__(self, first_name, last_name, age):
        """initializes public/private instance data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary desc of class"""
        if attrs is not None and isinstance(attrs, list):
            new_d = {}
            for strs in attrs:
                if isinstance(strs, str) is not True:
                    return self.__dict__
                if strs in self.__dict__.keys():
                    new_d[strs] = self.__dict__[strs]
            return new_d
        else:
            return self.__dict__
