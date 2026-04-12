echo '#!/usr/bin/python3
"""This module defines a class Square with getter and setter."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)' > 4-square.py
