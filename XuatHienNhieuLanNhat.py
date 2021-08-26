def run():
    n = int(input())
    s = input()
    a = s.split()
    count = {}
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    maxx = 0
    kq = 0
    for i in a:
        if count[i] > maxx:
            maxx = count[i]
            kq = i
    tmp = int(n / 2) 
    if maxx > tmp:
        print(kq)
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()

main()
