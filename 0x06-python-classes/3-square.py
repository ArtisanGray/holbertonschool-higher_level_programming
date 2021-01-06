#!/usr/bin/python3
class Square():
    '''square class, complete with initialized data'''
    def __init__(self, size=0):
        '''initializes the data used in the class'''
        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''returns the total area of the square'''
        return (self.__size ** 2)
