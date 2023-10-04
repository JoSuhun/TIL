from collections import deque
n = int(input())
arr = [[] for _ in range(n+1)]
visit = [0]*(n+1)
cost = [0]*(n+1)
for i in range(n):
    lst = list(map(int, input().split()))
    c = lst.pop(0)
    cost[i+1] = c
    for v in lst:
        if v == -1: break
        arr[v].append(i+1)
        visit[i+1] += 1

q = deque()
for i in range(1, n+1):
    if visit[i] == 0:
        q.append(i)
ans = [0]*(n+1)
while q:
    now=q.popleft()

    for next in arr[now]:
        visit[next] -= 1
        ans[next] = max(ans[next], ans[now]+cost[now])
        if visit[next] == 0:
            q.append(next)

for i in range(1, n+1):
    print(ans[i]+cost[i])