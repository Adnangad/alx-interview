#!/usr/bin/python3
"""Contains a function"""


def makeChange(coins, total):
    """Solves make change problem"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    result = total
    for coin in coins:
        while result >= coin:
            result -= coin
            count += 1
    if result == 0:
        return count
    else:
        return - 1
