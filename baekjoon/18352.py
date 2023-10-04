from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
# 도시 개수 n // 도로 개수 m // 거리 k // 출발 x
lst = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)

visit = [0]*(n+1)

def make(start):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        now = q.popleft()
        for next in lst[now]:
            if visit[next] != 0: continue
            visit[next] = visit[now] + 1
            q.append(next)


make(x)

if k+1 in visit:
    for i in range(1, n+1):
        if visit[i] == k+1: print(i)
else:
    print(-1)