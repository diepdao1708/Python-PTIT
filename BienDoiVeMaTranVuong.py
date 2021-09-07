def run():
    s = [int(i) for i in input().split()]
    
    
    if s[0] > s[1]:
        n = s[0] - s[1]
        for i in range(s[0]):
            tmp = input()
            if i % 2 == 1 and n > 0:
                print(tmp) 
                n -= 1
            elif n <= 0:
                print(tmp)
    elif s[0] < s[1]:
        for i in range(s[0]):
            tmp = [int(j) for j in input().split()]
            m = s[1] - s[0]
            for j in range(0, len(tmp)):
                if j % 2 == 0 and m >= 0:
                    print(tmp[j], end=" ")
                    m -= 1
                elif m < 0:
                    print(tmp[j], end=" ")
            print("")
    else:
        for i in range(s[0]):
            tmp = input()
            print(tmp)

run()