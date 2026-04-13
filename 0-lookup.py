#!/usr/bin/python3
"""
Bu modul obyektlərin atributlarını axtarmaq üçün funksiyanı ehtiva edir.
"""


def lookup(obj):
    """
    Obyektin mövcud atribut və metodlarının siyahısını qaytarır.

    Args:
        obj: Yoxlanılacaq obyekt.

    Returns:
        list: Atributların adlarından ibarət siyahı.
    """
    return dir(obj)
