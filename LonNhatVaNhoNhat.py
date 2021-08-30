def run():
    while 1:
        n = int(input())
        if n == 0:
            return
        lst = []
        for i in range(n):
            lst.append(int(input()))
        if n == 1:
            print("BANG NHAU")
            continue
        lst.sort()
        if lst[0] == lst[n - 1]:
            print("BANG NHAU")
        else:
            print(lst[0], lst[n - 1])
run()
