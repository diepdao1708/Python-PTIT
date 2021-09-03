def run():
    n = input()
    Sum = 0
    for i in n:
        Sum = Sum*10 + int(i)
        Sum %= 3

    if Sum == 0:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()