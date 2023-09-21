from collections import deque
T = int(input())

def find():
    directy = [1, -1, 0, 0]
    directx = [0, 0, 1, -1]
    inf = int(21e8)
    cost = [[inf]*n for _ in range(n)]
    cost[0][0] = 0
    q = deque()
    q.append((0,0))
    while q:
        now = q.popleft()
        for i in range(4):
            dy = now[0] + directy[i]
            dx = now[1] + directx[i]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1: continue
            p = 0
            if mapp[dy][dx] > mapp[now[0]][now[1]]:
                p = mapp[dy][dx] - mapp[now[0]][now[1]]
            if cost[dy][dx] > cost[now[0]][now[1]] + p + 1:
                cost[dy][dx] = cost[now[0]][now[1]] + p + 1
                q.append((dy, dx))
    return cost[n-1][n-1]


for tc in range(1, T+1):
    n = int(input())
    mapp = [list(map(int, input().split())) for _ in range(n)]

    ret = find()

    print(f'#{tc} {ret}')