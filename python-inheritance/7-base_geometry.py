#!/usr/bin/python3
"""BaseGeometry modulu."""


class BaseGeometry:
    """BaseGeometry sinfi."""

    def area(self):
        """Area metodu."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator metodu."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
