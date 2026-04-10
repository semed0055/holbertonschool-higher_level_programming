#!/usr/bin/python3
"""
Module defining the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
