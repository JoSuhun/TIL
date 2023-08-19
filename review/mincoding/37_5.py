from collections import deque

arrs = [[0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]]
sty, stx = map(int, input().split())
edy, edx = map(int, input().split())

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]



def bfs(sty, stx, edy, edx):
    q = deque()
    q.append([sty, stx, 0])

    used = [[0] * 4 for _ in range(4)]

    used[sty][stx] = 1
    while q:
        nowy, nowx, level = q.popleft()
        if nowy == edy and nowx == edx: return level
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>3 or dx>3: continue
            if arrs[dy][dx] == 1: continue
            if used[dy][dx] == 1: continue
            q.append([dy, dx, level+1])
            used[dy][dx] = 1
ret = bfs(sty, stx, edy, edx)
print(ret)