#!/usr/bin/python3
"""Contains a module"""


def sieve_of(n):
    """Helper function to return a list of primes up to n."""
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def count_primes_up_to(n, sieve):
    """Helper function"""
    return sum(sieve[:n+1])


def isWinner(x, nums):
    """Determine who wins the most rounds of the Prime Game."""
    if not nums or x <= 0:
        return None
    max_num = max(nums)
    sieve = sieve_of(max_num)
    m = 0
    b = 0
    for n in nums:
        prime_count = count_primes_up_to(n, sieve)
        if prime_count % 2 == 1:
            m += 1
        else:
            b += 1
    if m > b:
        return "Maria"
    elif b > m:
        return "Ben"
    else:
        return None
