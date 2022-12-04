#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace elemnt of a list at a specific position
    Args:
        my_list: list
        idx: index
        element: element to replace at index
    Returns:
        modified list
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
