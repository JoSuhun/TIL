import heapq

n, m = map(int, input().split())    # n 노드 수 // m 간선 수
start = 0
end = n-1

graph = [[] for _ in range(n+1)]    # graph 도착 출발 간선 및 비용 정보
for _ in range(m):
    a, b, c = map(int, input().split())     # a에서 출발해서 b로 도착하는 비용 c
    graph[a].append((b, c))

inf = int(21e8)
distance = [inf] * n    # distance 갱신할 최단 거리 테이블

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # 시작 노드 큐에 삽입하고 시작
    distance[start] = 0     # 시작노드 -> 시작노드 거리는 0으로 업데이트 하고 시작

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist: continue  # 큐에서 뽑은 거리가 이미 업데이트 된 거리보다 클 경우, 고려 안 함

        for next in graph[node]:    # 큐에서 뽑은 노드와 인접된 노드 탐색
            cost = distance[node] + next[1]     # 시작점에서 노드까지 + 노드에서 인접한 한 노드
            if cost < distance[next[0]]:
                distance[next[0]] = cost    # 업데이트!
                heapq.heappush(q, (cost, next[0]))  # 갱신된 경우만 큐에 넣어 줌

dijkstra(start)

if distance[end] == inf:
    print('impossible')
else:
    print(distance[end])
