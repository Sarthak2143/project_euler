# Problem 6: Largest palindrome product

def main():
    res = []
    for i in range(100, 1000):
        for j in range(i+1, 1000):
            string = str(int(i * j))
            if string == string[::-1]:
                res.append(int(string))
    print(res)
    print(max(res))

if __name__ == "__main__":
    main()
