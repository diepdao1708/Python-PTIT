def check(a):
    if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
        return True
    return False

def End(a):
    if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
        return True
    return False

def run():
    T = 1
    while T == 1:
        a = [int(i) for i in input().split()]
        if End(a):
            return
        dem = 0
        while check(a) == False:
            x = abs(int(a[0]) - int(a[1]))
            y = abs(int(a[1]) - int(a[2]))
            z = abs(int(a[2]) - int(a[3]))
            t = abs(int(a[3]) - int(a[0]))
            a[0] = x
            a[1] = y
            a[2] = z
            a[3] = t
            dem += 1
        print(dem)

run()
