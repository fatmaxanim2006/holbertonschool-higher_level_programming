#!/usr/bin/python3
"""BaseGeometry sinfi üçün modul"""


class BaseGeometry:
    """Həndəsə əməliyyatları üçün baza sinfi"""

    def area(self):
        """Hələ tətbiq olunmayıbsa Exception qaytarır"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və 0-dan böyük olmasını yoxlayır"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
