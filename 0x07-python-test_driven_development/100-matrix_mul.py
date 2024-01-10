#!/usr/bin/python3
"""
    matrix_mul mod
    using mod doctest
    for cases
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrixes.
    Arguments:
        m_a: matrix A.
        m_b: matrix B
    Returns:
        matrix: results of m_a * m_b
    Raises:
        TypeError: m_a or m_b not lists.
        TypeError: m_a or m_b not lists of lists.
        ValueError: m_a or m_b are empty.
        TypeError: m_a or m_b not only numbers.
        TypeError: m_a or m_b are not rectangular.
        ValueError: m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance (row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num in row:
            if type(num) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if type(row) != list:
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num in row:
            if type(num) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            z = 0
            for k in range(len(m_b)):
                z += m_a[x][k] * m_b[k][y]
            result[x].append(z)

    return result


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/100-matrix_mul.txt")
