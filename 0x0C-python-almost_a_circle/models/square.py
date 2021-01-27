#!/usr/bin/python3
"""Square Class module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes square instance with super call"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str magic function"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """returns the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates instance attributes"""

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "size":
                        self.width = kwargs["size"]
                        self.height = kwargs["size"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """exports instance atts to a dictionary"""

        dic = {}

        dic["id"] = self.id
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
