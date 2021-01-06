#!/usr/bin/python3
"""this module contains a square class"""


class Square:
    """square class with different methods"""
    def __init__(self, size=0):
        """initializes the size of the square and any other data needed

        Args:
            size(int): size of the square
        """
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
