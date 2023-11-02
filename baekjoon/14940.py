from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
goaly, goalx = 0, 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            goaly, goalx = i, j

visit = [[0]*m for _ in range(n)]

def find(y, x):
    q = deque()
    q.append((y, x))
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        nowy, nowx = q.popleft()
        for k in range(4):
            dy = nowy+directy[k]
            dx = nowx+directx[k]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if mapp[dy][dx] == 0: continue
            if visit[dy][dx]: continue
            if dy==goaly and dx==goalx: continue
            visit[dy][dx] = visit[nowy][nowx] +1
            q.append((dy, dx))

find(goaly, goalx)
for i in range(n):
    for j in range(m):
        if i==goaly and j==goalx:continue
        if visit[i][j] == 0 and mapp[i][j] != 0:
            visit[i][j] = -1

for v in visit:
    print(*v)