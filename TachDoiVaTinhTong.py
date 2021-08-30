n = input()
k = len(n)
# print(int(5/2))
while k > 1:
    tmp = int(k/2)
    x = ""
    y = ""
    for i in range(0, tmp):
        x += n[i]
    for i in range(tmp, k):
        y += n[i]
    n = str(int(x) + int(y))
    k = len(n)
    print(n)
