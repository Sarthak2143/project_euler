# Problem 7: 10001st prime

import math

def isPrime(n):
    if n == 2: return True
    c = int(math.sqrt(n))
    for i in range(2, c+1):
        if n % i == 0:
            return False
    return True

def find_prime():
    num, count = 2, 0
    while True:
        if isPrime(num):
            count += 1
            if count == 10001:
                return num
        num += 1

def main():
    print(find_prime())

if __name__ == "__main__":
    main()
