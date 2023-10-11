from collections import deque
n, m = map(int, input().split())    # n*n 도시 // 치킨집 최대 m개
mapp = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 2:
            chicken.append((i, j))
        if mapp[i][j] == 1:
            home.append((i, j))

def find(sty, stx, edy, edx):
    q = deque([sty, stx, ])
    used = [[0]*n for _ in range(n)]

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]

    while q:
        nowy, nowx = q.popleft()
        used[nowy][nowx] = 1
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if used[dy][dx] == 1: continue