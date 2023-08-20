T = int(input())

def isSum(y, x):
    directx = [0, 0, 1, -1]
    directy = [1, -1, 0, 0]
    SUM = arrs[y][x]
    for i in range(4):
        for k in range(1, arrs[y][x]+1):
            dy = y + directy[i]*k
            dx = x + directx[i]*k
            if dy<0 or dy>n-1 or dx<0 or dx>m-1: continue
            SUM += arrs[dy][dx]
    return SUM

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(n)]

    MAX = -1
    for i in range(n):
        for j in range(m):
            ret = isSum(i, j)
            if ret > MAX:
                MAX = ret
    print(f'#{tc} {MAX}')
