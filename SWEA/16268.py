# 풍선팡!
# n * m 격자판
# +모양

T = int(input())

def isSUM(y, x):
    SUM = arrs[y][x]
    direct_y = [0, 0, -1, 1]
    direct_x = [1, -1, 0, 0]
    for k in range(4):
        dy = i + direct_y[k]
        dx = j + direct_x[k]
        if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1: continue
        SUM += arrs[dy][dx]
    return SUM


for tc in range(1, T+1):
    n,m = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(n)]

    MAX = -21e8

    for i in range(n):
        for j in range(m):
            ret = isSUM(i,j)
            if ret > MAX:
                MAX = ret


    print(MAX)
