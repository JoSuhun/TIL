from collections import deque
n, m = map(int, input().split())    # n*m
gril = [list(map(int, input().split())) for _ in range(m)]
sty, stx = map(int, input().split())

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

q = deque()
q.append((sty, stx, 0))
MAX = -1
while q:
    nowy, nowx, level = q.popleft()

    for k in range(4):
        dy = nowy + directy[k]
        dx = nowx + directx[k]
        if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
        if gril[dy][dx] != 0: continue
        gril[dy][dx] = gril[nowy][nowx] + 1
        q.append((dy, dx, level+1))

        if level>MAX:
            MAX = level

print(level)
