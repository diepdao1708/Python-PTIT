t = int(input())
while t > 0:
    s = input()
    res  = ""
    a = []
    for i in s:
        if i >= "0" and i <= "9":
            res += i
        elif res != "":
            a.append(int(res))
            res = ""
    if res != "":
        a.append(int(res))
    a = sorted(a)
    print(a[len(a) - 1])
    t -= 1
            
