from collections import deque
n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n+1)]


def virus(y, x):
    q = deque()
    q.append((y, x))
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if visit[dy][dx] == 1: continue
            if mapp[dy][dx] == 0:
                visit[dy][dx] = 1
                mapp[dy][dx] = 2
                q.append((dy, dx))