def run():
    s = input()
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
    for i in a:
        print(i, count[i])

run()