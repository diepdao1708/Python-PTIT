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
    for i in range(0, len(n)):
        if snt(i) == True and snt(int(n[i])) == False:
            print("NO")
            return
        if snt(i) == False and snt(int(n[i])) == True:
            print("NO")
            return
    print("YES")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()