n = int(input())    # n*n
arrs = [list(input()) for _ in range(n)]

mapp = [['']*n for _ in range(n)]

directy = [-1, -1, -1, 0, 0, 1, 1, 1]
directx = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(n):
        if arrs[i][j] != '.':
            mapp[i][j] = '*'
        else:
            SUM = 0
            for k in range(8):
                dy = i + directy[k]
                dx = j + directx[k]
                if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
                if arrs[dy][dx] != '.':
                    SUM += int(arrs[dy][dx])
            if SUM >= 10:
                mapp[i][j] = 'M'
            else: mapp[i][j] = SUM
for m in mapp:
    print(*m, sep='')