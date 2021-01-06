#!/usr/bin/python3
"""this module contains square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """initializes the size of the square and any other data needed


        Args:
            size(int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """returns the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square, checks for errors/bad type


        Args:
            value(int): value to resize square with
        """
        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)
