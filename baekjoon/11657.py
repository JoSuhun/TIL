import heapq, sys
input = sys.stdin.readline
n, m = map(int, input().split())    # n 도시 개수 // m 노선 개수
lst = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    lst[st].append((ed, cost))
visit = [0]*(n+1)
inf = int(21e8)
ret = [inf]*(n+1)
ret[1] = 0
q = []
heapq.heappush(q, (0, 1))
flag = 0
while q:
    cost, now = heapq.heappop(q)
    if visit[now]: continue
    visit[now] = 1
    if flag == 1: break
    for next in lst[now]:
        node = next[0]
        plus = next[1]
        if ret[now]+ plus <= 0:
            flag = 1
            break
        if ret[node] > ret[now]+plus:
            ret[node] = ret[now]+plus
            heapq.heappush(q, (ret[node], node))

if flag: print(-1)
else:
    for i in range(2, n+1):
        if not visit[i]: print(-1)
        else: print(ret[i])