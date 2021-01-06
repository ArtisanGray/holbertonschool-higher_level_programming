#!/usr/bin/python3
"""placeholder module doc thing, no idea what goes here
"""


class Square:
    """square class with different methods
    """
    def __init__(self, size=0):
        """initializes the size of the square and any other data needed

        Args:
            size(int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """returns the current size of the square
        """
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

    def area(self):
        """returns the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints the square
        """
        if (self.__size) != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
