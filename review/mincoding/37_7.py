from collections import deque
n, m = map(int, input().split()) # n*m
arrs = [list(map(str, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arrs[i][j] == 'C':
            chy = i
            chx = j
        if arrs[i][j] == 'D':
            edy = i
            edx = j
        if arrs[i][j] == 'S':
            sty = i
            stx = j


directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
def bfs(sty, stx, edy, edx):
    q = deque()
    q.append([sty, stx, 0])
    used = [[0]*m for _ in range(n)]
    used[sty][stx] = 1

    while q:
        nowy, nowx, cnt = q.popleft()

        if nowy == edy and nowx == edx:
            return cnt

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if used[dy][dx] == 1: continue
            if arrs[dy][dx] == 'x': continue
            used[dy][dx] = 1
            q.append([dy, dx, cnt+1])

ans = 0
ans += bfs(sty, stx, chy, chx)
ans += bfs(chy, chx, edy, edx)
print(ans)