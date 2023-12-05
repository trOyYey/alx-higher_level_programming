#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for z in matrix:
        for y in z:
            if (y == z[-1]):
                print("{:d}".format(y), end='')
            else:
                print("{:d}".format(y), end=' ')
        print()
