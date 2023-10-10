import sys, heapq
input = sys.stdin.readline
v, e = map(int, input().split())    # v 정점 개수 // e 간선 개수
start = int(input())
lst = [[] for _ in range(v+1)]
for _ in range(e):
    st, ed, cost = map(int, input().split())
    lst[st].append((ed, cost))

inf = int(21e8)
ret = [inf]*(v+1)
visit = [0]*(v+1)
ret[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    cost, now = heapq.heappop(q)
    if visit[now]: continue
    visit[now] = 1
    for next in lst[now]:
        node = next[0]
        plus = next[1]
        if ret[node] > ret[now]+plus:
            ret[node] = ret[now]+plus
            heapq.heappush(q, (ret[node], node))

for i in range(1, v+1):
    if visit[i]: print(ret[i])
    else: print('INF')