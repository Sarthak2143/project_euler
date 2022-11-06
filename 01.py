# Problem I: Multiples of 3 and 5

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples(num, limit):
    res = []
    for i in range(num, limit):
        if i % num == 0:
            res.append(i)
    return res

mul_3 = multiples(3, 1000)
mul_5 = multiples(5, 1000)
res = set(mul_3 + mul_5)

print(f"Sum: {sum(res)}") # => 233168
