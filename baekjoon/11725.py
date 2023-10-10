import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visit = [0]*(n+1)
ans = [0]*(n+1)
q = deque()

def find(now):
    q.append(now)
    while q:
        now = q.popleft()
        visit[now] = 1
        for next in lst[now]:
            if visit[next] == 1: continue
            ans[next] = now
            q.append(next)

find(1)
for i in range(2, n+1):
    print(ans[i])