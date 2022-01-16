def time(x, y):
    return y[0] * 60 + y[1] - x[0] * 60 - x[1]

a = {}
t = int(input())
while t > 0:
    t -= 1
    name = input()
    x = [int(i) for i in input().split(":")]
    y = [int(i) for i in input().split(":")]
    luong_mua = int(input())
    if name not in a:
        a[name] = (time(x, y), luong_mua)
    else:
        ans = a[name]
        a[name] = (ans[0] + time(x, y), ans[1] + luong_mua)
    
k = 1
for i in a:
    print('T{:02d}'.format(k), end=" ")
    k += 1
    tmp = a.get(i)
    print(i, "{:.2f}".format(round(tmp[1] * 60 / tmp[0], 2)))

'''
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
'''
