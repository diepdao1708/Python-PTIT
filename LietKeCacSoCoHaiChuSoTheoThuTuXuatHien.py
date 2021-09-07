def run():
    s = input()
    count = []
    i = 0
    while i + 1 < len(s):
        tmp = s[i] + s[i + 1]
        if tmp not in count:
            count.append(tmp)
        i += 2
    for i in count:
        print(i, end=" ")

run()