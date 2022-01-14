def run():
    s = input()
    n = input()
    i = 0
    dem = 0
    while i + len(n) <= len(s):
        tmp = s[i: i + len(n)]
        if(n == tmp):
            dem += 1
            i += len(n)
        else:
            i += 1
    print(dem)

def main():
    t = int(input())
    for i in range(0, t):
        run()

main()

# import re
# def solve():
#     s = input()
#     tmp = input()
#     ans = re.findall(tmp, s)
#     print(len(ans))
    
# T = int(input())
# while T:
#     solve()
#     T -= 1