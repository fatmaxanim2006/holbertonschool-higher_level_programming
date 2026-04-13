#!/usr/bin/python3
"""Module for add_attribute"""

def add_attribute(obj, name, value):
    """Adds attribute if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
