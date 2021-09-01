def run():
    n = input()

    a = list(str(i) for i in n)
    i = len(a) - 2;
    while i >= 0 and a[i] <= a[i+1]:
        i -= 1
    if i < 0:
        print(-1)
        return
    k = i + 1
    for j in range(i + 1, len(a)):
        if a[j] < a[i] and a[j] > a[k]:
            k = j
    # print(i, k)
    a[i], a[k] = a[k], a[i]
    if a[0] == '0':
        print(-1)
        return
    for j in a:
        print(j, end = "")
    print()
    
    
def main():
    t = int(input())
    for i in range(t):
        run()
main()