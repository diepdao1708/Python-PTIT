import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def main():
    n = [int(i) for i in input().split()]
    for i in range(0, int(n[0])):
        a = [int(i) for i in input().split()]
        res = ""
        for j in range(len(a)):
            if isPrime(int(a[j])):
                res += "1 "
            else:
                res += "0 "
        print(res)

main()