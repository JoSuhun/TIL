arrs = [[0]*3 for _ in range(3)]

n = int(input())
for _ in range(n):
    y, x, info = map(int, input().split())
    arrs[y][x] = list(map(int, str(info)))

m = int(input())
power = list(map(int, input().split()))

for p in power:
    for i in range(3):
        for j in range(3):
            if arrs[i][j] != 0 and arrs[i][j]:
                if arrs[i][j][-1]-p <=0:
                    arrs[i][j].pop(-1)
                else:
                    arrs[i][j][-1] -= p
cnt = 0
for arr in arrs:
    for a in arr:
        if a!= 0:
            cnt += len(a)

print(cnt)