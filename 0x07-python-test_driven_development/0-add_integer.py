#!/usr/bin/python3
"""
This is a module that contains a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers/ floats or an integer and a float
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the input
    Raises:
        TypeError: If a or b are not integers and/or float numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
