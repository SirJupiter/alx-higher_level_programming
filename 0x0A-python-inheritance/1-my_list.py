#!/usr/bin/python3
"""Module contains MyList class"""


class MyList(list):
    """A simple implementation of a list with added functionality.
    """

    def print_sorted(self):
        """Prints the elements in ascending order."""
        print(sorted(self))
