def run():
    n = int(input())
    lst = [int(i) for i in input().split()]
    lst.sort()
    for i in range(1, lst[n - 1]):
        if i not in lst:
            print(i)
            return
    print(lst[n - 1] + 1) 
    
run()
