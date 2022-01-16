from operator import le


t = int(input())
a = []
while t > 0:
    t -= 1
    s = input()
    if s != "":
        a.append(s)
    else:
        print(a[0], end="")
        print(": ", end="")
        print(len(a) - 1)
        a.clear()
    
print(a[0], end="")
print(": ", end="")
print(len(a) - 1)