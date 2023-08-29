import copy

n, k = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(n)]

now = 0
while now < k:
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-1-i] = arrs[i][j]
    arrs = copy.deepcopy(new)
    now += 1
for arr in arrs:
    print(*arr)