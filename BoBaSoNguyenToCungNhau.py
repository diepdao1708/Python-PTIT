def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def run():
    n = [int(i) for i in input().split()]
    a = []
    for i in range(n[0], n[1] + 1):
        for j in range(i + 1, n[1] + 1):
            if gcd(i, j) == 1:
                a.append((i, j))

    res = []
    for i in a:
        for j in range(i[1] + 1, n[1] + 1):
            if gcd(i[0], j) == 1 and gcd(i[1], j) == 1:
                res.append((i[0], i[1], j))
    for i in res:
        print(f"({i[0]}, {i[1]}, {i[2]})")

run()