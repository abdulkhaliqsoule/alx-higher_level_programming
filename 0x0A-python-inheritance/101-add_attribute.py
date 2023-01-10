#!/usr/bin/python3
"""
file: 101-add_attribute.py
Functions:
-> add_attribute
"""


def add_attribute(obj, name, value):
    """ Add attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
