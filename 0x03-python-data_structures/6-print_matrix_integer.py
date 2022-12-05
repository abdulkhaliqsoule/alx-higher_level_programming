#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints amatrix of integers
    Args:
        matrix: matrix
    Returns:
        None
    """
    for list in matrix:
        for element in list:
            print("{:d}".format(element), end="")
            if element != list[len(list) - 1]:
                print(" ", end="")
        print()
