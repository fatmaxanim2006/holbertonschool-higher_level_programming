#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class with area and str representation"""

    def __init__(self, size):
        """Initializes size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
