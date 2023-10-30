import heapq
v, e = map(int, input().split())    # v 정점 // e 간선
nodes = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    heapq.heappush(nodes, (cost, a, b))

boss = [0]*(v+1)
for i in range(v+1):
    boss[i] = i


def findboss(mem):
    if mem == boss[mem]:
        return mem
    else:
        boss[mem] = findboss(boss[mem])
        return boss[mem]

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa==fb: return
    else: boss[fb] = fa


ans = 0
for i in range(e):
    cost, a, b = heapq.heappop(nodes)
    if findboss(a) != findboss(b):
        union(a, b)
        ans += cost
print(ans)