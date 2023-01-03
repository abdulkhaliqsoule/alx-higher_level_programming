#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix: a list of lists of integers or floats
        div: a number that divides each element in the matrix
    Returns:
        a matrix of the divided by div
    Raises:
        TypeError: If matrix is not a list of integers/floats,
                    or if each row of the matrix do not
                    have the same size or div is not a number
        ZeroDivisionError: If div is 0
    """
    sizes = []
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix(list of lists)
                                of integers/floats")
        size = len(row)
        sizes.append(size)
    for length in sizes:
        if len(matrix[0]) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            element = round((element/div), 2)
            new_row.append(element)
        new_matrix.append(new_row)
    return (new_matrix)
