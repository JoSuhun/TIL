import heapq


def dijkstra(start):
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


T = int(input())

for tc in range(1, T+1):
    e, m = map(int, input().split())
    graph = [[] for _ in range(m)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    inf = int(21e8)
    distance = [inf]*m

    dijkstra(0)
    print(f'#{tc} {distance[e]}')