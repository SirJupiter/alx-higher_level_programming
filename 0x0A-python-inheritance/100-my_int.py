#!/usr/bin/python3
"""Module contains class 'MyInt' which inherits from 'int'"""


class MyInt(int):
    """Rebel class MyInt; '==' and '!=' are to be inverted"""

    def __init__(self, num):
        """Instantiates an object of this class

        Args:
            num (int): integer
        """

        self.num = num

    def __eq__(self, other):
        """Override the equality operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator"""
        return super().__eq__(other)

    def __str__(self):
        """Prints something when print() is called"""
        return f"{self.num}"
