from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    info = list(map(int, input().split()))
    node = info.pop(0)
    for i in range(len(info)//2):
        graph[node].append((info[2*i],info[2*i +1]))
        if graph[info[2*i]] not in (node, info[2*i+1]):
            graph[info[2*i]].append((node, info[2*i + 1]))

def find(now):
    used = [0] * (n + 1)
    MAX = -1
    MAXnode = -1
    q = deque()
    q.append((now, 0))
    used[now] = 1
    while q:
        now, distance = q.popleft()
        if distance > MAX:
            MAX = max(MAX, distance)
            MAXnode = now
        for next in graph[now]:
            if used[next[0]] == 1: continue
            used[next[0]] = 1
            q.append((next[0], distance+next[1]))

    return MAXnode, MAX

node1, dist = find(1)
node2, result = find(node1)
print(result)

