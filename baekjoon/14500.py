n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]



MAX = -1

def find(y, x, cnt, SUM):
    global MAX

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    if cnt == 3:
        MAX = max(MAX, SUM)
        return
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
        if visit[dy][dx] == 1: continue
        visit[dy][dx] = 1
        find(dy, dx, cnt+1, SUM+mapp[dy][dx])
        visit[dy][dx] = 0

MAX2 = -1
def findA(y, x, cnt, SUM):
    global MAX2
    if cnt == 3:
        print(y, x, SUM)
        MAX2 = max(MAX2, SUM)
        return
    direct = [[(0, 1), (0, 2), (1, 1)], [(0, 1), (0, 2), (-1, 1)],
              [(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)]]
    for i in range(4):
        for directy, directx in direct[i]:
            dy, dx = y+directy, x+directx
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if visit[dy][dx] == 1: continue
            visit[dy][dx] = 1
            findA(dy, dx, cnt+1, SUM+mapp[dy][dx])
            visit[dy][dx] = 1


for i in range(n):
    for j in range(m):
        visit = [[0]*m for _ in range(n)]
        visit[i][j] = 1
        find(i, j, 0, mapp[i][j])

for i in range(n):
    for j in range(m):
        visit = [[0]*m for _ in range(n)]
        visit[i][j] = 1
        findA(i, j, 0, mapp[i][j])

print(MAX2)