#!/usr/bin/python3
class Square():
    '''creates a class that is a square'''
    def __init__(self, size=0):
        '''initializes the data used for the square'''
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
