#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for a in matrix:
        if type(a) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(a)
        elif size != len(a):
            raise TypeError("Each row of the matrix must have the same size")
        for i in a:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in a] for a in matrix]
