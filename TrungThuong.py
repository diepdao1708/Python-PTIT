def run():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    lst.append(-1)
    # print(lst)
    maxx = 0
    res = 0
    tmp = 1
    for i in range(n):
        if lst[i] == lst[i + 1]:
            tmp += 1
        else:
            if maxx < tmp:
                maxx = tmp
                res = lst[i]
            tmp = 1
    print(res)
    
def main():
    t = int(input())
    for i in range(t):
        run()

main()
