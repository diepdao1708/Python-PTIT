def run():
    n = [int(i) for i in input().split()]
    a = []
    maxx = -1
    minn = 10001
    for i in range(int(n[0])):
        x = [int(i) for i in input().split()]
        a.append(x)
        for j in x:
            maxx = max(maxx, j)
            minn = min(minn, j)

    res = []
    for i in range(int(n[0])):
        for j in range(int(n[1])):
            if a[i][j] == maxx - minn:
                res.append((i, j))
    if len(res) == 0:
        print("NOT FOUND")
        return
    print(maxx - minn)
    for i in res:
        print(f"Vi tri [{i[0]}][{i[1]}]")

run()