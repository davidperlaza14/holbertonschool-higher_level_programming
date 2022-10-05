#!/usr/bin/python3
"""
Define a private instance attibute size
size must be an int and greater than zero
"""

class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return size * size