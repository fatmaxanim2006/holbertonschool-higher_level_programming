#!/usr/bin/python3
"""Modul BaseGeometry sinfini təyin edir."""


class BaseGeometry:
    """Həndəsi fiqurlar üçün sinif."""

    def area(self):
        """Sahəni hesablayır. Hələ tətbiq edilməyib."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyəri tam ədəd olaraq doğrulayır.

        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.
        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0 və ya daha azdırsa.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
