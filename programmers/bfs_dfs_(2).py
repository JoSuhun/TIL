# 네트워크
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i]: continue
        bfs(i, visited, computers, n)
        answer +=1
    return answer

def bfs(now, visited, computers, n):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        visited[now] = 1
        for i in range(n):
            if visited[i]: continue
            if computers[now][i]:
                q.append(i)


print(solution(n, computers))