#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class that inherited from a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
