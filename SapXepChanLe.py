n = int(input())
dem = 0
chan = []
le = []
a = []
while 1:
    s = [int(k) for k in input().split()]
    dem += len(s)
    for k in range(len(s)):
        a.append(s[k])
        if s[k] % 2 == 0:
            chan.append(s[k])
        else:
            le.append(s[k])
    if dem == n:
        break
le.sort(reverse=True)
chan.sort()
res = ""
i = 0
j = 0
for k in range(n):
    if a[k] % 2 == 0:
        res += str(chan[i]) + " "
        i += 1
    else:
        res += str(le[j]) + " "
        j += 1
print(res)