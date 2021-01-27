#!/usr/bin/python3
"""Rectangle Class module doc"""
from models.base import Base


class Rectangle(Base):
    """Class for rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of instance variables"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width to value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """returns Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x to value"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y to value"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """Prints rectangle"""

        for s in range(self.__y):
            print()
        for i in range(self.__height):
            for j1 in range(self.__x):
                print(" ", end='')
            for j2 in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str magic function"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update attributes"""

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "width":
                        self.width = kwargs["width"]
                    if key == "height":
                        self.height = kwargs["height"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """exports attributes to a newly created dictionary"""

        dic = {}

        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
