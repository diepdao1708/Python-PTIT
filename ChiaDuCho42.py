def run():
    count = {}
    dem = 0
    sl = 0
    t = 1
    while t:
        a = [int(i) for i in input().split()]
        sl += len(a)
        for i in a:
            tmp = int(i) % 42
            if tmp not in count:
                dem += 1
                count[tmp] = 1 
        if sl == 10:
            break
    print(dem)

run()
