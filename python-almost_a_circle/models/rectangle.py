#!/usr/bin/python3
'''
Write the class Rectangle that
inherits from Base:
'''
from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Width getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Width setter
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''
        height getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        height setter
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''
        x getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        x setter
        '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''
        y getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        y setter
        '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''
        Returns area
        '''
        return self.width * self.height

    def display(self):
        """Returns printed rectangle with '#'
        y is newline, x is space
        """

        if self.__y != 0:
            for newline in range(self.__y):
                print()

        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Returns formatted information display
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates rectangle values
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Returns dict representation
        """

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
