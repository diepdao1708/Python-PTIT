def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    vt = a[0]
    minn = 1000000
    
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += abs(a[j] - a[i])
        # print(tmp)
        if tmp < minn:
            minn = tmp
            vt = a[i]

    print(minn, vt)

run()