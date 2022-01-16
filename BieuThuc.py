def solve(s):
    index_stack = 0
    count = 0
    stack = []
    dd = {}
    for i in s:
        if i == "(":
            count += 1
            index_stack = count
            stack.append(index_stack)
        elif i == ")":
            while index_stack in dd:
                index_stack -= 1
            dd[index_stack] = 1
            stack.append(index_stack)
    for i in stack:
        print(i, end=" ")

T = int(input())
while T > 0:
    T -= 1
    s = input()
    solve(s)
    print()
