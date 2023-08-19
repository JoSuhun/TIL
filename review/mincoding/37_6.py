from collections import deque

arrs = [list(map(int, input().split())) for _ in range(4)]

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

def bfs(y, x):
    cnt = 0
    used = [[0]*6 for _ in range(4)]
    q = deque()
    q.append([y, x])
    used[y][x] = 1
    while q:
        nowy, nowx = q.popleft()

        if arrs[nowy][nowx] == 2:
            cnt += 1

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>3 or dx>5: continue
            if used[dy][dx] == 1: continue
            if arrs[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx])

    return cnt

print(bfs(0,0))
