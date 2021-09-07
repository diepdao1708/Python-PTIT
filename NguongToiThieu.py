def run():
    s = input()
    k = int(input())
    count = {}
    a = []
    i = 0
    while i + 1 < len(s):
        tmp = s[i] + s[i + 1]
        if tmp not in count:
            count[tmp] = 1
            a.append(tmp)
        else:
            count[tmp] += 1
        i += 2
    a.sort()
    ok = False
    for i in a:
        if count[i] >= k:
            ok = True
            print(i, count[i])
    if ok == False:
        print("NOT FOUND")

run()