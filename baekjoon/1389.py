from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(now):
    q = deque()
    q.append(now)
    used = [now]
    cnt = [0]*(n+1)
    while q:
        now = q.popleft()
        for i in graph[now]:
            if i not in used:
                q.append(i)
                used.append(i)
                cnt[i] = cnt[now] + 1
    return sum(cnt)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+1)