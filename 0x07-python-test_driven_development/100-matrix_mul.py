#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    r1 = len(m_a)
    if r1 == 0:
        raise ValueError("m_a can't be empty")
    r2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if r2 is None:
            r2 = len(i)
            if r2 == 0:
                raise ValueError("m_a can't be empty")
        if r2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    r3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if r3 is None:
            r3 = len(i)
            if r3 == 0:
                raise ValueError("m_b can't be empty")
        if r3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if r2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(r1):
        r = []
        for j in range(r3):
            n = 0
            for k in range(r2):
                n += m_a[i][k] * m_b[k][j]
            r.append(n)
        matrix.append(r)
    return matrix
