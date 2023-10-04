from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    visit[b] += 1

q = deque()
for i in range(1, n+1):
    if visit[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    print(now, end=' ')
    for next in arr[now]:
        visit[next] -= 1
        if visit[next] == 0:
            q.append(next)