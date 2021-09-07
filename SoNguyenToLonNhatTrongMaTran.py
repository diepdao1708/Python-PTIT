import math

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def run():
    n = [int(i) for i in input().split()]
    a = []
    maxx = -1
    for i in range(int(n[0])):
        x = [int(i) for i in input().split()]
        a.append(x)
        for j in x:
            if isPrime(j) == True:
                maxx = max(j, maxx)
    if maxx == -1:
        print("NOT FOUND")
        return
    print(maxx)
    for i in range(int(n[0])):
        for j in range(int(n[1])):
            if a[i][j] == maxx:
                print(f"Vi tri [{i}][{j}]")
    # print(maxx)

run()