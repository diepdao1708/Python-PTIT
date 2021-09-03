def Check(n):
    vt = 0
    while vt + 2 < len(n):
        if n[vt] != n[vt + 2]:
            return False
        vt += 2
            
    return True

def run():
    n = input()
    if len(n) % 2 == 1 and len(n) > 2 and n[0] != n[1] and Check(n):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()