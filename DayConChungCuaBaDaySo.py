def run():
    inp = [int(i) for i in input().split()]
    n1 = int(inp[0])
    n2 = int(inp[1])
    n3 = int(inp[2])
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ok = False
    i = 0
    j = 0
    k = 0
    res = ""
    while (i < n1) and (j < n2) and (k < n3):
        if a[i] < b[j] or a[i] < c[k]:
            i += 1
        elif b[j] < a[i] or b[j] < c[k]:
            j += 1
        elif c[k] < a[i] or c[k] < b[j]:
            k += 1
        else:
            res += str(a[i]) + " "
            ok = True
            i += 1
            j += 1
            k += 1
    if ok == False:
        print("NO")
    else:
        print(res)

def main():
    t = int(input())
    for i in range(t):
        run()
main()