import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True    

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    isPrime = []
    for i in a:
        if snt(i):
            isPrime.append(i)
    isPrime.sort()
    vt = 0
    for i in range(0, n):
        if  snt(a[i]):
            print(isPrime[vt], end=" ")
            vt += 1
        else:
            print(a[i], end=" ")


run()