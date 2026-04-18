#!/usr/bin/python3
"""BaseGeometry modulu üçün sənədləşmə."""


class BaseGeometry:
    """BaseGeometry sinfi."""

    def area(self):
        """Sahəni hesablayan metod (hələ icra olunmayıb)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd və 0-dan böyük olmasını yoxlayır.

        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: Əgər value int deyilsə.
            ValueError: Əgər value <= 0 olarsa.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
