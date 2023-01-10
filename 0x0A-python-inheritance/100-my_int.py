#!/usr/bin/python3
"""
file: 100-my_int.py
Class:
-> MyInt
"""


class MyInt(int):
    """ __eq__ and __ne__ inverted """

    def __eq__(self, other):
        """ Inverted to not equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverted to equal """
        return super().__eq__(other)
