from collections import deque
n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]
sty, stx, edy, edx = 0, 0, n, m
used = [[0]*m for _ in range(n)]

MIN = 21e8
def find(y, x, edy, edx):
    global MIN
    q = deque()
    q.append((y, x, 1))

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        y, x, cnt = q.popleft()
        if y == edy and x == edx:
            MIN = min(MIN, cnt)
            return
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if used[dy][dx] == 1: continue
            if miro[dy][dx] == '0': continue
            used[dy][dx] = 1
            q.append((dy, dx, cnt+1))

find(0, 0, n-1, m-1)
print(MIN)