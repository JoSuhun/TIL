from collections import deque
n, m = map(int, input().split())
lst = [list(input()) for _ in range(m)]


def make(y, x, type):
    my = deque()
    my.append((y, x))
    lst[y][x] = 0
    cnt = 1

    while my:
        y, x = my.popleft()
        directy = [1, -1, 0, 0]
        directx = [0, 0, 1, -1]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dx<0 or dy>m-1 or dx>n-1: continue
            if lst[dy][dx] == 0: continue
            if lst[dy][dx] == type:
                lst[dy][dx] = 0
                my.append((dy,dx))
                cnt += 1
    return cnt ** 2

power = [0, 0]

for i in range(m):
    for j in range(n):
        if lst[i][j] == 'W':
            ret = make(i, j, 'W')
            power[0] += ret
        elif lst[i][j] == 'B':
            ret = make(i, j, 'B')
            power[1] += ret
print(*power)