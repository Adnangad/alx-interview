#!/usr/bin/python3
"""
This module contains functions that calculate min operations it takes/
to display a certain number of characters.
"""


def copy(current_value):
    """
    Returns the length of the current string.
    """
    copy_value = len(current_value)
    return copy_value


def paste(copy_value, current_value):
    """
    Adds the number of characters to a string depending on the copy_value
    """
    return current_value + 'H' * copy_value


def minOperations(n):
    """
    Returns the min amnt of operations required to result
    the string with the same length as n.
    """
    if n <= 1:
        return 0
    count = 0
    current_value = 'H'
    while len(current_value) < n:
        if n % len(current_value) == 0:
            copy_value = copy(current_value)
            count = count + 1
        current_value = paste(copy_value, current_value)
        count = count + 1
    return count
