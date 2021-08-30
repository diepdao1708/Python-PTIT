def run():
    n = int(input())
    ls = [int(i) for i in input().split()]
    count = {}
    for i in range(n):
        if ls[i] in count:
            count[ls[i]] += 1
        else:
            count[ls[i]] = 1
    for i in range(n):
        if count[ls[i]] % 2 == 1:
            print(ls[i])
            return

def main():
    t = int(input())
    for i in range(t):
        run()

main()
