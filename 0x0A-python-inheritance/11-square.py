#!/usr/bin/python3
"""
file: 11-square.py
Class:
-> Rectangle(BaseGeometry)
-> Square(Rectangle)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle """

    def __init__(self, size):
        """ Constructor method """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ print(self) method """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
