def run():
    n = input()
    Sum = 1
    for i in n:
        if i != '0':
            Sum *= int(i)

    print(Sum)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()