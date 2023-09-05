from collections import deque

T = int(input())

def check():
    q = deque(water)

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]

    while q:
        nowy, nowx, now = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if used[dy][dx] != 0: continue
            if arrs[dy][dx] == 'L':
                used[dy][dx] = now+1
                q.append((dy, dx, now+1))


for tc in range(1, T+1):
    n, m = map(int, input().split())
    arrs = [input() for _ in range(n)]
    used = [[0]*m for _ in range(n)]


    water = []
    for i in range(n):
        for j in range(m):
            if arrs[i][j] == 'W':
                water.append((i, j, 0))
    check()
    SUM = 0
    for i in range(n):
        for j in range(m):
            SUM += used[i][j]

    print(f'#{tc} {SUM}')