def run():
    s1 = input()
    s2 = s1[::-1]
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            print("NO") 
            return
    print("YES")

def main():
    t = int(input())
    for i in range(0, t):
        run()    

main()
