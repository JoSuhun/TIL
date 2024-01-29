from collections import deque
y, x = map(int, input().split())

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]
def bfs(nowy, nowx):
    q = deque([(nowy, nowx)])
    cheese = deque([])
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            ny, nx = nowy+directy[i], nowx+directx[i]
            if ny<0 or ny>y-1 or nx<0 or nx>x-1: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = 1
            if mapp[ny][nx] == 1:
                cheese.append((ny, nx))
            if mapp[ny][nx] == 0:
                q.append((ny, nx))


    return cheese

mapp = [list(map(int, input().split())) for _ in range(y)]

total = 0
for i in range(y):
    for j in range(x):
        if mapp[i][j] == 1:
            total += 1
cnt = 1

while True:
    visited = [[0 for _ in range(x)] for _ in range(y)]
    cheese = bfs(0, 0)
    for i, j in cheese:
        mapp[i][j] = 0
    ans = len(cheese)
    total -= ans
    if total == 0:
        print(cnt)
        print(ans)
        break
    else:
        cnt += 1
