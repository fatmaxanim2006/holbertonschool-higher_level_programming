#!/usr/bin/python3
"""Rectangle sinfi üçün modul"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry-dən miras alan Rectangle sinfi"""

    def __init__(self, width, height):
        """En və hündürlüyü təyin edir və doğrulayır"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
