n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

def find():
    ans = 0
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                ans += 1
    return ans

def virus(y, x):
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    l = max(n, m)
    cnt = 0
    for i in range(4):
        for k in range(l):
            dy = y + directy[i]*k
            dx = x + directx[i]*k
            if dx<0 or dy<0 or dx>m or dy>n: continue
            if mapp[dy][dx] == 0: mapp[dy][dx] = 2

for i in range(m):
    for j in range(n):
        if mapp[i][j] == 2:
            virus(i, j)

visit = [[0]*m for _ in range(n)]
MAX = 0
def make(cnt):
    global MAX
    if cnt == 3:
        ret = find()
        MAX = max(MAX, ret)
        return
    for i in range(m):
        for j in range(n):
            if visit[i][j] == 1: continue
            visit[i]
            if mapp[i][j] == 0:


