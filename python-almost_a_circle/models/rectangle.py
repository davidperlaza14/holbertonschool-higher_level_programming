#!/usr/bin/python3
from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            pass
        @width.setter
        def width(self, value):
            pass

        @property
        def height(self):
            pass
        @height.setter
        def height(self, value):
            pass

        @property
        def x(self):
            pass
        @x.setter
        def x(self, value):
            pass

        @property
        def y(self):
            pass
        @y.setter
        def y(self, value):
            pass
