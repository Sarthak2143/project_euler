# Problem 1: Multiples of 3 and 5

def multiples(num, limit):
    res = []
    for i in range(num, limit):
        if i % num == 0:
            res.append(i)
    return res

def main():
    mul_3 = multiples(3, 1000)
    mul_5 = multiples(5, 1000)
    res = set(mul_3 + mul_5)

    print(f"Sum: {sum(res)}") # => 233168

if __name__ == "__main__":
    main()
