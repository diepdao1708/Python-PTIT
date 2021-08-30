def run():
    a = [int(i) for i in input().split()]
    n = a[0]
    p = a[1]
    dem = 0
    for i in range(p, n + 1):
        tmp = i
        while tmp % p == 0:
            dem += 1
            tmp /= p
        
    print(dem) 

def main():
    t = int(input())
    for i in range(t):
        run()

main()