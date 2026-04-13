#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """MyInt class that inherits from int"""

    def __eq__(self, value):
        """Inverts the == operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts the != operator"""
        return super().__eq__(value)
