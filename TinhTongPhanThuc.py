def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def run():
    n = int(input())
    res = 0.0
    if n % 2 == 0:
        i = 2
        while i <= n:
            res += float(1 / i)
            i += 2
    else:
        i = 1
        while i <= n:
            res += float(1 / i)
            i += 2
    print("{:.6f}".format(res)) 

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()