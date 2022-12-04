#!/usr/bin/bash
def element_at(my_list, idx):
    """Retrieve an element from a list like in C
    Args:
        my_list: list
        idx: index
    Returns:
        element at idx
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return (my_list[idx])
