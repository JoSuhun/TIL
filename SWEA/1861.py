T = int(input())


ret = -1
def find(y, x, cnt):
    global ret

    if cnt > ret:
        ret = cnt

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    for k in range(4):
        dy = y + directy[k]
        dx = x + directx[k]
        if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
        if arrs[dy][dx] == arrs[y][x] + 1:
            find(dy, dx, cnt+1)


for tc in range(1, T+1):
    n = int(input())    # n*n 방
    arrs = [list(map(int, input().split())) for _ in range(n)]

    MAX = -21e8
    ans = 21e8
    lst  = []
    for i in range(n):
        for j in range(n):
            find(i, j, 0)
            if ret >= MAX:
                MAX = ret
                ans = arrs[i][j]
                lst.append((ans, MAX+1))
            ret = -1
    lst = sorted(lst, key=lambda x:(-x[1], x[0]))

    print(f'#{tc} {lst[0][0]} {lst[0][1]}')
