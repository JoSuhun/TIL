T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arrs = [[0]*n for _ in range(n)]

    for i in range(n//2-1, n//2+1):
        for j in range(n//2-1, n//2+1):
            if i==j: arrs[i][j] = 2
            else: arrs[i][j] = 1

    directy = [0, 0, 1, 1, -1, -1, 1, -1]
    directx = [1, -1, 1, -1, 1, -1, 0, 0]

    for i in range(m):
        y, x, c = map(int, input().split()) # 흑1 // 백2
        y-=1
        x-=1
        arrs[y][x] = c
        for arr in arrs:
            print(*arr)
        now = 1
        while True:
            for k in range(8):
                dy = y + directy[k] * now
                dx = x + directx[k] * now
                if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
                if arrs[dy][dx] != c:
                    arrs[dy][dx] = c
            now += 1

    for arr in arrs:
        print(*arr)