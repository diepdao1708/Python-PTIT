def N1(n):
    s1 = str(n)
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False

def N2(n):
    n = str(n)
    for i in range(0, len(n)):
        x = int(n[i])
        if x % 2 != 0:
            return False
    return True

def N3(n):
    n = int(len(str(n)))
    if n % 2 == 0:
        return True
    return False

def run():
    n = int(input())
    res =""
    for i in range(1, n):
        if N1(i) and N2(i) and N3(i):
            res += str(i) + " "
    print(res)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
