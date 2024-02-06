#!/usr/bin/python3
"""Module contains class Student"""


class Student:
    """Initializes class Student

    Attributes:
        first_name (str): first name
        last_name (Str): last name
        age (int): age
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates an object

        Args:
            first_name (str): first name
            last_name (Str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
