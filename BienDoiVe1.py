import math

def run():
    t = 1
    while t:
        n = int(input())
        if n == 0:
            return
        count = 1
        while n != 1:
            count += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = n*3 + 1
        print(count)    

run()
