#!/usr/bin/python3
"""
    multiply 2 matrixies using NumPy module
    doctest to check cases
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrixes
    Arguments:
        m_a: matrix A
        m_b: matrix B
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
