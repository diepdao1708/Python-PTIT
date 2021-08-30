lst = ["000", "001", "010", "011", "100", "101", "110", "111"]

def cs(n):
    for i in range(len(lst)):
        if n == lst[i]:
            return i

def run():
    n = input()
    if len(n) % 3 == 2:
        n = "0" + n
    if len(n) % 3 == 1:
        n = "00" + n
    tmp = ""
    res = ""
    for i in range(len(n)):
        tmp += n[i]
        if len(tmp) == 3:
            res += str(cs(tmp))
            tmp = ""
    print(res)

run()
