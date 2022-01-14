import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def countNumberIsPrime(n):
    count = 0
    for i in n:
        if isPrime(int(i)):
            count += 1
    return count
        
def solve(n):
    if isPrime(len(n)) and countNumberIsPrime(n) > len(n) - countNumberIsPrime(n):
        print("YES")
    else: print("NO")

t = int(input())
while t > 0:
    t -= 1
    n = input()
    solve(n)