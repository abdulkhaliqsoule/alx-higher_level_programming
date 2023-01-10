#!/usr/bin/python3
"""
file: 4-inherits_from.py
Class:
-> inherits_from
"""


def inherits_from(obj, a_class):
    """ Check for directly or indirectly inheritance """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
