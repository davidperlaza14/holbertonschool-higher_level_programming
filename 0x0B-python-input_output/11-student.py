#!/usr/bin/python3
"""Class 'Student'"""


class Student:

    """Constructor method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""

        dictionary = {}

        if attrs is None:
            return self.__dict__

        for key_inside, value_inside in self.__dict__.items():
            if key_inside in attrs:
                dictionary[key_inside] = value_inside
        return dictionary

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        for key_inside, value_inside in json.items():
            setattr(self, key_inside, value_inside)
