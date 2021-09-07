def b4():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Sum = 0
    count = 0
    for i in a:
        if str(i).isnumeric():
            Sum += int(i)
            count += 1
    print(Sum, float(Sum / count))

def b3():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            del a[i]
            i -= 1
        i += 1
    print(a)

def b5():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = []
    for i in a:
        b.append(i*i)
    b = sorted(b, reverse=True)
    print(b)

def b6():
    a = [1, "a", 34, "a", "b", 1, "c"]
    print(len(set(a)))

def run():
    b5()
run()