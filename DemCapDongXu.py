a = []
n = int(input())
res = 0
for i in range(n):
    s = input()
    k = s.count("C", 0, len(s))
    res += int(k * (k - 1) / 2)
    a.append(s)
for i in range(n):
    tmp = ""
    for j in range(n):
        tmp += a[j][i]
    k = tmp.count("C", 0, len(tmp))
    res += int(k * (k - 1) / 2)
print(res)