#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints amatrix of integers
    Args:
        matrix: matrix
    Returns:
        None
    """
    for list in matrix:
        for int in list:
            print("{:d}".format(int), end=" ")
        print()
