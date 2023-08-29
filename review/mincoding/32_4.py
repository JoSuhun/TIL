lst = [list(map(int, input())) for _ in range(5)]
n1, n2 = map(int, input().split())

lst[n1].sort()
lst[n2].sort()
for l in lst:
    print(l[0], end=' ')