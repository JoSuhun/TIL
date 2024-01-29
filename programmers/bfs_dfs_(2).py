# 네트워크
from collections import deque
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]: continue
        bfs(n, computers, i, visited)
        answer += 1
    return answer
def bfs(n, computers, i, visited):
    q = deque()
    q.append(i)
    while q:
        now = q.popleft()
        visited[now] = 1
        for i in range(n):
            if i == now: continue
            if visited[i]: continue
            if computers[now][i] == 1:
                q.append(i)

ret = solution(n, computers)
print(ret)