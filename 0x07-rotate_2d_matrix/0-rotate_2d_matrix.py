#!/usr/bin/python3
"""Module contains a function"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix 90 degrees"""
    for row in range(len(matrix)):
        for column in range(row + 1, len(matrix)):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    for row in matrix:
        row.reverse()
