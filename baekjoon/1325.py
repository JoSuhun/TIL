import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())    # n 노드 수 // m 간선 수
lst = [[] for _ in range(n)]
for _ in range(m):
    e, s = map(int, input().split())
    e-=1
    s-=1
    lst[s].append(e)


def dfs(now):
    global cnt
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        for i in lst[now]:
            if used[i] == 1: continue
            used[i] = 1
            cnt += 1
            q.append(i)

    return cnt

ans = [0]*n
for i in range(n):
    cnt = 0
    used= [0]*n
    used[i] = 1
    dfs(i)
    ans[i] = cnt

MAX = max(ans)
for i in range(n):
    if ans[i] == MAX:
        print(i+1, end=' ')