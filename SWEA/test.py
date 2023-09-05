from collections import deque

d = [[[0, 1], [0, -1], [1, 0], [-1, 0]],
     [[1, 0], [-1, 0]],
     [[0, 1], [0, -1]],
     [[-1, 0], [0, 1]],
     [[1, 0], [0, 1]],
     [[1, 0], [0, -1]],
     [[-1, 0], [0, -1]]]

for t in range(int(input())):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 1
    q = deque([[r, c, 1]])

    visit = [[0] * m for _ in range(n)]
    visit[r][c] = 1

    while q:
        now = q.popleft()

        x, y, depth = now
        if depth == l:
            break
        for dx, dy in d[arr[x][y] - 1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and ([-dx, -dy] in d[arr[nx][ny] - 1]):
                if visit[nx][ny] != 0: continue
                visit[nx][ny] = visit[x][y] + 1
                q.append([nx, ny, depth + 1])
                ans += 1

    print(f'#{t + 1} {ans}')