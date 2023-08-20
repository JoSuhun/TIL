from collections import deque


def bfs(sty, stx, edy, edx):
    q = deque()
    q.append((sty, stx))
    arrs[sty][stx] = 1
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    flag = 0
    while q:
        nowy, nowx = q.popleft()
        if nowy == edy and nowx == edx:
            flag = 1

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy < 0 or dx < 0 or dy > 99 or dx > 99: continue
            if arrs[dy][dx] == 1: continue
            arrs[dy][dx] = 1
            q.append((dy, dx))
    return flag



for i in range(10):
    n = int(input())    # tc
    arrs = [list(map(int, input())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if arrs[i][j] == 2:
                sty = i
                stx = j
            if arrs[i][j] == 3:
                edy = i
                edx = i

    ret = bfs(sty, stx, edy, edx)
    print(f'#{n} {ret}')
