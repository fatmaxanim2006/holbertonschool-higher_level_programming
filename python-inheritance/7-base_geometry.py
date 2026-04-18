#!/usr/bin/python3
"""
BaseGeometry modulunu ehtiva edir.
"""


class BaseGeometry:
    """BaseGeometry sinfi."""

    def area(self):
        """area() metodunu elan edir (hələ tətbiq olunmayıb)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyərin tam ədəd və > 0 olmasını yoxlayır.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
