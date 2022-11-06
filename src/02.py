# Problem 2: Even Fibonacci Numbers

def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def main():
    col_of_fibs = [] 
    
    for i in range(1, 40):
        if fib(i) < 4000000 and fib(i) % 2 == 0:
            col_of_fibs.append(fib(i))
        if fib(i) > 4000000:
            break

    print(sum(set(col_of_fibs))) # => 4613732 

if __name__ == "__main__":
    main()
