import math

def snt(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def run():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = []
    for i in a:
        if i not in count:
            count.append(i)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(0, len(count)):
        if snt(count[i]) and snt(count[len(count) - 1] - count[i]):
            print(i)
            return
    print("NOT FOUND")
run()
#  3 4 6 7