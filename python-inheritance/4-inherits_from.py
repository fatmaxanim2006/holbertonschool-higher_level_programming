#!/usr/bin/python3
"""Module for inherits_from"""

def inherits_from(obj, a_class):
    """Checks inheritance only"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
