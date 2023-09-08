#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Type and Value Validation"""
        if not isinstance(self, int):
            raise TypeError("width muist be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    height.setter
    def height(self, value):
        if not isinstance(self, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("Height must be > 0")
        self.__height
