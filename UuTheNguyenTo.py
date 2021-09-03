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
    dem = 0
    for i in n:
        if(snt(int(i))):
            dem += 1
    # print(dem)
    if snt(len(n)) and dem > len(n) - dem:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()