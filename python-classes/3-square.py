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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
