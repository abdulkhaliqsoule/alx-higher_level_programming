#!/usr/bin/python3
"""
file: 2-is_same_class.py
Class:
-> is_same_class
"""


def is_same_class(obj, a_class):
    """ Compare is obj is exactly an instance of a_class """
    return type(obj) == a_class
