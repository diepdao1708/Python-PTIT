def run():
    n = input()
    tong = 0
    tich = -1
    for i in range(0, len(n)):
        if i % 2 == 1:
            tong += int(n[i])
        if i % 2 == 0:
            if n[i] != '0' and tich == -1:
                tich = int(n[i])
            elif n[i] != '0' and tich != -1:
                tich = tich * int(n[i])
            
    if(tich == -1):
        print(0, tong)
    else:
        print(tich, tong)

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()