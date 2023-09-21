import heapq
n, m, k = map(int, input().split())
# n 노드 // m 간선 // k 반복 횟수

start, end = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))



def dijkstra(start, p):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist: continue

        for next in graph[node]:
            cost = distance[node] + next[1] + p
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


p = [0]
for _ in range(k):
    p.append(p[_]+int(input()))
for v in p:
    inf = int(21e8)
    distance = [inf] * (n + 1)
    dijkstra(start, v)

    print(distance[end])