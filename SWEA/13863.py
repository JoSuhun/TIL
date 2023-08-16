T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        if arr[N-1][i] == 2:
            y, x = N-1, i

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if dy<0 or dx<0 or dy>=N or dx>=N: continue
        if arr[dy][dx] != 0: continue