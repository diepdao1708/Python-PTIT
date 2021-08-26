def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = sorted(a)
    b = sorted(b)
    check = True
    for i in range(n):
        if a[i] > b[i]: 
            check = False
            break
    print("YES" if check else "NO")   
    
def main():
    t = int(input())
    for i in range(0, t):
        run()

main()