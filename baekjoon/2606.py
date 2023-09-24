from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

used = [0]*(n+1)
def bfs(now):
    cnt = 0
    used[now] = 1
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        for next in graph[now]:
            if used[next] == 1: continue
            used[next] = 1
            cnt += 1
            q.append(next)
    return cnt

ret = bfs(1)
print(ret)