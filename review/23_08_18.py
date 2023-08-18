# 소방훈련 문제

from collections import deque

n = int(input()) # 맵의 크기 n*n
mapArr = [list(input()) for _ in range(n)]
sty, stx = map(int, input().split())


def shg(sty, stx, edy, edx, type):
    q = deque()
    q.append([sty, stx, 0])
    used = [[0] * n for _ in range(n)]
    used[sty][stx] = 1
    while q:
        now = q.popleft()
        yy, xx, level = now
        if yy == edy and xx == edx:
            return level

        directy = [0, 0, 1, -1]
        directx = [1, -1, 0, 0]

        for i in range(4):
            dy = yy + directy[i]
            dx = xx + directx[i]
            if dy < 0 or dx < 0 or dy > n - 1 or dx > n - 1: continue
            if used[dy][dx] == 1: continue
            if mapArr[dy][dx] == '#': continue
            if type == 0:
                if mapArr[dy][dx] == '$': continue
            used[dy][dx] = 1
            q.append([dy, dx, level+1])


lst = []
for y in range(n):
    for x in range(n):
        if mapArr[y][x] == '$':
            fy = y
            fx = x
        if mapArr[y][x] == 'A':
            lst.append((y,x))


MIN = 21e8
ans = 0

for a in lst:
    MIN = min(MIN, ((shg(a[0], a[1], sty, stx, 0))+(shg(a[0],a[1], fy, fx, 1))))
print(MIN)