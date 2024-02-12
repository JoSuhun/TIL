# 게임 맵 최단거리

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    answer = 21e8
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    def dfs(cnt, y, x):
        nonlocal answer
        if cnt > answer: return
        if y == n-1 and x == m-1:
            answer = min(answer, cnt)
            return
        directy = [0, 0, 1, -1]
        directx = [1, -1, 0, 0]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if dy < 0 or dy > n-1 or dx < 0 or dx > m-1: continue
            if visited[dy][dx] == 1: continue
            if maps[dy][dx] == 0: continue
            visited[dy][dx] = 1
            dfs(cnt+1, dy, dx)
            visited[dy][dx] = 0
    dfs(1, 0, 0)
    if answer == 21e8:
        return -1
    else:
        return answer
print(solution(maps))