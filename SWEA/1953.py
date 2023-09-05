from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(n)]
    used = [[0]*m for _ in range(n)]
    used[r][c] = 1

    q = deque([[r, c, 1]])

    cnt = 1

    direct = [
        [[-1, 0], [1, 0], [0, -1], [0, 1]],
        [[1, 0], [-1, 0]],
        [[0, 1], [0, -1]],
        [[-1, 0], [0, 1]],
        [[1, 0], [0, 1]],
        [[0, -1], [1, 0]],
        [[-1, 0], [0, -1]]
    ]

    while q:
        nowy, nowx, now = q.popleft()
        if now == l:
            break
        for d in direct[arrs[nowy][nowx]-1]:
            dy = nowy + d[0]
            dx = nowx + d[1]

            if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
            if arrs[dy][dx] == 0: continue
            if used[dy][dx] == 1: continue

            if [-1*d[0], -1*d[1]] in direct[arrs[dy][dx]-1]:
                used[dy][dx] = 1
                cnt += 1
                q.append([dy, dx, now+1])

    print(f'#{tc} {cnt}')

