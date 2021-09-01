x = []
def cs(s):
    Sum = 0
    s = "".join(reversed(s))
    for i in range(len(s)):
        if s[i] == '1':
            Sum += pow(2, i)
    return Sum

def pre(s):
    if len(s) > 22:
        return
    if len(s) > 0 and s[0] != "0":
        x.append(cs(s))
    pre("0" + s + "0")
    pre("1" + s + "1")

def BS(l, r, k):
    res = -1
    while l <= r:
        mid = int((l + r) / 2)
        if x[mid] < k:
            l = mid + 1
        elif x[mid] > k:
            res = mid
            r = mid - 1
        elif x[mid] == k:
            return mid
    return res
        
def run():
    a = [int(i) for i in input().split()]
    
    if a[2] == 2:
        pre("")
        pre("0")
        pre("1")
        x.append(0)
        x.sort()
        it1 = BS(0, len(x) - 1, a[0])
        it2 = BS(0, len(x) - 1, a[1])
        if x[it2] > a[1]:
            it2 -= 1
        print(it2 - it1 + 1)
        return
     
    dem = 0
    if a[0] <= 0 and a[1] >= 0:
        dem += 1

    if a[0] <= 1 and a[1] >= 1:
        dem += 1
    
    if a[0] <= 6643 and a[1] >= 6643 and a[2] == 3:
        dem += 1
    
    if a[0] <= 1422773 and a[1] >= 1422773 and a[2] == 3:
        dem += 1
        
    print(dem)
    
run()