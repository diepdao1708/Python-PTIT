
def ok(c):
    if (c >= 'a' and c <= 'z') :
        return False
    return True

def cmp(a, b):
    if a[0] < b[0]:
        if a[1] > b[1]:
            return True
        return True
    return False

def run():
    n = int(input())
    count = {}
    for i in range(n):
        tmp = input().lower()
        x = ""
        for j in range(len(tmp)):
            if ok(tmp[j]):
                if len(x) > 0:
                    if x not in count:
                        count[x] = 1
                    else:
                        count[x] += 1
                x = ""
            else:
                x += tmp[j]
        if len(x) > 0:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1

    count = sorted(count.items(), key = lambda x: (-x[1], x[0]), reverse=True)
    count = reversed(count)
    for i in count:
            print(i[0], i[1])

run()