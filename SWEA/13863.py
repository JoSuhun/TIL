T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        if arr[N-1][i] == '2':
            s = N-1
            e = i

    flag = 0
    used = [[0] * N for _ in range(N)]

    def miro(y, x):
        global flag

        if arr[y][x] == '3':
            flag = 1
            return

        directy = [0, 0, 1, -1]
        directx = [1, -1, 0, 0]

        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy<0 or dy>=N or dx<0 or dx>=N: continue
            if arr[dy][dx] == '1': continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            miro(dy,dx)


    miro(s, e)
    print(f'#{tc} {flag}')