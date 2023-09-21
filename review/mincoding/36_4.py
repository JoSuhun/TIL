import heapq
import sys
input = sys.stdin.readline
m, n, k, x, y = map(int, input().split())
# c 간선 수 // p 노드 수 // k 시작 점 // a, b 경유지
# k - x - y // k - y - x

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    inf = int(21e8)
    distance = [inf] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]: continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance

kTo = dijkstra(k)
s1 = kTo[x] + dijkstra(x)[y]
s2 = kTo[y] + dijkstra(y)[x]
print(min(s1, s2))