from collections import deque
T = int(input())


def miro(sty, stx, edy, edx):
    q = deque()
    q.append((sty, stx, 0))
    used = [[0]*n for _ in range(n)]

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    lst = [0]
    while q:
        nowy, nowx, cnt = q.popleft()
        if nowy == edy and nowx == edx:
            lst.append(cnt-1)

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if arrs[dy][dx] == 1: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append((dy, dx, cnt+1))
    return max(lst)


for tc in range(1, T+1):
    n = int(input())    #n*n미로
    arrs = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arrs[i][j] == 2:
                sty = i
                stx = j
            if arrs[i][j] == 3:
                edy = i
                edx = j
    ret = miro(sty, stx, edy, edx)
    print(f'#{tc} {ret}')