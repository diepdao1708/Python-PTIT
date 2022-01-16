from os import sep
import re


def tinh_gia(x, y):
    ans = y - x
    if ans <= 50:
        ans *= 100
        ans += ans * 0.02
    elif ans <= 100:
        ans = 50 * 100 + (ans - 50) * 150
        ans += ans * 0.03
    else:
        ans = 50 * 100 + 50 * 150 + (ans - 100) * 200
        ans += ans * 0.05
    return round(ans)

a = {}
T = int(input())
for t in range(1, T + 1):
    name = input()
    x = int(input())
    y = int(input())
    ma = "KH{:02d}".format(t)
    a[(ma, name)] = tinh_gia(x, y)
a = sorted(a.items(), key=lambda x: -x[1])
for i in a:
    print(i[0][0], i[0][1], i[1])

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''
