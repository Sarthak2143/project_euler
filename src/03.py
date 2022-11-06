# Largest Prime Factor

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def isPrime(n):
    if n == 1 or n == 2: return True
    c = int(math.sqrt(n))
    for i in range(2, c+1):
        if n % i == 0:
            return False
    return True

def send_factors(n):
    res = []
    while n != 1 :
        for i in range(2, n):
            if n % i == 0:
                res.append(i)
                n = n / i
            if n == 1:
                break
    return list(set(res))

print(max(send_factors(600851475143))) # => 6857
