def main():
    t = int(input())
    for i in range(0, t):
        a = input()
        b = input()
        a = sorted(a)
        b = sorted(b)
        if a == b:
            res = "Test " + str(i + 1) + ": " + "YES"
            print(res)
        else:
            res = "Test " + str(i + 1) + ": " + "NO"
            print(res)

main()
