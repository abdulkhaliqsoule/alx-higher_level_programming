#!/usr/bin/python3
"""
file: 10-square.py
Class:
-> Rectangle(BaseGeometry)
-> Square(Rectangle)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size):
        """ Constructor method """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area """
        return super().area()
