from collections import deque
import copy

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

visit = [[0]*m for _ in range(n)]

virusPoint = []
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            virusPoint.append((i, j))

def virus():
    cnt = 0
    q = deque(virusPoint)
    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        nowy, nowx = q.popleft()
        visit[nowy][nowx]= 1
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if visit[dy][dx] == 1: continue
            if mapp[dy][dx] == 0:
                mapp[dy][dx] = 2
                q.append((dy, dx))
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                cnt += 1
    return cnt

backup = copy.deepcopy(mapp)
used = [[0] * m for _ in range(n)]
MAX = -1
def make(cnt):
    global mapp, MAX

    if cnt == 3:
        print(mapp)
        ret = virus()
        MAX = max(MAX, ret)
        mapp = backup
        return

    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                mapp[i][j] = 1
                make(cnt+1)
                mapp[i][j] = 0

make(0)
print(MAX)