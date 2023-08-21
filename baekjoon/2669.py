arrs = [[0]*100 for _ in range(100)]

for _ in range(4):
    stx, sty, edx, edy = map(int, input().split())
    for i in range(sty, edy):
        for j in range(stx, edx):
            arrs[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arrs[i][j] == 1:
            cnt += 1
print(cnt)