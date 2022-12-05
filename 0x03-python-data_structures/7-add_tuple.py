#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples
    Args:
        tuple_a: first tuple
        tuple_b: second tuple
    Returns:
        Tuple containg the sum of the two integers
    """
    if len(tuple_a) >= 2:
        x1 = tuple_a[0]
        y1 = tuple_a[1]
    if len(tuple_b) >= 2:
        x2 = tuple_b[0]
        y2 = tuple_b[1]
    if len(tuple_a) == 1:
        y1 = 0
        x1 = tuple_a[0]
    if len(tuple_b) == 1:
        y2 = 0
        x2 = tuple_b[0]
    if len(tuple_a) == 0:
        x1 = 0
        y1 = 0
    if len(tuple_b) == 0:
        x2 = 0
        y2 = 0
    x = x1 + x2
    y = y1 + y2
    new_tuple = (x, y)
    return (new_tuple)
