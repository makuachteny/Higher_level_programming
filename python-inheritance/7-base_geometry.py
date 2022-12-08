#!/usr/bin/python3
"""A module that creates a class named BaseGeometry"""


class BaseGeometry:
    """ BaseGeometry class
    Attributes
    attr1(area):raises an exception
    """
    def area(self):
        """raise an exception error message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
