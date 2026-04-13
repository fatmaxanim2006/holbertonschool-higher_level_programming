#!/usr/bin/python3
"""
Bu modul düzbucaqlını təyin edən Rectangle class-ından ibarətdir.
"""


class Rectangle:
    """Düzbucaqlını təmsil edən class."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır.
        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width üçün getter metodu."""
        return self.__width

    @width.setter
    def width(self, value):
        """width üçün setter metodu."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height üçün getter metodu."""
        return self.__height

    @height.setter
    def height(self, value):
        """height üçün setter metodu."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
