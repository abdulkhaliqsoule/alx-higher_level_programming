#!/usr/bin/python3
"""
file: 9-rectangle.py
Class:
-> BaseGeometry
-> Rectangle(BaseGeometry)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits from BaseGeomtry """

    def __init__(self, width, height):
        """ Constructor method """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def __str__(self):
        """ print(self) method """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
