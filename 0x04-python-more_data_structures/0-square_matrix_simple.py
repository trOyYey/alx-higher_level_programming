#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda sqmat: list(map(lambda q: q**2, sqmat)), matrix))
