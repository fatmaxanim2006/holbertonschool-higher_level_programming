#!/usr/bin/python3
"""
SimpleCustomDict klassı - lüğət elementlərinə atribut kimi müraciət üçün
"""


class SimpleCustomDict(dict):
    """
    Standart dict-i genişləndirir və atribut üslublu müraciəti təmin edir
    """

    def __getattr__(self, key):
        """Atribut kimi müraciət edildikdə (obj.key)"""
        try:
            return self[key]
        except KeyError:
            raise AttributeError("No such attribute: {}".format(key))

    def __setattr__(self, key, value):
        """Atribut təyin edildikdə (obj.key = value)"""
        self[key] = value
