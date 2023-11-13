from collections import deque
mapp = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

visit = [[0]*5 for _ in range(5)]
MIN = 21e8
def find(y, x):
    global MIN
    q = deque([(y, x, 0)])
    directy = [1, -1, 0, 0]
    directx = [0, 0, 1, -1]
    while q:
        nowy, nowx, cnt = q.popleft()
        visit[nowy][nowx] = 1
        if cnt>MIN: continue
        if mapp[nowy][nowx] == 1:
            MIN = min(MIN, cnt)
        for i in range(4):
            dy = nowy+directy[i]
            dx = nowx+directx[i]
            if dy<0 or dx<0 or dy>4 or dx>4: continue
            if mapp[dy][dx] == -1: continue
            if visit[dy][dx] == 1: continue
            q.append((dy, dx, cnt+1))
find(r, c)
if MIN == 21e8:
    print(-1)
else:
    print(MIN)