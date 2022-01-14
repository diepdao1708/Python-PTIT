def run():
    a = [int(i) for i in input().split()]
    n = int(a[0])
    b = int(a[1])
    sb = ""
    while (n > 0):
        m = n % b
        if m >= 10:
            sb += str(chr(55 + m))
        else:
            sb += str(m)
        n = int(n / b)
    print(sb[::-1])

def main():
    t = int(input())
    for i in range(t):
        run()

main()
