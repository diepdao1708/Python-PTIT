import math

def run():
    n = int(input())
    dem = 0
    maxx = int((math.sqrt(n * 8 + 1) + 1) / 2) 
    for i in range(2, maxx):
        k = n - int(i * (i - 1) / 2)
        if(k % i == 0):
            dem += 1
    print(dem)
    
def main():
    t = int(input())
    for i in range(t):
        run()
main()