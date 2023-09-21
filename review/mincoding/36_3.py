import heapq
n, m, p = map(int, input().split())
# n 마을 수 // m 도로 수 // p 도착지
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]: continue

        for next in graph[node]:
            cost = next[1] + distance[node]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

inf = int(21e8)
distance = [inf] * (n+1)
dijkstra(p)
pToHome = distance

MAX = -1
for i in range(1, n+1):
    inf = int(21e8)
    distance = [inf] * (n + 1)
    dijkstra(i)

    MAX = max(distance[p]+pToHome[i], MAX)
print(MAX)