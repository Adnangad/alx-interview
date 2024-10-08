#!/usr/bin/python3
"""
This module contains the function that creates a pascal triangle from an array.
"""


def pascal_triangle(n):
    """
    Args: n
    n the number of arrays.
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
