from collections import deque
sky = [list(map(int, input().split())) for _ in range(4)]

q = deque()

for i in range(4):
    for j in range(5):
        if sky[i][j] == 1:
            q.append((i, j, 0))

directy = [0, 0, 1, -1, 1, -1, 1, -1]
directx = [1, -1, 0, 0, 1, -1, -1, 1]
while q:
    y, x, level = q.popleft()

    for i in range(8):
        dy = y + directy[i]
        dx = x + directx[i]
        if dy<0 or dx<0 or dy>3 or dx>4: continue
        if sky[dy][dx] == 1: continue
        sky[dy][dx] = 1
        q.append((dy, dx, level+1))

print(level)
