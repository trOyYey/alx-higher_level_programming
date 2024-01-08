#!/usr/bin/python3
"""
    matrix_divided mod
    using doctest
    to test how it works
"""


def matrix_divided(matrix, div):
    """Divides matrix by div.
    Args:
        matrix: List of list of numbers
        div: number to fiv with
    Returns:
        list: list of products
    Raises:
        TypeError: matrix is not list of lists of numbers.
        TypeError: If sublists are not all in the same size.
        TypeError: If division is not a number.
        ZeroDivisionError: If division is zero.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for i in matrix:
        if type(i) != list or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    result = []
    for j in matrix:
        s = []
        for x in j:
            s.append(round(x / div, 2))
        result.append(s)
    return result


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/2-matrix_divided.txt")
