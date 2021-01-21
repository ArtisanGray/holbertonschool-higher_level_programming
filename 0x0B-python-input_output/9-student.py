#!/usr/bin/python3
"""this module creates a student"""


class Student:
    """ Class for student"""
    def __init__(self, first_name, last_name, age):
        """initializes public/private instance data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary desc of class"""
        return self.__dict__
