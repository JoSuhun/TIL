from collections import deque
honey = [list(map(int, input().split())) for _ in range(4)]


def bfs(y, x, now):
    q = deque()
    q.append((y, x, now))

    used = [[0]*9 for _ in range(4)]
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        y, x, now = q.popleft()
        for k in range(4):
            dy = y + directy[k]
            dx = x + directx[k]
            if dy<0 or dx<0 or dy>3 or dx>8: continue
            if used[dy][dx] == 1: continue
            if honey[dy][dx] != honey[y][x]: continue
            used[dy][dx] = 1
            q.append((dy, dx, now+1))
    return now

MAX = -1
ans = 0
for i in range(4):
    for j in range(9):
        ret = bfs(i, j, 0)

        MAX = max(MAX, ret)
        ans = honey[i][j]
print(MAX*ans)