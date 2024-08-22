#!/usr/bin/python3
"""Contains a function"""


def makeChange(coins, total):
    """Solves make change problem"""
    if total <= 0:
        return 0
    coins.sort(reversed=True)
    i = len(coins) - 1
    count = 0
    result = total
    while i > 0:
        result = result - coins[i]
        count += 1
        if result < coins[i]:
            i = i - 1
    if result == 0:
        return count
    else:
        return - 1
