import math

def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def run():
    n = input()
    res = ""
    if len(n) < 4:
        res = n
    else:
        res = n[len(n)-4:]
    if snt(int(res)):
        print("YES")
    else:
        print("NO")
def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()