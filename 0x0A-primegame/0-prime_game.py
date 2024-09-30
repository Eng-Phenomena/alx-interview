#!/usr/bin/python3
"""Task solution
"""


def isWinner(x, nums):
    """	prime number game to identify who is the winner
    """
    if x < 1 or not nums:
        return None
    maria, ben = 0, 0

    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben += primes_count % 2 == 0
        maria += primes_count % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
