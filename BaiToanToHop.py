import itertools

n, k = map(int, input().split())
a = set([int(i) for i in input().split()])
a = sorted(a)
res = itertools.combinations(a, k) 
for i in res:
    print(*i, sep=" ")