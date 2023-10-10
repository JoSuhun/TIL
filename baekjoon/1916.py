import sys, heapq
input = sys.stdin.readline
n = int(input())    # n 도시의 개수
m = int(input())    # m 버스의 개수
lst = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    lst[st].append((ed, cost))
start, end = map(int, input().split())
visit = [0]*(n+1)
inf = int(21e8)
ret = [inf]*(n+1)
ret[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    cost, now = heapq.heappop(q)
    if visit[now] == 1: continue
    visit[now] = 1
    for next in lst[now]:
        node = next[0]
        plus = next[1]
        if ret[node] > ret[now]+plus:
            ret[node] = ret[now]+plus
            heapq.heappush(q, (ret[node], node))
print(ret[end])
