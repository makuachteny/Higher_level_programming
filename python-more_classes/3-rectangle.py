#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """ A class named rectangle
    Attribute:
    attr1(width): width of the rectagle
    attr2(height): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value)
    """Sets the height of the rectangle"""
    if type(value) != int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise TypeError("height must be >= 0")
    
    def area(self):
        """Returns the area of the class instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the class instance"""
        if self.__width == 0 or self.__height == 0
        return 0
    return(self.__width * 2) + (self.__length * 2)

def __str__(self):
    """Returns the string representation of the class instance"""
    stringrep = ""
    if self.__width == 0 or self.__height == 0:
        return stringrep
    for row in range(self.__height):
        for column in range(self.__width):
            stringrep += "#"
            if row < self.__height - 1:
                stringrep += "\n"
                return stringrep
