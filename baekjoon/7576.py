from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
# m 가로 // n 세로

tomatoes = [list(map(int, input().split())) for _ in range(n)]

def bfs(lst):
    q = deque(lst)
    ans = 0

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        nowy, nowx, cnt = q.popleft()
        ans = cnt
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if used[dy][dx] == 1: continue
            if tomatoes[dy][dx] < 0: continue
            used[dy][dx] = 1
            tomatoes[dy][dx] = tomatoes[nowy][nowx] + 1
            q.append((dy, dx, cnt+1))
    return ans

used = [[0] * m for _ in range(n)]
lst = []
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            used[i][j] = 1
            lst.append((i, j, 0))
flag = 1
ret = bfs(lst)
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            flag = 0
            break
    if flag == 0: break

if flag: print(ret)
else: print(-1)