#!/usr/bin/python3
def no_c(my_string):
    """ Remove all characters c and C from string
    Args:
        my_string: string
    Returns:
        new string
    """
    new_string = ""
    for letter in my_string:
        if letter not in "cC":
            new_string += letter
    return (new_string)
