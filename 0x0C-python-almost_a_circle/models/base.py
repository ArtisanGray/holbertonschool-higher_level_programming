#!/usr/bin/python3
"""Documentation for class module"""
import json
import os


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance variables"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON rep of an object to a file"""

        if list_objs is None or len(list_objs) == 0:
            o_list = []
        else:
            o_list = []
            for item in list_objs:
                o_list.append(item.to_dictionary())
        rep = Base.to_json_string(o_list)

        with open("{}.json".format(cls.__name__), mode="w")\
                as o_file:
            o_file.write(rep)

    @staticmethod
    def from_json_string(json_string):
        """returns json string"""

        if json_string is None or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with new attributes"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            tmp = cls(7, 7)
        if cls == Square:
            tmp = cls(2)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """return list from file"""

        filename = "{}.json".format(cls.__name__)

        if os.path.isfile(filename):
            il = []
            with open(filename) as o_file:
                insta_o = cls.from_json_string(o_file.read())
                for dic in insta_o:
                    il.append(cls.create(**dic))
            return il
        return []
