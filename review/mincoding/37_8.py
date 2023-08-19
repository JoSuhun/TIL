# 37_4와 비교
from collections import deque

n, m = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(n)]

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
def bfs(y, x):
    q = deque()
    q.append([y,x])
    arrs[y][x] = 0
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if arrs[dy][dx] == 0: continue
            arrs[dy][dx] = 0
            q.append([dy, dx])
    return arrs

cnt = 0
for i in range(n):
    for j in range(m):
        if arrs[i][j] == 1:
            cnt += 1
            bfs(i,j)


print(cnt)
