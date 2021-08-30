def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    a = sorted(a)
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if gcd(int(a[i]), int(a[j])) == 1:
                print(a[i], a[j])

run()
