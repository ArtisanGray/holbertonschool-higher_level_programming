#!/usr/bin/python3
"""this module contains a rectangle class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initialize class attributes

        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getter for the rectangle's height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter for the rectangle's height

        Args:
            value(int): integer value for the height of rect
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """getter for the rectangle's width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value(int): an integer used for the width of rect
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
