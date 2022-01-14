s = input()
a = [0] * 10
dd = [0] * 10

def hoan_vi(i):
    for j in range(0, len(s)):
        if dd[j] == 0:
            a[i] = j
            dd[j] = 1
            if i == len(s) - 1:
                for k in range(0, len(s)):
                    print(s[a[k]], end="")
                print()
            else:
                hoan_vi(i + 1)
            dd[j] = 0

hoan_vi(0)


