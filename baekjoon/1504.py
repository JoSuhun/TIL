import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
lst = [[] for _ in range(n+1)]

for _ in range(e):
    st, ed, cost = map(int, input().split())
    lst[st].append((ed, cost))
    lst[ed].append((st, cost))

v1, v2 = map(int, input().split())
inf = 21e8
def find(start):
    ref = [inf] * (n + 1)
    ref[start] = 0
    visit = [0]*(n+1)
    q = []
    heapq.heappush(q, (0, start))   # cost 와 출발 노드

    while q:
        cost, now = heapq.heappop(q)
        if visit[now]: continue
        visit[now] = 1
        for next in lst[now]:
            next_node, plus = next
            if ref[next_node] > ref[now] + plus:
                ref[next_node] = ref[now] + plus
            heapq.heappush(q, (ref[next_node], next_node))
    return ref

startToNode = find(1)
v1Tov2 = find(v1)[v2]
nodeToEnd = find(n)

ans = min((startToNode[v1]+v1Tov2+nodeToEnd[v2]),
          (startToNode[v2]+v1Tov2+nodeToEnd[v1]))

if ans >= inf:
    print(-1)
else: print(ans)