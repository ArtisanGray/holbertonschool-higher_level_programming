#!/usr/bin/python3
"""this module contains a rectangle class"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize class attributes

        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    def __str__(self):
        """prints the rectangle"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """returns a representation of the current instance"""
        return "Rectangle({},{})".format(self.__width, self.__height)

    def __del__(self):
        """runs when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """returns the total area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return(2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangle objects

        Args:
            rect_1(Rectangle): rectangle 1
            rect_2(Rectangle): rectangle 2
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return(rect_1)
        return(rect_1 if rect_1.area() > rect_2.area() else rect_2)
