#!/usr/bin/python3
"""Module of Square"""


class Square:
    """ An class called Square """
    def __init__(self, size=0):
        """
        Initialize the data
        And validates if the number is an int
        and > 0
        Size: The size of the square
        """
        self.__size = size


    # Property
    @property
    def size(self):
        """ Gets the value """
        return self.__size

    # Setter modifies
    @size.setter
    def size(self, value):
        """ Validates if the number is valid """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
