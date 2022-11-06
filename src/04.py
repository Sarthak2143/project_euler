# Problem 4: Sum square difference

def sum_of_squares(n):
    result = (n*(n+1)*(2*n + 1)) / 6
    return result

def square_of_sum(n):
    sum = (n * (n+1)) / 2
    sqr = sum ** 2
    return sqr

def main():
    sum_of_sqr = sum_of_squares(100)
    sqr_of_sum = square_of_sum(100)
    print(int(sqr_of_sum - sum_of_sqr))

if __name__ == "__main__":
    main()
