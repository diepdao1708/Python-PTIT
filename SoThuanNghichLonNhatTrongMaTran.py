import math

def stn(n):
    if n < 10:
        return False
    s1 = str(n)
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False

def run():
    n = [int(i) for i in input().split()]
    a = []
    maxx = -1
    for i in range(int(n[0])):
        x = [int(i) for i in input().split()]
        a.append(x)
        for j in x:
            if stn(j) == True:
                maxx = max(j, maxx)
    if maxx == -1:
        print("NOT FOUND")
        return
    print(maxx)
    for i in range(int(n[0])):
        for j in range(int(n[1])):
            if a[i][j] == maxx:
                print(f"Vi tri [{i}][{j}]")
    # print(maxx)

run()