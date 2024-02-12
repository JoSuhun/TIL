# 게임 맵 최단거리

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

from collections import deque
def solution(maps):
    answer = 21e8
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    def bfs(cnt, y, x):
        nonlocal answer
        q = deque()
        directy = [0, 0, 1, -1]
        directx = [1, -1, 0, 0]
        q.append((1, 0, 0))
        while q:
            cnt, nowy, nowx = q.popleft()
            visited[nowy][nowx] = 1
            # if cnt > answer: continue
            if nowy == n-1 and nowx == m-1:
                answer = min(answer, cnt)
            for i in range(4):
                dy = nowy + directy[i]
                dx = nowx + directx[i]
                if dy<0 or dx<0 or dy>n-1 or dx>m-1: continue
                if visited[dy][dx] == 1: continue
                if maps[dy][dx] == 0: continue
                visited[dy][dx] = 1
                q.append((cnt+1, dy, dx))
    bfs(1, 0, 0)
    if answer == 21e8:
        return -1
    else:
        return answer

print(solution(maps))