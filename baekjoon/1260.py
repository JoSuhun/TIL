from collections import deque
n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)
for i in range(n+1):
    graph[i].sort()

dfs_ans = []
bfs_ans = []
used = [0]*(n+1)
def dfs(now):
    dfs_ans.append(now)
    used[now] = 1
    graph[now].sort()
    for node in graph[now]:
        if used[node] == 1: continue
        used[node] = 1
        dfs(node)
    return dfs_ans

def bfs(now):
    used = [0] * (n + 1)
    q = deque()
    q.append(now)
    used[now] = 1

    while q:
        now = q.popleft()
        bfs_ans.append(now)
        for node in graph[now]:
            if used[node] == 1: continue
            used[node] = 1
            q.append(node)

    return bfs_ans

dfs(s)
print(*dfs_ans)
bfs(s)
print(*bfs_ans)