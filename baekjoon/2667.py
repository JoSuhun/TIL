from collections import deque

n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    used[y][x] = 1
    ans = 1

    directy = [0, 0, 1, -1]
    directx = [1, -1, 0, 0]
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if used[dy][dx] == 1: continue
            if mapp[dy][dx] == 0: continue
            ans += 1
            used[dy][dx] = 1
            q.append((dy, dx))
    return ans

used = [[0]*n for _ in range(n)]
result = []
cnt = 0
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1 and used[i][j] != 1:
            cnt += 1
            result.append(bfs(i, j))
print(cnt)
result.sort()
for c in result:
    print(c)
