#!/usr/bin/python3
"""
Bu modul BaseGeometry klassını təyin edir.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün əsas klass."""

    def area(self):
        """Sahəni hesablamaq üçün metod (hələ tətbiq edilməyib)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dəyərin tam ədəd olub-olmadığını yoxlayır.

        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.
        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value <= 0-dırsa.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
