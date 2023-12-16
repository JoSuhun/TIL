def dfs(nowy, nowx):
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    for i in range(4):
        dy, dx = nowy+directy[i], nowx+directx[i]
        if dy<0 or dy>n-1 or dx<0 or dx>m-1: continue
        if point[dy][dx] == 0: continue
        point[dy][dx] = 0
        dfs(dy, dx)

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())
    point = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        point[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if point[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)