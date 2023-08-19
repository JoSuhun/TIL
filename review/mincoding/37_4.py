import quopri
from collections import deque
ground = [list(map(int, input().split())) for _ in range(4)]

directx = [0, 0, 1, -1]
directy = [1, -1, 0, 0]

def bfs(y, x):
    q = deque()
    q.append([y, x])
    size = 1
    ground[y][x] = 0
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>3 or dx>3: continue
            if ground[dy][dx] == 0: continue
            q.append([dy,dx])
            ground[dy][dx] = 0
            size += 1
    return size

print(bfs(0,0))