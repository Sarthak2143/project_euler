# Problem 3: Largest Prime Factor

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

def main():
    print(max(send_factors(600851475143))) # => 6857

if __name__ == "__main__":
    main()
