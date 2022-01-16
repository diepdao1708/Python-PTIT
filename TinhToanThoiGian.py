def time(y, x):
    return x[0] * 60 + x[1] - y[0] * 60 - y[1]

def thoiGian(x):
    return f"{x//60} gio {x%60} phut"

a = {}
t = int(input())
while t > 0:
    t -= 1
    ma = input()
    ten = input()
    x = [int(i) for i in input().split(":")]
    y = [int(i) for i in input().split(":")]
    a[(ma, ten)] = time(x, y)

a = sorted(a.items(), key = lambda x : (-x[1], x[0][0]))
for i in a:
    print(i[0][0], i[0][1], thoiGian(i[1]))