def run():
    n = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    count = {}
    maxx = -1
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        maxx = max(maxx, count[i])
    res = -1
    vt = -1
    for i in range(0, len(a)):
        if count[a[i]] > res and count[a[i]] < maxx:
            res = count[a[i]]
            vt = a[i]
    if vt == -1:
        print("NONE")
        return
    print(vt)
    


run()