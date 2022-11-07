# Problem 5: Smallest Multiple

def get_gcd(a, b):
    GCDs = []
    smaller = min(a, b)
    if a == b: return a
    if b % a == 0 or a % b == 0: return min(a, b)
    for i in range(2, smaller):
        if a % i == 0 and b % i == 0:
            GCDs.append(i)
    if len(GCDs) == 0: return 1
    return max(GCDs)

def get_lcm(a, b):
    return int(a * b / get_gcd(a, b))

def gcd(array):
    num1 = array[0]
    num2 = array[1]
    gcd_0 = get_gcd(num1, num2)
    for i in range(2, len(array)):
        gcd_0 = get_gcd(gcd_0, array[i])
    return gcd_0

def lcm(array):
    lcm_0 = get_lcm(array[0], array[1])
    for i in range(2, len(array)):
        lcm_0 = get_lcm(lcm_0, array[i])
    return lcm_0

def main():
    data = []
    for i in range(1, 21):
        data.append(i)
    print(data)
    print(lcm(data))

if __name__ == "__main__":
    main()
