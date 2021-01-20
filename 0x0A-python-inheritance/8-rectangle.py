#!/usr/bin/python3
"""this module does nothing"""


class BaseGeometry:
    """this class throws an error"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this checks and validates an integer

        Args:
            name(str): name of the integer
            value(int): value of the integer
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
