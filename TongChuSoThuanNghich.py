def N1(n):
    s1 = str(n)
    s2 = s1[::-1]
    if s1 == s2:
        return True
    return False

def run():
    n = input()
    Sum = 0
    for i in n:
        Sum += int(i)

    if len(str(Sum)) > 1 and N1(Sum):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()