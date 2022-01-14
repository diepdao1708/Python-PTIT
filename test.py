def b1(List):
    tich = 1
    for i in List:
        tich *= i
    return tich
    
def make_car(hang, dong, **c):
    c['hang xe'] = hang
    c['ten dong'] = dong
    return c

def mul():
    a = [int(i) for i in input().split()]
    x = a[0]
    y = a[1]
    if x < 0 or y < 0:
        return 0
    res = 1
    if x == 0:
        res = 0
    for i in range(y):
        res *= x
    return res

