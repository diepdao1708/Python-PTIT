def run():
    s1 = input()
    s2 = input()
    k = int(input())
    k -= 1
    res = ""
    for i in range(0, len(s1)+1):
        if i == k:
            res = res + s2 
            break
        res = res + s1[i]
    for i in range(k, len(s1)):
        res = res + s1[i]
    print(res)

run()
