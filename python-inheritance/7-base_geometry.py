#!/usr/bin/python3
"""
Bu modul BaseGeometry sinfini ehtiva edir.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza sinfi."""

    def area(self):
        """Hələ tətbiq olunmamış sahə funksiyası."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyərin tam ədəd və 0-dan böyük olub-olmadığını yoxlayır.

        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.
        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value <= 0 olarsa.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
