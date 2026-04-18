#!/usr/bin/python3
"""
SimpleCustomDict modulu - atribut üslublu müraciət üçün
"""


class SimpleCustomDict(dict):
    """
    Standart lüğəti genişləndirir ki, obyekt.açar kimi istifadə olunsun
    """

    def __getattr__(self, key):
        """Atribut kimi çağırılanda lüğətdən açarı qaytarır"""
        try:
            return self[key]
        except KeyError:
            # Atribut tapılmayanda standart AttributeError qaytarılmalıdır
            raise AttributeError("No such attribute: {}".format(key))

    def __setattr__(self, key, value):
        """Atribut təyin ediləndə onu lüğətə açar kimi əlavə edir"""
        self[key] = value
