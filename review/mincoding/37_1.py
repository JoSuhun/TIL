from collections import deque
n = int(input())        # n * n 배열
y1, x1, y2, x2 = map(int, input().split())  # 바이러스 들어갈 두 곳

arrs = [[0]*n for _ in range(n)]

directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

arrs[y1][x1] = 1
arrs[y2][x2] = 1

virus = [(y1, x1, 1),(y2, x2, 1)]

def bfs(virus):
    q = deque(virus)
    while q:
        nowy, nowx, level = q.popleft()

        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            if arrs[dy][dx] != 0: continue
            arrs[dy][dx] = arrs[nowy][nowx] + 1
            q.append((dy, dx, level+1))

bfs(virus)
print(arrs)
