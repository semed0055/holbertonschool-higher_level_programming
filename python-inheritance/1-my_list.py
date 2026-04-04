#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It provides an additional method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList inherits from list and adds a method for sorted printing.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        All elements in the list are assumed to be of type int.
        """
        print(sorted(self))
