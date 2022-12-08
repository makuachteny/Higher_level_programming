#!/usr/bin/python3
""" A script that contains the class BaseGeometry and subclass Rectangle"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
         """validates that value is an integer greater than 0"""
         if type(value) is not int:
             raise TypeError("{:s} must be an integer".format(name))
         if value <= 0:
             raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class named BaseGeometry
     Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width, height):
        """initializes an instance"""
         self.integer_validator("width", width)
         self.integer_validator("height", height)
         self.__width = width
         self.__height = height

    def area(self):
        """returns area of instance"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
