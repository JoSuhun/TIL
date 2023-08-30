def dfs(y, x, SUM):
    global MIN
    if SUM > MIN:
        return
    if y == n-1 and x == n-1:
        if SUM < MIN: MIN = SUM
        return

    directy = [1, 0]
    directx = [0, 1]
    for i in range(2):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
        if used[dy][dx] == 1: continue
        used[dy][dx] = 1
        dfs(dy, dx, SUM+arrs[dy][dx])
        used[dy][dx] = 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arrs = [list(map(int, input().split())) for _ in range(n)]

    used = [[0]*n for _ in range(n)]
    used[0][0] = 1

    MIN = 21e8
    dfs(0,0,arrs[0][0])
    print(f'#{tc} {MIN}')
