#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list
    Args:
        my_list: list
    Returns:
        maximum integer
    """
    max = 0
    for element in my_list:
        if element > max:
            max = element
    return (max)
