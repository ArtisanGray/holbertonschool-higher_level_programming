#!/usr/bin/python3
"""this module contains a square class with its own data"""


class Square:
    """square class with different methods"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the size of the square and any other data needed

        Args:
            size(int): size of the square
            position(tuple): starting pos of the square
        """
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """returns the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square, checks for errors/bad types

        Args:
            value(int): value to set the size to
        """
        if isinstance(value, int) is not True:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """returns the position of the square"""
        return(self.__position)

    def position(self, value):
        """sets the value of the position of the square

        Args:
            value(tuple): position of the square
        """
        if type(value) != tuple:
            raise TypeError("Position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError(te)
        for pos in value:
            if isinstance(pos, int) is not True:
                raise TypeError(te)
            if pos < 0:
                raise TypeError(te)
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square"""
        if (self.__size) != 0:
            for o in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for p in range(0, self.__position[0]):
                        print("_", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
