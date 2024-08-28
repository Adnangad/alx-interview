#!/usr/bin/python3
"""Contains a function"""


def island_perimeter(grid):
    """Returns the perimiter of an island"""
    count = 0
    rows = len(grid)
    for row in range(rows):
        j = len(grid[row])
        for column in range(j):
            if grid[row][column] == 1:
                if row == 0 or grid[row - 1][column] == 0:
                    count += 1
                if row == rows - 1 or grid[row + 1][column] == 0:
                    count += 1
                if column == 0 or grid[row][column - 1] == 0:
                    count += 1
                if column == j - 1 or grid[row][column + 1] == 0:
                    count += 1
    return count
