#!/usr/bin/python3

from re import I


class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id == int
    
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

