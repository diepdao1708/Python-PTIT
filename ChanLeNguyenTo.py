import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    for i in range(0, len(n)):
        if i % 2 == 1 and int(n[i]) % 2 == 0:
            return False
        if i % 2 == 0 and int(n[i]) % 2 == 1:
            return False
    return True

def run():
    n = input()
    Sum = 0
    for i in n:
        Sum += int(i)
    if check(n) and snt(Sum):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()