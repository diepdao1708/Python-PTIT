import math

def run():
    s = input()
    Sum = 0
    res = ""
    for i in range(0, len(s)):
        if s[i] >= '0' and s[i] <= '9':
            Sum += int(s[i])
        else:
            res += s[i]
    res = sorted(res)
    kq = ""
    for i in res:
        kq += i
    kq += str(Sum)
    print(kq)
    

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
