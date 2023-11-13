import heapq
import sys
input = sys.stdin.readline
n, m, x = map(int, input().split())
# n 노드 수 // m 간선 수 // x 목적지 노드 번호

mapp = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    mapp[st].append((ed, cost))

def find(now, ret):
    q = []
    visit = [0] * (n + 1)
    ret[now] = 0
    heapq.heappush(q, (0, now))
    MAX = -1
    while q:
        cost, now = heapq.heappop(q)
        MAX = max(MAX, cost)
        visit[now] = 1
        for next in mapp[now]:
            next_node, plus = next
            if visit[next_node] == 1: continue
            if ret[next_node] > ret[now]+plus:
                ret[next_node] = ret[now]+plus
                heapq.heappush(q, (ret[next_node], next_node))


inf = 21e8
ret = [inf]*(n+1)
find(x, ret)
ans = -1
for i in range(1, n+1):
    ret2 = [inf] * (n + 1)
    find(i, ret2)
    ans = max(ans, ret[i]+ret2[x])
print(ans)
