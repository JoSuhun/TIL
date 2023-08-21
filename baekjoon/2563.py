arrs = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    stx, sty = map(int, input().split())
    for i in range(sty, sty+10):
        for j in range(stx, stx+10):
            arrs[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arrs[i][j] == 1:
            cnt +=1
print(cnt)
