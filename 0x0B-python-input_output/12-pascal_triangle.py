#!/usr/bin/python3
"""Defining pascal_triangle funtion"""


def pascal_triangle(n):
    """Generates Pascal's triangle as a list of lists"""
    if n <= 0:
        return []

    triangle = [[1]]

    for x in range(n - 1):
        new_row = [1]
        for col in range(len(triangle[-1]) - 1):
            new_row.append(triangle[-1][col] + triangle[-1][col + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
