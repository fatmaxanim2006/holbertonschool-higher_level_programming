#!/usr/bin/python3
"""Module for MyInt"""

class MyInt(int):
    """Inverted int"""
    def __eq__(self, other):
        """== becomes !="""
        return super().__ne__(other)
    def __ne__(self, other):
        """!= becomes =="""
        return super().__eq__(other)
