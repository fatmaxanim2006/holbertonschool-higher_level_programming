#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """A class MyInt that inverts == and != operators"""

    def __eq__(self, other):
        """Inverts == into !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts != into =="""
        return super().__eq__(other)
