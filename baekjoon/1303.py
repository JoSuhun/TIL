from collections import deque
n, m = map(int, input().split())

lst = [list(input()) for _ in range(m)]
my = deque()
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'B':
            my.append((i, j))

def make(y, x, mySum, reSum):
    y, x = deque.popleft()

    used = [[0]*n for _ in range(m)]
    while my:
        directy = [1, -1, 0, 0]
        directx = [0, 0, 1, -1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if used[dy][dx] == 1: continue