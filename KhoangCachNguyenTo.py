import math

prime = {}

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def pre():
    count = 0
    for i in range(2, 10000):
        if isPrime(i):
            prime[count] = i
            count += 1

def main():
    pre()
    n = [int(i) for i in input().split()]
    res = ""
    res += str(n[1]) + " "
    tmp = prime[0] + int(n[1]) 
    for i in range(0, int(n[0])):
        res += str(tmp) + " "
        tmp += prime[i + 1]
    print(res)

main()