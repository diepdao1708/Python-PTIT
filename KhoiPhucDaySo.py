def run():
    n = int(input())
    ls = []
    Sum = 0
    for i in range(n):
        a = [int(i) for i in input().split()]
        k = 0
        for j in range(n):
            k += a[j]
        ls.append(k)
        Sum += k
    Sum = int(Sum / ((n - 1) * 2))
    res = ""
    for i in range(n):
        res += str(int ((ls[i] - Sum) / (n - 2))) + " "
    print(res)
run()