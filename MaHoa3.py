al = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"

def vt(c):
    for i in range(len(al)):
        if c == al[i]:
            return i
            
def Sum(s):
    res = 0
    for i in range(len(s)):
        res += int(vt(s[i]))
    return res

def Rotate(s):
    res = Sum(s)
    res %= 26
    k = ""
    for i in range(len(s)):
        tmp = vt(s[i]) + res
        tmp %= 26
        k += al[tmp]
    return k

def Merge(a, b):
    k = ""
    for i in range(len(a)):
        tmp = vt(a[i]) + vt(b[i])
        tmp %= 26
        k += al[tmp]
    return k

def run():
    s = input()
    a = ""
    for i in range(0, int(len(s) / 2)):
        a += s[i]
    b = ""
    for i in range(int(len(s) / 2), len(s)):
        b += s[i]
    print(Merge(Rotate(a), Rotate(b)))
    
def main():
    t = int(input())
    for i in range(t):
        run()
main()