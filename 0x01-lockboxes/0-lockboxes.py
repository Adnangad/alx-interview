#!/usr/bin/python3
"""
This module contains a python function.
"""


def canUnlockAll(boxes):
    """
    Args:
    boxes: the nested list.
    """
    if boxes == null:
        return False
    ls = []
    len_of_boxes = len(boxes)
    for i in range(1, len_of_boxes):
        ls.append(i)
    count = -1
    set_ls = set()
    for i in boxes:
        set_ls.update(i)
    for x in ls:
        if x not in set_ls:
            return False
    for i in boxes:
        count = count + 1
        for j in i:
            if j == count and (sum(row.count(j) for row in boxes) <= 1):
                return False
    return True
