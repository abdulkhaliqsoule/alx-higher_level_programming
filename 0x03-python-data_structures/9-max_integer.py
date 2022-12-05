#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list
    Args:
        my_list: list
    Returns:
        maximum integer
    """
    if(len(my_list) == 0):
        return(None)
    return(sorted(my_list)[-1])
