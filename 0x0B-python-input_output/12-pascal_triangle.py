#!/usr/bin/python3
"""Defining pascal_triangle funtion"""


def generate_pascal_triangle(rows):
    """Generates Pascal's triangle as a list of lists"""
    if rows <= 0:
        return []

    triangle = [[1]]

    for x in range(rows - 1):
        new_row = [1]
        for col in range(len(triangle[-1]) - 1):
            new_row.append(triangle[-1][col] + triangle[-1][col + 1])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
