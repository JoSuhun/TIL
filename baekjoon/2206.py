n, m = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(n)]
sty, stx = 0, 0
edy, edx = n-1, m-1
MIN = 21e8
visit = [[0]*m for _ in range(n)]
visit[0][0] = 1

def find(sty, stx, edy, edx, cnt, bomb):
    global MIN


    if sty == edy and stx == edx:
        MIN = min(MIN, cnt)
        return

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]

    for i in range(4):
        dy = sty + directy[i]
        dx = stx + directx[i]
        if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
        if visit[dy][dx] == 1: continue
        if mapp[dy][dx] == 0:
            visit[dy][dx] = 1
            find(dy, dx, edy, edx, cnt+1, bomb)
            visit[dy][dx] = 0
        elif mapp[dy][dx] == 1:
            if not bomb:
                mapp[dy][dx] = 0
                visit[dy][dx] = 1
                find(dy, dx, edy, edx, cnt+1, 0)
                mapp[dy][dx] = 1
                visit[dy][dx] = 0

find(0, 0, n-1, m-1, 1, 1)
print(MIN)