#!/usr/bin/python3
"""
This module defines a Square class with getter, setter, and area calculation.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
