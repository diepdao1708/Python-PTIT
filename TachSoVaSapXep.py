def so(c):
    if c >= "0" and c <= "9":
        return True
    return False

def run():
    n = int(input())
    a = []
    for i in range(n):
        s = input()
        tmp = ""
        for i in s:
            if so(i):
                tmp += i
            else:
                if tmp != "":
                    a.append(int(tmp))
                tmp = ""
        if tmp != "":
            a.append(int(tmp))
    a = sorted(a)
    for i in a:
        print(i)
        

run()
