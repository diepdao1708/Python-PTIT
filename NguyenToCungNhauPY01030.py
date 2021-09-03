def gcd(a, b):
    while a > 0:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def run():
    n = [int(i) for i in input().split()]
    soD = 1
    soC = 9
    for i in range(1, n[1]):
        soD = soD * 10 
        soC = soC * 10 + 9
    dem = 0
    res = ""
    for i in range(soD, soC):
        if gcd(i, n[0]) == 1:
            res += str(i) + " "
            dem += 1
        if dem == 10:
            print(res)
            res = ""
            dem = 0
    print(res)
    

run()
